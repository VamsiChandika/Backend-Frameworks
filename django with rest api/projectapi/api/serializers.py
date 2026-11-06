from rest_framework import serializers
from api.models import MyStudent
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        """ In this we will define the model name
        & feilds of the model"""
        model = MyStudent
        fields = "__all__"