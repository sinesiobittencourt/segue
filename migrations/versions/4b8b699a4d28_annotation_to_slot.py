"""empty message

Revision ID: 4b8b699a4d28
Revises: 3c8d450cb51f
Create Date: 2015-06-24 16:22:10.892316

"""

# revision identifiers, used by Alembic.
revision = '4b8b699a4d28'
down_revision = '3c8d450cb51f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slot', sa.Column('annotation', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('slot', 'annotation')
    ### end Alembic commands ###