from sqlalchemy import Column, Integer, String, Date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.base import Model


class Employee(Model):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    position = Column(String(200))
    employment_date = Column(Date)
    salary = Column(Integer)
    chief_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=True)
    chief: Mapped["Employee"] = relationship(
        back_populates="subordinates", remote_side=[id]
    )

    subordinates: Mapped[list["Employee"]] = relationship(
        back_populates="chief",
    )

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "employment_date": str(self.employment_date),
            "salary": self.salary,
            "chief_id": self.chief_id,
        }
