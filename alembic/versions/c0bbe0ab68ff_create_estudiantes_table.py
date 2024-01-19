"""create estudiantes table

Revision ID: c0bbe0ab68ff
Revises: 
Create Date: 2024-01-17 03:55:46.402004

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column

# revision identifiers, used by Alembic.
revision: str = 'c0bbe0ab68ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'estudiantes',   
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('nombre',VARCHAR(50)),
        Column('apellido',VARCHAR(50)),
        Column('estado',VARCHAR(50))
    )


def downgrade() -> None:
    pass
