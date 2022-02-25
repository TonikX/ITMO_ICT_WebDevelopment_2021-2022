from djangorestframework_camel_case.parser import CamelCaseFormParser, CamelCaseJSONParser, CamelCaseMultiPartParser
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.views import APIView


class CamelCaseView(APIView):
    parser_classes = (CamelCaseFormParser, CamelCaseJSONParser, CamelCaseMultiPartParser)
    renderer_classes = (CamelCaseJSONRenderer,)
