import typing as t

from pydantic import BaseModel

# ------ request schemas ------


class StudentList(BaseModel):
    page: int = 1
    size: int = 10
    search: str = ""


class CourseCreate(BaseModel):
    name: str


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    courses: t.List[CourseCreate] | None = None


# ------ response schemas ------


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    created_at: str
    updated_at: str


class StudentListResp(BaseModel):
    count: int
    data: t.List[Student]


class Course(BaseModel):
    id: int
    name: str
    created_at: str
    updated_at: str
