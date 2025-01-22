import typing as t

import pytest
from unfazed.core import Unfazed
from unfazed.test import Requestfactory

from enroll import models as m
from enroll import services as svc


@pytest.fixture(autouse=True)
async def setup_enroll() -> t.AsyncGenerator[None, None]:
    await m.Student.all().delete()
    await m.Course.all().delete()

    # create more than 10 students
    for student in [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Helen",
        "Ivy",
        "Jack",
        "Kevin",
    ]:
        await m.Student.create(name=student, age=20)

    for course in ["Math", "Physics", "Chemistry"]:
        await m.Course.create(name=course, description=f"description of {course}")

    yield

    await m.Student.all().delete()
    await m.Course.all().delete()


async def test_enroll_services() -> None:
    # test list_student
    ret = await svc.EnrollService.list_student(1, 10)
    assert len(ret["data"]) == 10

    ret = await svc.EnrollService.list_student(2, 10)
    assert len(ret["data"]) == 1

    # test list_course
    ret = await svc.EnrollService.list_course(1, 10)

    assert len(ret["data"]) == 3

    ret = await svc.EnrollService.list_course(2, 10)

    assert len(ret["data"]) == 0

    # test bind
    student = await m.Student.get(name="Alice")
    course = await m.Course.get(name="Math")
    ret = await svc.EnrollService.bind(student.id, course.id)
    assert ret["status"] == "ok"


async def test_enroll_endpoints(unfazed: Unfazed) -> None:
    async with Requestfactory(unfazed) as rf:
        # test hello
        resp = await rf.get("/enroll/hello")
        assert resp.status_code == 200

        # test list_student
        resp = await rf.get("/enroll/student-list")
        assert resp.status_code == 200

        # test list_course
        resp = await rf.get("/enroll/course-list")
        assert resp.status_code == 200

        student = await m.Student.get(name="Bob")
        course = await m.Course.get(name="Math")
        resp = await rf.post(
            "/enroll/bind", json={"student_id": student.id, "course_id": course.id}
        )
        assert resp.status_code == 200
