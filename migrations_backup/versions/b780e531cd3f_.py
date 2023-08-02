"""empty message

Revision ID: b780e531cd3f
Revises: 1bc188b0a759
Create Date: 2023-07-14 03:25:11.988202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b780e531cd3f'
down_revision = '1bc188b0a759'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('engine', sa.String(100), nullable=True))
        batch_op.add_column(sa.Column('transmission', sa.String(100), nullable=True))
        batch_op.add_column(sa.Column('trim', sa.String(100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.drop_column('trim')
        batch_op.drop_column('transmission')
        batch_op.drop_column('engine')

    # ### end Alembic commands ###