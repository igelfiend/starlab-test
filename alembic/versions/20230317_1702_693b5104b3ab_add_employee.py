"""add employee

Revision ID: 693b5104b3ab
Revises: 
Create Date: 2023-03-17 17:02:01.245713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693b5104b3ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('employment_date', sa.Date(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('chief_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chief_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###