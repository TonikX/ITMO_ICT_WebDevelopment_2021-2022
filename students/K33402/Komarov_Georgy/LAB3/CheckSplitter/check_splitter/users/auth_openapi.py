from django.conf import settings
from drf_spectacular.contrib.rest_framework_simplejwt import TokenRefreshSerializerExtension
from drf_spectacular.extensions import OpenApiSerializerExtension, OpenApiViewExtension
from drf_spectacular.utils import extend_schema
from rest_framework import serializers

auth_login_schema_kwargs = {'summary': 'Авторизация пользователя'}
auth_login_schema = extend_schema(**auth_login_schema_kwargs)

auth_logout_schema_kwargs = {'summary': 'Выход'}
auth_logout_schema = extend_schema(**auth_logout_schema_kwargs)

auth_register_schema_kwargs = {'summary': 'Регистрация пользователя'}
auth_register_schema = extend_schema(**auth_register_schema_kwargs)

auth_password_change_schema_kwargs = {'summary': 'Смена пароля'}
auth_password_change_schema = extend_schema(**auth_password_change_schema_kwargs)

auth_password_reset_schema_kwargs = {'summary': 'Запрос на сброс пароля'}
auth_password_reset_schema = extend_schema(**auth_password_reset_schema_kwargs)

auth_password_reset_confirm_schema_kwargs = {'summary': 'Подтверждение сброса пароля'}
auth_password_reset_confirm_schema = extend_schema(**auth_password_reset_confirm_schema_kwargs)

auth_verify_email_schema_kwargs = {'summary': 'Подтверждение e-mail'}
auth_verify_email_schema = extend_schema(**auth_verify_email_schema_kwargs)

auth_resend_email_schema_kwargs = {'summary': 'Повторная отправка e-mail'}
auth_resend_email_schema = extend_schema(**auth_resend_email_schema_kwargs)

auth_token_refresh_schema_kwargs = {'summary': 'Обновить JWT токен'}
auth_token_refresh_schema = extend_schema(**auth_token_refresh_schema_kwargs)

auth_token_verify_schema_kwargs = {'summary': 'Валидировать JWT токен'}
auth_token_verify_schema = extend_schema(**auth_token_verify_schema_kwargs)


def get_token_serializer_class():
    from dj_rest_auth.app_settings import JWTSerializer, TokenSerializer

    if getattr(settings, 'REST_USE_JWT', False):
        return JWTSerializer
    else:
        return TokenSerializer


class RestAuthDetailSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True, required=False)


class RestAuthDefaultResponseView(OpenApiViewExtension):
    schema_override_kwargs = {}

    def view_replacement(self):
        class Fixed(self.target_class):
            @extend_schema(responses=RestAuthDetailSerializer, **self.schema_override_kwargs)
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed


class RestAuthLoginView(OpenApiViewExtension):
    target_class = 'dj_rest_auth.views.LoginView'

    def view_replacement(self):
        class Fixed(self.target_class):
            @auth_login_schema
            @extend_schema(responses=get_token_serializer_class())
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed


class RestAuthLogoutView(OpenApiViewExtension):
    target_class = 'dj_rest_auth.views.LogoutView'

    def view_replacement(self):
        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', None):
            get_schema_params = {'responses': RestAuthDetailSerializer}
        else:
            get_schema_params = {'exclude': True}

        class Fixed(self.target_class):
            @auth_logout_schema
            @extend_schema(**get_schema_params)
            def get(self, request, *args, **kwargs):
                pass  # pragma: no cover

            @auth_logout_schema
            @extend_schema(request=None, responses=RestAuthDetailSerializer)
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed


class RestAuthPasswordChangeView(RestAuthDefaultResponseView):
    schema_override_kwargs = auth_password_change_schema_kwargs
    target_class = 'dj_rest_auth.views.PasswordChangeView'


class RestAuthPasswordResetView(RestAuthDefaultResponseView):
    schema_override_kwargs = auth_password_reset_schema_kwargs
    target_class = 'dj_rest_auth.views.PasswordResetView'


class RestAuthPasswordResetConfirmView(RestAuthDefaultResponseView):
    schema_override_kwargs = auth_password_reset_confirm_schema_kwargs
    target_class = 'dj_rest_auth.views.PasswordResetConfirmView'


class RestAuthVerifyEmailView(RestAuthDefaultResponseView):
    schema_override_kwargs = auth_verify_email_schema_kwargs
    target_class = 'dj_rest_auth.registration.views.VerifyEmailView'


class RestAuthResendEmailVerificationView(RestAuthDefaultResponseView):
    schema_override_kwargs = auth_resend_email_schema_kwargs
    target_class = 'dj_rest_auth.registration.views.ResendEmailVerificationView'


class RestAuthJWTSerializer(OpenApiSerializerExtension):
    target_class = 'dj_rest_auth.serializers.JWTSerializer'

    def map_serializer(self, auto_schema, direction):
        from dj_rest_auth.app_settings import UserDetailsSerializer

        class Fixed(self.target_class):
            user = UserDetailsSerializer()

        return auto_schema._map_serializer(Fixed, direction)


class CookieTokenRefreshSerializerExtension(TokenRefreshSerializerExtension):
    target_class = 'dj_rest_auth.jwt_auth.CookieTokenRefreshSerializer'

    def get_name(self):
        return 'TokenRefresh'


class RestAuthRegisterView(OpenApiViewExtension):
    target_class = 'dj_rest_auth.registration.views.RegisterView'

    def view_replacement(self):
        from allauth.account.app_settings import EMAIL_VERIFICATION, EmailVerificationMethod

        if EMAIL_VERIFICATION == EmailVerificationMethod.MANDATORY:
            response_serializer = RestAuthDetailSerializer
        else:
            response_serializer = get_token_serializer_class()

        class Fixed(self.target_class):
            @auth_register_schema
            @extend_schema(responses=response_serializer)
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed


class RestAuthTokenRefreshView(OpenApiViewExtension):
    target_class = 'rest_framework_simplejwt.views.TokenRefreshView'
    match_subclasses = True

    def view_replacement(self):
        class Fixed(self.target_class):
            @auth_token_refresh_schema
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed


class RestAuthTokenVerifyView(OpenApiViewExtension):
    target_class = 'rest_framework_simplejwt.views.TokenVerifyView'

    def view_replacement(self):
        class Fixed(self.target_class):
            @auth_token_verify_schema
            def post(self, request, *args, **kwargs):
                pass  # pragma: no cover

        return Fixed
