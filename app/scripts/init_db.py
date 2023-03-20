from datetime import date

from app.base import Session
from app.models import Employee

if __name__ == "__main__":
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
        chief = Employee(chief_id=None, **chief_data)
        chief_sub1 = Employee(chief=chief, **chief_sub1_data)
        chief_sub2 = Employee(chief=chief, **chief_sub2_data)
        sub1_sub11 = Employee(chief=chief_sub1, **sub1_sub11_data)

        session.add_all([chief, chief_sub1, chief_sub2, sub1_sub11])
