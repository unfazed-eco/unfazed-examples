import logging
import typing as t

from .schema import StudentCreate, StudentListResp
from .serializers import StudentSerializer

_Logger = logging.getLogger("common")


class StudentService:
    @classmethod
    async def list_students(cls, cond: t.Dict, page: int, size: int) -> StudentListResp:
        ret = await StudentSerializer.list_from_ctx(cond, page, size)
        _Logger.info(f"ret: {ret}")

        return StudentListResp(count=ret.count, data=ret.data)

    @classmethod
    async def create_student(cls, ctx: StudentCreate) -> StudentSerializer:
        ret = await StudentSerializer.create_from_ctx(ctx)

        return ret
