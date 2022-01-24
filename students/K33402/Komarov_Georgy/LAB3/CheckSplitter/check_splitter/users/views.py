from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from drf_spectacular.utils import extend_schema_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.openapi import *
from users.serializers import ProfileSerializer, ProfileAvatarSerializer
from utils.views import CamelCaseView


class ProfilePermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class ProfileMixin(GenericAPIView, CamelCaseView):
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission,)

    queryset = User.objects.all()

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user


@extend_schema_view(
    get=user_retrieve_schema,
    put=user_update_schema,
    patch=user_update_schema,
    delete=user_destroy_schema,
)
class ProfileView(RetrieveUpdateDestroyAPIView, ProfileMixin):
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


@extend_schema_view(
    put=user_avatar_update_schema,
)
class ProfileAvatarView(UpdateModelMixin, ProfileMixin):
    serializer_class = ProfileAvatarSerializer
    parser_classes = (CamelCaseMultiPartParser,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
