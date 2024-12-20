import typing as t

from unfazed.route import Route, path

from . import endpoints as e

patterns: t.List[Route] = [
    path("/student-list", endpoint=e.list_student, methods=["GET"]),
    path("/student-create", endpoint=e.create_student, methods=["POST"]),
]
