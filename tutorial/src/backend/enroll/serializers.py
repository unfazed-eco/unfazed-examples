from unfazed.serializer import Serializer

from . import models as m


class StudentSerializer(Serializer):
    class Meta:
        model = m.Student
        exclude = ["courses"]


class CourseSerializer(Serializer):
    class Meta:
        model = m.Course
        exclude = ["students"]
