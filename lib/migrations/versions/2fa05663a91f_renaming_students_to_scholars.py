"""Renaming students to scholars

Revision ID: 2fa05663a91f
Revises: 791279dd0760
Create Date: 2023-03-08 09:55:06.080709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa05663a91f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='nickname')

def downgrade() -> None:
    op.alter_column('students', 'nickname', new_column_name='name')

# commands to run after alembic upgrade head(aka revision#) to check for update
# sqlite3 migrations_test.db
# .schema table_name