from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


class CommentListCreate(APIView):
    def get(self, request, format=None):
        payment_method = Comment.objects.all()
        serializer = CommentSerializer(payment_method, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)