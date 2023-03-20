from sqlalchemy.exc import ArgumentError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase


class Model(RepresentableBase):
    def _get_column_names(self):
        return {column.name for column in self.__table__.columns}

    def update(self, **kwargs):
        model_columns = self._get_column_names()
        update_columns = set(kwargs)
        if not update_columns.issubset(model_columns):
            raise ArgumentError(
                f"Unsupported fields received: {update_columns - model_columns}. "
            )
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        column_names = self._get_column_names()
        return {column_name: getattr(self, column_name) for column_name in column_names}


Model = declarative_base(name="Model", cls=Model)


metadata = Model.metadata
