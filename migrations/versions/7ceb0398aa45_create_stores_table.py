"""create_stores_table

Revision ID: 7ceb0398aa45
Revises: 
Create Date: 2021-12-20 14:55:45.469173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ceb0398aa45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('motoboy_percent', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('stores')