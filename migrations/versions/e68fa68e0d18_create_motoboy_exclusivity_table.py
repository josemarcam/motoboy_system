"""create_motoboy_exclusivity_table

Revision ID: e68fa68e0d18
Revises: 852835ca20f7
Create Date: 2021-12-21 20:03:18.843113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68fa68e0d18'
down_revision = '852835ca20f7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'exclusivities',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('store_id', sa.BigInteger, sa.ForeignKey('stores.id')),
        sa.Column('motoboy_id', sa.BigInteger, sa.ForeignKey('motoboys.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('exclusivities')
