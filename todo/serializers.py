from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'is_complete', 'created_at', 'update_at', 'completion_at']
        read_only_fields = ['user']
        # fields = "__all__"
        # extra_kwargs = {
        #     "user": {
        #         # "requited":False,
        #         "required":False,

        #     },
            
        # }