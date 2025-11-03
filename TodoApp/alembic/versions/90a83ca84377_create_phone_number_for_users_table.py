"""create phone number for users table

Revision ID: 90a83ca84377
Revises: 
Create Date: 2025-10-29 14:11:38.484318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90a83ca84377'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(100), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
