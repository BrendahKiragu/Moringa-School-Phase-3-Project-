from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e26ae8c801b7'
down_revision: Union[str, None] = 'f7eb08b232d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create a temporary table with the new schema
    op.create_table(
        'users_temp',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.VARCHAR(), nullable=False),
        sa.Column('password', sa.VARCHAR(), nullable=False),
        # Include other columns here if any
    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO users_temp (id, username, password) SELECT id, username, password FROM users')

    # Drop the old table
    op.drop_table('users')

    # Rename the new table to the original table name
    op.rename_table('users_temp', 'users')

def downgrade() -> None:
    # Reverse the above steps
    op.create_table(
        'users_temp',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.VARCHAR(), nullable=True),
        sa.Column('password', sa.VARCHAR(), nullable=True),
        # Include other columns here if any
    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO users_temp (id, username, password) SELECT id, username, password FROM users')

    # Drop the old table
    op.drop_table('users')

    # Rename the new table to the original table name
    op.rename_table('users_temp', 'users')
