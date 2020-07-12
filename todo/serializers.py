from rest_framework import serializers
from .models import Task, Category
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['url', 'id', 'title', 'category', 'user', 'date_created']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="user-detail",
                                                lookup_field="username")
    task = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'task']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['url', 'id', 'title', 'color',]

