from rest_framework import serializers
from .models import *

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = '__all__'

class RootSerializer(serializers.ModelSerializer):

    class Meta:
        model = Root
        fields = '__all__'
