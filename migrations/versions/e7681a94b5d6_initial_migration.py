"""initial migration

Revision ID: e7681a94b5d6
Revises: 
Create Date: 2026-05-05 16:36:38.715687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7681a94b5d6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'trip',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('destination', sa.String(), nullable=False),
        sa.Column('days', sa.Integer(), nullable=False),
        sa.Column('budget', sa.Integer(), nullable=False),
        sa.Column('trip_style', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'itinerary',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('trip_id', sa.Integer(), nullable=False),
        sa.Column('days', sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
def downgrade() -> None:
    op.drop_table('itinerary')
    op.drop_table('trip')
    op.drop_table('user')
