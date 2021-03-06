"""change the topic model

Revision ID: 28d9974af759
Revises: 
Create Date: 2018-04-26 00:20:46.714661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28d9974af759'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('pic_url', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topics', 'pic_url')
    # ### end Alembic commands ###
