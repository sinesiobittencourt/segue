"""created products table

Revision ID: 441179703573
Revises: 16b1659c8e
Create Date: 2015-03-09 04:10:11.160589

"""

# revision identifiers, used by Alembic.
revision = '441179703573'
down_revision = '16b1659c8e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('kind', sa.Enum('ticket', 'swag', name='product_kinds'), nullable=True),
            sa.Column('category', sa.Text(), nullable=True),
            sa.Column('public', sa.Boolean(), nullable=True),
            sa.Column('price', sa.Numeric(), nullable=True),
            sa.Column('sold_until', sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    ENUM(name="product_kinds").drop(op.get_bind(), checkfirst=False)
    ### end Alembic commands ###
