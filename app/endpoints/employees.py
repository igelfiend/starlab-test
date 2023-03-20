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


@employees_routes.get("/employees/init")
async def init(request: Request) -> Response:
    chief_data = {
        "first_name": "John",
        "last_name": "Doe",
        "position": "SEO",
        "employment_date": date(1992, 10, 20),
        "salary": 1000,
    }
    chief_sub1_data = {
        "first_name": "Jane",
        "last_name": "Smith",
        "position": "Tech lead",
        "employment_date": date(1982, 9, 1),
        "salary": 2000,
    }
    chief_sub2_data = {
        "first_name": "Michael",
        "last_name": "McNeel",
        "position": "Team lead",
        "employment_date": date(2000, 1, 31),
        "salary": 500,
    }
    sub1_sub11_data = {
        "first_name": "Homer",
        "last_name": "Simpson",
        "position": "JavaScript developer",
        "employment_date": date(1976, 6, 25),
        "salary": 2500,
    }
    with Session() as session, session.begin():
        chief = DbEmployee(chief_id=None, **chief_data)
        chief_sub1 = DbEmployee(chief=chief, **chief_sub1_data)
        chief_sub2 = DbEmployee(chief=chief, **chief_sub2_data)
        sub1_sub11 = DbEmployee(chief=chief_sub1, **sub1_sub11_data)

        session.add_all([chief, chief_sub1, chief_sub2, sub1_sub11])
    return json_response({"success": True})


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
