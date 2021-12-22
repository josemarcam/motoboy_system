"""create_motoboys_table

Revision ID: d5add54ee069
Revises: fd2a763b5ec9
Create Date: 2021-12-20 15:04:12.800903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5add54ee069'
down_revision = 'fd2a763b5ec9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'motoboys',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('fixed_rate', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('motoboys')
