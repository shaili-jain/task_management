from rest_framework import serializers
from EmployeeApp.models import User,Task,Assign

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_id',
                    'uFName',
                    'uLName',
                    'uRole',
                    'uEmail',
                    'uAvailableHr',
                    'uPassword')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('t_id',
                    'tName',
                    'tDescp',
                    'tPriority',
                    'tExpHr',
                    'u_id')


class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields=('id',
                't_status',
                'assignDate',
                'assignerName',
                'assigneeId',
                't_id')