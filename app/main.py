import json


from aiohttp import web
import aiohttp_jinja2
import jinja2
from pathlib import Path

from app.endpoints.employees import employees_routes
from app.base import Session
from app.models import Employee
from app.pydantic_models.employee import ResponseEmployee as PdResponseEmployee

template_dir = Path(__file__).resolve().parent / "templates"


@aiohttp_jinja2.template("index.html")
async def root(request: web.Request):
    with Session() as session, session.begin():
        all_employees: list[Employee] = session.query(Employee).all()
        empl_list = [PdResponseEmployee.from_orm(empl).dict() for empl in all_employees]
        return {
            "data": json.dumps(empl_list, default=str),
        }


app = web.Application()
app.add_routes([web.get("/", root)])
app.add_routes(employees_routes)

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(template_dir)))
