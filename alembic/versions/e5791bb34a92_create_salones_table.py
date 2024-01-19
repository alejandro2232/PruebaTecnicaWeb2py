"""create salones table

Revision ID: e5791bb34a92
Revises: 18313d22e921
Create Date: 2024-01-17 03:56:09.717983

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column

# revision identifiers, used by Alembic.
revision: str = 'e5791bb34a92'
down_revision: Union[str, None] = '18313d22e921'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'salones',   
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('nombre',VARCHAR(50)),
        Column('edificio',VARCHAR(50)),
    )


def downgrade() -> None:
    pass
