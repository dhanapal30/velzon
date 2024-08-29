from rest_framework import serializers
from velzonapi.models import State,Users,City
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Must include both username and password.")

        data['user'] = user
        return data
class Login1Serializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate1(self, data):
        name = data.get("name")
        password = data.get("password")

        if name and password:
            user = authenticate(username=name, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Must include both username and password.")

        data['Users'] = user
        return data


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'  # or specify fields explicitly
        
class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    class Meta:
        model = City
        fields = '__all__'  # or specify fields explicitly

        
        
        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # or specify fields explicitly

