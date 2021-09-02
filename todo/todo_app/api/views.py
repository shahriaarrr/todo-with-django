from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializers, DeleteSerializers
from todo_app.models import Task


class addTaskView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        addTask = TaskSerializers(data=request.data)
        if addTask.is_valid():
            data = TaskSerializers.validated_data
            Task.objects.create(**data)
            
            return Response({'message' : 'Your Task successfully add'})

class DeleteTaskAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        delete_task = DeleteSerializers(data=request.data)
        if delete_task.is_valid():
            data = DeleteSerializers.validated_data
            Task.objects.delete(**data)

            return Response({'message' : 'Your Task successfully deleted'})