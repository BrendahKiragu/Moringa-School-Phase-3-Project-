"""Created Job_field model

Revision ID: 3b25c7ff29f2
Revises: bcbd3f41dcd2
Create Date: 2024-09-17 13:16:13.813501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b25c7ff29f2'
down_revision: Union[str, None] = 'bcbd3f41dcd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_fields',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_fields')
    # ### end Alembic commands ###