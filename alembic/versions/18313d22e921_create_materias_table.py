"""create materias table

Revision ID: 18313d22e921
Revises: c0bbe0ab68ff
Create Date: 2024-01-17 03:55:57.078511

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column

# revision identifiers, used by Alembic.
revision: str = '18313d22e921'
down_revision: Union[str, None] = 'c0bbe0ab68ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'materias',   
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('nombre',VARCHAR(50)),
        Column('area',VARCHAR(50)),
    )


def downgrade() -> None:
    pass
