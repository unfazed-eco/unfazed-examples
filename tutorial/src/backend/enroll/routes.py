import typing as t

from unfazed.route import Route, path

from .endpoints import bind, hello, list_course, list_student

patterns: t.List[Route] = [
    path("/hello", endpoint=hello),
    path("/student-list", endpoint=list_student),
    path("/course-list", endpoint=list_course),
    path("/bind", endpoint=bind, methods=["POST"]),
]
