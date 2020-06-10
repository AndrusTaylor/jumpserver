# ~*~ coding: utf-8 ~*~
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class SessionCommandSerializer(serializers.Serializer):
    """使用这个类作为基础Command Log Serializer类, 用来序列化"""

    id = serializers.UUIDField(read_only=True)
    user = serializers.CharField(max_length=64, label=_('User'))
    asset = serializers.CharField(max_length=128, label=_('Asset'))
    system_user = serializers.CharField(max_length=64, label=_('System user'))
    input = serializers.CharField(max_length=128)
    output = serializers.CharField(max_length=1024, allow_blank=True)
    session = serializers.CharField(max_length=36, label=_('Session'))
    risk_level = serializers.IntegerField(required=False)
    org_id = serializers.CharField(max_length=36, required=False, default='', allow_null=True, allow_blank=True)
    timestamp = serializers.IntegerField()

