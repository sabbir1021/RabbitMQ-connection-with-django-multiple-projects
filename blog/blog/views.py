from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category,Blog,Comments
from .serializers import CategorySerializer,BlogSerializer,CommentsSerializer
from .producer import publish
# Create your views here.

class CategoryListCreate(APIView):
    def get(self, request, format=None):
        payment_method = Category.objects.all()
        serializer = CategorySerializer(payment_method, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogListCreate(APIView):
    def get(self, request, format=None):
        payment_method = Blog.objects.all()
        serializer = BlogSerializer(payment_method, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CommentListCreate(APIView):
    def get(self, request, format=None):
        payment_method = Comments.objects.all()
        serializer = CommentsSerializer(payment_method, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            publish('comment_created', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)