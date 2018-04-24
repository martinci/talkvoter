"""add user field to vote

Revision ID: 2f3daec0d25f
Revises: 42410bd32a0f
Create Date: 2018-04-15 21:27:35.657955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f3daec0d25f'
down_revision = '42410bd32a0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vote', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'vote', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vote', type_='foreignkey')
    op.drop_column('vote', 'user_id')
    # ### end Alembic commands ###