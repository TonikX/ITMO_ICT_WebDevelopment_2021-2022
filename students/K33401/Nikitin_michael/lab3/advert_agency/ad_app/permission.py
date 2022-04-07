from rest_framework.permissions import *


class IsApplicationOwner(BasePermission):
    permission_classes = [AllowAny]
    message = 'You are not allowed to view details, change or delete this application'

    def has_object_permission(self, request, view, obj):
        return obj.worker.user == request.user or obj.client.user == request.user
