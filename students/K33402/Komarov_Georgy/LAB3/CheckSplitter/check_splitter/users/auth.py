from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme


class JWTPasswordAuthScheme(SimpleJWTScheme):
    priority = 1

    def get_security_requirement(self, auto_schema):
        return {self.name: ['profile']}

    def get_security_definition(self, auto_schema):
        from drf_spectacular.settings import spectacular_settings

        security = {
            'type':  'oauth2',
            'flows': {
                'password': {
                    'tokenUrl':   spectacular_settings.OAUTH2_TOKEN_URL,
                    'refreshUrl': spectacular_settings.OAUTH2_REFRESH_URL,
                }
            }
        }
        return security
