import typing as t

from unfazed.http import HttpRequest, JsonResponse
from unfazed.route import params as p

from .schema import StudentCreate, StudentList, StudentListResp
from .services import StudentService


async def list_student(
    request: HttpRequest, ctx: t.Annotated[StudentList, p.Query()]
) -> t.Annotated[JsonResponse, StudentListResp]:
    cond: t.Dict[str, t.Any] = {}
    if ctx.search:
        cond["first_name__icontains"] = ctx.search
    ret = await StudentService.list_students(cond, ctx.page, ctx.size)

    return JsonResponse(ret)


async def create_student(
    request: HttpRequest, ctx: t.Annotated[StudentCreate, p.Json()]
) -> t.Annotated[JsonResponse, StudentListResp]:
    ret = await StudentService.create_student(ctx)

    return JsonResponse(ret)


async def list_course(
    request: HttpRequest, ctx: t.Annotated[StudentList, p.Query()]
) -> t.Annotated[JsonResponse, StudentListResp]:
    cond: t.Dict[str, t.Any] = {}
    if ctx.search:
        cond["name__icontains"] = ctx.search
    ret = await StudentService.list_courses(cond, ctx.page, ctx.size)

    return JsonResponse(ret)
