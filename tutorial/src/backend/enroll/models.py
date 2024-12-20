from tortoise import Model, fields


class Student(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "students"


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    students = fields.ManyToManyField("models.Student", related_name="courses")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "courses"
