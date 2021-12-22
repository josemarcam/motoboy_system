"""add_motoboy_id_in_orders_table

Revision ID: 852835ca20f7
Revises: d5add54ee069
Create Date: 2021-12-20 15:19:25.531113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '852835ca20f7'
down_revision = 'd5add54ee069'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders',
        sa.Column('motoboy_id', sa.BigInteger, sa.ForeignKey("motoboys.id"), nullable=True)
    )


def downgrade():
    pass
