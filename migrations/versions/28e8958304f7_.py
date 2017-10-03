"""empty message

Revision ID: 28e8958304f7
Revises: 015402e3399b
Create Date: 2017-10-03 14:41:54.933472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e8958304f7'
down_revision = '015402e3399b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('code', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'code')
    # ### end Alembic commands ###