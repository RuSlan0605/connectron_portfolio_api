from rest_framework import serializers
from app.models import Project, Staff, Field

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            '__all__'
        )
    
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            '__all__'
        )
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['field'] = instance.field.field_name
        return response

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = (
            '__all__'
        )