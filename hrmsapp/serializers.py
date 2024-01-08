from .models import Employee, Attendence
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for the Employee model."""
    class Meta:
        model = Employee
        fields = '__all__'


class AttendenceSerializer(serializers.ModelSerializer):
    """Serializer for the Attendance model."""
    employee_name = serializers.CharField(source='employee.name', read_only=True)

    class Meta:
        model = Attendence
        fields = ['date', 'department', 'employee_name', 'attendence', 'time_in', 'time_out']

