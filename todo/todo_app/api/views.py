from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializers


class addTaskView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        addTask = TaskSerializers(data=request.data)
        if addTask.is_valid():
            addTask.save()
            return Response({'message' : 'Your Task successfully add'})