from rest_framework import serializers

from todo_app.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'Priority', 'task_text', 'date')