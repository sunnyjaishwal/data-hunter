from rest_framework import serializers
from ..models.request import Request 
from django.contrib.auth import get_user_model
from .parameter_serializer_mapping import PARAMETER_SERIALIZER_MAP

User = get_user_model()

class EmailToUserPrimaryKeyField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        # If data looks like email, try to get User by email
        if isinstance(data, str) and '@' in data:
            try:
                user = User.objects.get(email=data)
                return user
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with email '{data}' does not exist.")
        # Fallback to default behavior (assumes pk)
        return super().to_internal_value(data)
    
class RequestSerializer(serializers.ModelSerializer):
    client_id = EmailToUserPrimaryKeyField(queryset=User.objects.all())
    class Meta:
        model = Request
        fields = '__all__'
        

    def validate(self, data):
        if data.get("retry_count") != 2:
            raise serializers.ValidationError(
                {"retry_count": "retry_count must always be 2"}
            )
        domain = data.get('domain_name')
        param = data.get('parameter')
        param_serializer_class = PARAMETER_SERIALIZER_MAP.get(domain)
        if not param_serializer_class:
            raise serializers.ValidationError(f"Unsupported domain: {domain}")
        param_serializer = param_serializer_class(data=param)
        param_serializer.is_valid(raise_exception=True)
        return data
