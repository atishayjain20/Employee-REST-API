from rest_framework import serializers
from .models import empoylee
class empoyleeSerializer(serializers.Serializer):
    firstname=serializers.CharField(max_length=20)
    lastname=serializers.CharField(max_length=20)
    emp_id=serializers.IntegerField()

    def create(self,validated_data):
        return empoylee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.firstname=validated_data.get('firstname',instance.firstname)
        instance.lastname=validated_data.get('lastname',instance.lastname)
        instance.emp_id=validated_data.get('emp_id',instance.emp_id)
        instance.save()
        return instance
    