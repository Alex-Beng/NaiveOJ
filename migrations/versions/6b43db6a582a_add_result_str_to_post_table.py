"""add result:str to Post table

Revision ID: 6b43db6a582a
Revises: cbfbea560861
Create Date: 2020-11-04 19:19:16.380352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b43db6a582a'
down_revision = 'cbfbea560861'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('result', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'result')
    # ### end Alembic commands ###
