import typing as t

from . import models as m
from . import serializers as s


class EnrollService:
    @classmethod
    async def list_student(
        cls,
        page: int,
        size: int,
    ) -> t.Dict:
        result = await s.StudentSerializer.list_from_ctx({}, page, size)
        return {
            "status": "ok",
            "message": "student list",
            "data": result.model_dump()["data"],
        }

    @classmethod
    async def list_course(
        cls,
        page: int,
        size: int,
    ) -> t.Dict:
        result = await s.CourseSerializer.list_from_ctx({}, page, size)

        return {
            "status": "ok",
            "message": "course list",
            "data": result.model_dump()["data"],
        }

    @classmethod
    async def bind(
        cls,
        student_id: int,
        course_id: int,
    ) -> t.Dict:
        student = await m.Student.get_or_none(id=student_id)
        course = await m.Course.get_or_none(id=course_id)

        if not student:
            raise ValueError(f"student {student_id} not found")

        if not course:
            raise ValueError(f"course {course_id} not found")

        await student.courses.add(course)

        return {
            "status": "ok",
            "message": "bind success",
            "data": {},
        }
