from rest_framework import serializers
from .models import MasterTasks

class MasterTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=MasterTasks
        fields="__all__"