import typing as t

from pydantic import BaseModel

from .serializers import CourseSerializer, StudentSerializer


class BaseResponse(BaseModel):
    status: str
    message: str


class StudentListResponse(BaseResponse):
    data: t.List[StudentSerializer]


class CourseListResponse(BaseResponse):
    data: t.List[CourseSerializer]


class BindRequest(BaseModel):
    student_id: int
    course_id: int


class BindResponse(BaseResponse):
    data: t.Dict = {}
