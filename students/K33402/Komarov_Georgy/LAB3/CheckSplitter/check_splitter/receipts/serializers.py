from rest_framework import serializers

from receipts.models import Receipt, ReceiptItem, ReceiptItemPart
from users.models import User


class CheckItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'

    items = CheckItemSerializer(many=True)


class CheckItemPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItemPart
        fields = '__all__'

    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
