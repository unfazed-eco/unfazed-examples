from unfazed.serializer import Serializer

from . import models as m


class StudentSerializer(Serializer):
    class Meta:
        model = m.Student


class CourseSerializer(Serializer):
    class Meta:
        model = m.Course
