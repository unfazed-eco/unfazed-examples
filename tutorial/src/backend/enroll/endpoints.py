import typing as t

from unfazed.http import HttpRequest, JsonResponse, PlainTextResponse
from unfazed.route import params as p

from . import schema as s
from . import services as svc


async def hello(request: HttpRequest) -> PlainTextResponse:
    return PlainTextResponse("Hello, world!")


async def list_student(
    request: HttpRequest,
    page: t.Annotated[int, p.Query(default=1)],
    size: t.Annotated[int, p.Query(default=10)],
) -> t.Annotated[JsonResponse, p.ResponseSpec(model=s.StudentListResponse)]:
    ret = await svc.EnrollService.list_student(page, size)
    return JsonResponse(ret)


async def list_course(
    request: HttpRequest,
    page: t.Annotated[int, p.Query(default=1)],
    size: t.Annotated[int, p.Query(default=10)],
) -> t.Annotated[JsonResponse, p.ResponseSpec(model=s.CourseListResponse)]:
    ret = await svc.EnrollService.list_course(page, size)
    return JsonResponse(ret)


async def bind(
    request: HttpRequest,
    ctx: t.Annotated[s.BindRequest, p.Json()],
) -> t.Annotated[JsonResponse, p.ResponseSpec(model=s.BindResponse)]:
    ret = await svc.EnrollService.bind(ctx.student_id, ctx.course_id)
    return JsonResponse(ret)
