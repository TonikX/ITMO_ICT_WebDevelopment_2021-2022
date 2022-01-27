from rest_framework import generics, permissions

from users.models import User
from users.serializers import ProfileSerializer


class MyProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
