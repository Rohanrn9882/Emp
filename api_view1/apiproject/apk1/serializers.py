from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    eid = serializers.IntegerField()
    ename = serializers.CharField(max_length = 30)
    city = serializers.CharField(max_length = 30)
    sal = serializers.FloatField()
    

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.eid = validated_data.get('eid', instance.eid)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.city = validated_data.get('city', instance.city)
        instance.sal = validated_data.get('sal', instance.sal)

        instance.save()
        return instance
