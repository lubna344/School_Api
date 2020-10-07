from rest_framework import serializers
from .models import Students, Rooms, Teachers

########### Students Serializers ###########

class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'title']
    

    def create(self, validated_data):

        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

########### Rooms Serializers ##########

class RoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'numbers_of_rooms', 'numbers_of_students']

    def create(self, validated_data):

        return Rooms.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.numbers_of_rooms = validated_data.get('numbers_of_rooms', instance.numbers_of_rooms)
        instance.numbers_of_students = validated_data.get('numbers_of_students', instance.numbers_of_students)
        instance.save()
        return instance

################## Teachers Serializers ##############

class TeachersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'names_of_teachers', 'numbers_of_teachers']

    def create(self, validated_data):

        return Teachers.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.names_of_teachers = validated_data.get('names_of_teachers', instance.names_of_teachers)
        instance.numbers_of_teachers = validated_data.get('numbers_of_teachers', instance.numbers_of_teachers)
        instance.save()
        return instance




