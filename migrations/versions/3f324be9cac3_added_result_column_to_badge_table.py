"""added result column to badge table

Revision ID: 3f324be9cac3
Revises: 2cd344823c39
Create Date: 2015-07-04 00:49:49.438803

"""

# revision identifiers, used by Alembic.
revision = '3f324be9cac3'
down_revision = '2cd344823c39'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('badge', sa.Column('result', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('badge', 'result')
    ### end Alembic commands ###
