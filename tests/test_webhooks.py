import hashlib
import hmac
import json

import pytest

from selectwin.errors import SignatureVerificationError
from selectwin.webhooks import construct_event

SECRET = "whsec_test_123"
PAYLOAD = json.dumps(
    {"id": "wbh_1", "type": "transaction.approved", "payload": {"object": {"id": "tra_1", "amount": 9990}}}
)


def sign(body, secret=SECRET):
    body_bytes = body.encode("utf-8") if isinstance(body, str) else body
    return "sha256=" + hmac.new(secret.encode(), body_bytes, hashlib.sha256).hexdigest()


def test_accepts_valid_signature_and_parses_event():
    ev = construct_event(PAYLOAD, sign(PAYLOAD), SECRET)
    assert ev.id == "wbh_1"
    assert ev.type == "transaction.approved"
    assert ev.payload.object["amount"] == 9990


def test_accepts_raw_hex_without_prefix_and_bytes_body():
    assert construct_event(PAYLOAD, sign(PAYLOAD)[len("sha256=") :], SECRET).id == "wbh_1"
    assert construct_event(PAYLOAD.encode("utf-8"), sign(PAYLOAD), SECRET).id == "wbh_1"


def test_rejects_tampered_body_and_wrong_secret():
    with pytest.raises(SignatureVerificationError):
        construct_event(PAYLOAD + " ", sign(PAYLOAD), SECRET)
    with pytest.raises(SignatureVerificationError):
        construct_event(PAYLOAD, sign(PAYLOAD), "whsec_other")


def test_rejects_missing_signature_and_secret():
    with pytest.raises(SignatureVerificationError):
        construct_event(PAYLOAD, None, SECRET)
    with pytest.raises(SignatureVerificationError):
        construct_event(PAYLOAD, "", SECRET)
    with pytest.raises(SignatureVerificationError):
        construct_event(PAYLOAD, sign(PAYLOAD), "")


def test_rejects_non_json_after_signature_passes():
    not_json = "not json"
    with pytest.raises(SignatureVerificationError):
        construct_event(not_json, sign(not_json), SECRET)


class TestV1ReplayScheme:
    T = 1_000_000

    def v1(self, secret=SECRET):
        return hmac.new(secret.encode(), f"{self.T}.{PAYLOAD}".encode(), hashlib.sha256).hexdigest()

    def test_verifies_within_tolerance(self):
        ev = construct_event(
            PAYLOAD,
            sign(PAYLOAD),
            SECRET,
            signature_v1=f"t={self.T},v1={self.v1()}",
            tolerance=300,
            now=lambda: self.T,
        )
        assert ev.id == "wbh_1"

    def test_rejects_timestamp_outside_tolerance(self):
        with pytest.raises(SignatureVerificationError):
            construct_event(
                PAYLOAD,
                sign(PAYLOAD),
                SECRET,
                signature_v1=f"t={self.T},v1={self.v1()}",
                tolerance=300,
                now=lambda: self.T + 1000,
            )

    def test_rejects_forged_v1(self):
        with pytest.raises(SignatureVerificationError):
            construct_event(PAYLOAD, sign(PAYLOAD), SECRET, signature_v1=f"t={self.T},v1=deadbeef")

    def test_rejects_malformed_v1(self):
        # A v1 header present but unparseable (missing t, missing v1, or junk) must raise — never
        # silently fall back to having checked only the legacy sha256= scheme (the body sig IS valid).
        for bad in ("t=1000000", "v1=deadbeef", "garbage"):
            with pytest.raises(SignatureVerificationError):
                construct_event(PAYLOAD, sign(PAYLOAD), SECRET, signature_v1=bad)
