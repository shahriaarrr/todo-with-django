from rest_framework import serializers

from account.models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first name', 'last name', 'email', 'age', 'gender')

    def validate(self, data):
        if data.get('first name') == data.get('last name'):
            raise serializers.ValidationError('Your first and last name should not be the same')

        return data

    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Your password should not be less than 5 characters')

        return value

    def validate_age(self, value):
        if value <= 0:
            error = 'Your age must be a positive number and greater than zero'
            raise serializers.ValidationError(error)

        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
