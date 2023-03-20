from datetime import date

from .base import NoExtraFieldsModel


class UpdateEmployee(NoExtraFieldsModel):
    first_name: str
    last_name: str
    position: str
    employment_date: date
    salary: int


class NewEmployee(UpdateEmployee):
    chief_id: int | None


class ResponseEmployee(NewEmployee):
    class Config:
        orm_mode = True

    id: int
