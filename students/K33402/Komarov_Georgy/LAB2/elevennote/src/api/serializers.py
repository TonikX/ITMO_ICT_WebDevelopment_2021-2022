from rest_framework import serializers
from accounts.models import User
from notes.models import Note, Tag
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text


class UserDoesNotExistAPIError(APIException):
    status_code = 400
    default_detail = 'Some users were not found.'

    def __init__(self, user=None):
        if user is not None:
            error_message = f'User {user} is not found. You can\'t add it to shared.'
            self.detail = {'shared_users': force_text(error_message)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}


class TagRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return obj.name

    def to_internal_value(self, name):
        tag, created = Tag.objects.get_or_create(name=name)
        return tag


class SharedUserRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return obj.email

    def to_internal_value(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserDoesNotExistAPIError(user=email)


class NoteSerializer(serializers.ModelSerializer):
    tags = TagRelatedField(many=True, required=False, queryset=Tag.objects.all())
    shared = SharedUserRelatedField(many=True, required=False, queryset=User.objects.all())

    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'tags', 'shared', 'pub_date')
