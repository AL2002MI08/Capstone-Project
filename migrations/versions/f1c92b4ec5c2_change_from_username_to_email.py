"""change from username to email

Revision ID: f1c92b4ec5c2
Revises: e7681a94b5d6
Create Date: 2026-06-12 16:23:15.011345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'f1c92b4ec5c2'
down_revision: Union[str, Sequence[str], None] = 'e7681a94b5d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Step 1: add email as nullable so existing rows don't fail NOT NULL
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))

    # Step 2: copy username -> email for existing rows
    op.execute("UPDATE user SET email = username")

    # Step 3: make email NOT NULL and drop the old username column
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email', nullable=False)
        batch_op.drop_column('username')


def downgrade() -> None:
    """Downgrade schema."""
    # Step 1: add username as nullable first
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=True))

    # Step 2: copy email -> username
    op.execute("UPDATE user SET username = email")

    # Step 3: make username NOT NULL and drop email
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username', nullable=False)
        batch_op.drop_column('email')
