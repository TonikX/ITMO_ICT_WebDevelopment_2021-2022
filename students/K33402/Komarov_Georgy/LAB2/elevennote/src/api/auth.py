from rest_framework_jwt.authentication import exceptions


def jwt_response_payload_handler(token, user=None, request=None):
    if not user.is_confirmed:
        raise exceptions.AuthenticationFailed(
            'Your account is not confirmed. Please, follow link in your mail box.')
    return {'token': token}
