from datetime import date

from aiohttp.web import (
    HTTPNotFound,
    Request,
    Response,
    RouteTableDef,
    json_response,
)

from app.base import Session
from app.models import Employee as DbEmployee
from app.pydantic_models.employee import (
    NewEmployee as PdNewEmployee,
    ResponseEmployee as PdResponseEmployee,
    UpdateEmployee as PdUpdateEmployee,
)
from app.utils.error_handlers import raise_400_for_validation_error

employees_routes = RouteTableDef()


@employees_routes.patch("/employees/{employee_id:\d+}")
async def update_employee(request: Request) -> Response:
    with Session() as session, session.begin():
        employee: DbEmployee = session.query(DbEmployee).get(
            request.match_info["employee_id"]
        )
        if not employee:
            raise HTTPNotFound()

        data = await request.json()
        print(f"received: {data}")
        with raise_400_for_validation_error():
            pd_empl = PdUpdateEmployee(**data)

        employee.update(**pd_empl.dict())
        session.add(employee)

        pd_empl_response = PdResponseEmployee.from_orm(employee).json_ready_dict()
        return json_response(pd_empl_response)


@employees_routes.post("/employees")
async def create_employees(request: Request) -> Response:
    with Session() as session, session.begin():
        employees_data = await request.json()
        print(f"request data: {employees_data}")
        with raise_400_for_validation_error():
            pd_employees = [PdNewEmployee(**empl_data) for empl_data in employees_data]

        employees = [DbEmployee(**pd_empl.dict()) for pd_empl in pd_employees]
        session.add_all(employees)
        session.flush()
        session.expire_all()
        return json_response(
            [PdResponseEmployee.from_orm(empl).json_ready_dict() for empl in employees]
        )
