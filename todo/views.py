from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from todo.models import Todo
from todo.serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
# @api_view(['GET','POST'])
# def todoAPI(request):
#     if request.method == 'GET':
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)    
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TodoList(APIView):
    def get(self, request, format=None):
        # if pk:
        #     obj = Todo.objects.get(pk=pk)
        #     return Response(TodoSerializer(obj).data)

        # queryset = Todo.objects.filter(user=request.user)
        # return Response(TodoSerializer(queryset, many=True).data)

        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request, format=None):
            serializer = TodoSerializer(data = request.data)
            # raise_exception=True
            if serializer.is_valid():
                # user=request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)    
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT', 'DELETE'])    
# def todoDetailAPI(request, todo_id):
#     if request.method == 'GET':
#         todo = get_object_or_404(Todo, id=todo_id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         todo = get_object_or_404(Todo, id=todo_id)
#         serializer = TodoSerializer(todo, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         todo = get_object_or_404(Todo, id=todo_id)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

class TodoDetail(APIView):
    def get(self, request, todo_id, format=None):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, todo_id, format=None):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, format=None):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)