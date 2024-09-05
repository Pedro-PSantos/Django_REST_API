from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta: # Meta class is used to specify the model and fields
        model = Drink
        fields = ['id','name', 'description']