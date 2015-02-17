"""adding tracks and linkint it in proposal

Revision ID: 16b1659c8e
Revises: 48a39cec3049
Create Date: 2015-02-17 00:45:10.883116

"""

# revision identifiers, used by Alembic.
revision = '16b1659c8e'
down_revision = '48a39cec3049'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_pt', sa.Text(), nullable=True),
    sa.Column('name_en', sa.Text(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'proposal', sa.Column('track_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'proposal', 'track', ['track_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'proposal', type_='foreignkey')
    op.drop_column(u'proposal', 'track_id')
    op.drop_table('track')
    ### end Alembic commands ###
