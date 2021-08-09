from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from account.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'name',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class TokenBlacklistSerializer(serializers.Serializer):
    """
    Blacklist logged out tokens
    """
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
