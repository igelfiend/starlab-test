from datetime import date

from .base import NoExtraFieldsModel


class UpdateEmployee(NoExtraFieldsModel):
    first_name: str
    last_name: str
    position: str
    employment_date: date
    salary: int

    def json_ready_dict(self, *args, **kwargs):
        d = self.dict(*args, **kwargs)
        d["employment_date"] = str(d["employment_date"])
        return d


class NewEmployee(UpdateEmployee):
    chief_id: int | None


class ResponseEmployee(NewEmployee):
    class Config:
        orm_mode = True

    id: int
