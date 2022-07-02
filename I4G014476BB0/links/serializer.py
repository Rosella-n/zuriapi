from rest_framework import serializers
from links.models import Link
class LinkSerializer(serializers.Serializer):
    class Meta:
        model=Link
        feilds='__all__'

