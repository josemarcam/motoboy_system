"""create_orders_table

Revision ID: fd2a763b5ec9
Revises: 7ceb0398aa45
Create Date: 2021-12-20 14:59:03.676286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd2a763b5ec9'
down_revision = '7ceb0398aa45'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('store_id', sa.BigInteger, sa.ForeignKey('stores.id')),
        sa.Column('total_value', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('orders')
