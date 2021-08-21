from rest_framework import serializers

from todo_app.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'Priority', 'task_text', 'date')

    def validate(self, data):
        if data.get('title') == data.get('task_text'):
            raise serializers.ValidationError('The task title and its description can be the same')

    def validate_title(self, value):
        if len(value) > 10 or len(value) < 4:
            error='The task title should be a maximum of 10 characters and a minimum of 4 characters'
            raise serializers.ValidationError(error)

        return value