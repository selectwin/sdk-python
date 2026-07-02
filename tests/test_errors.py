import json

from selectwin.errors import (
    APIError,
    AuthenticationError,
    CardError,
    ConflictError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    SelectwinError,
    ValidationError,
    error_from_status,
)


def env(**err):
    return json.dumps({"error": err}).encode("utf-8")


def test_maps_each_status_to_its_subclass():
    assert isinstance(error_from_status(401, env(code="unauthorized")), AuthenticationError)
    assert isinstance(error_from_status(403, env()), PermissionDeniedError)
    assert isinstance(error_from_status(404, env()), NotFoundError)
    assert isinstance(error_from_status(409, env()), ConflictError)
    assert isinstance(error_from_status(422, env()), ValidationError)
    assert isinstance(error_from_status(500, env()), APIError)


def test_every_error_is_a_selectwin_error():
    for status in (400, 401, 402, 403, 404, 409, 422, 429, 500, 503):
        assert isinstance(error_from_status(status, env()), SelectwinError)


def test_card_error_exposes_display_message_and_reversible():
    err = error_from_status(402, env(code="card_declined", displayMessage="Cartão recusado", reversible=True))
    assert isinstance(err, CardError)
    assert err.code == "card_declined"
    assert err.display_message == "Cartão recusado"
    assert err.reversible is True


def test_validation_error_exposes_params():
    params = [{"field": "email", "message": "invalid"}]
    err = error_from_status(400, env(code="validation_error", params=params))
    assert isinstance(err, ValidationError)
    assert err.params == params


def test_rate_limit_carries_retry_after():
    err = error_from_status(429, env(code="rate_limited"), retry_after=12)
    assert isinstance(err, RateLimitError)
    assert err.retry_after == 12


def test_accepts_dict_and_survives_garbage_bodies():
    err = error_from_status(404, {"error": {"code": "not_found", "message": "nope"}})
    assert err.code == "not_found"
    assert err.message == "nope"
    # Non-JSON / empty bodies must not blow up.
    assert isinstance(error_from_status(500, b"<html>oops</html>"), APIError)
    assert isinstance(error_from_status(500, None), APIError)


def test_carries_request_id_and_status():
    err = error_from_status(404, env(), request_id="req_123")
    assert err.request_id == "req_123"
    assert err.status_code == 404
