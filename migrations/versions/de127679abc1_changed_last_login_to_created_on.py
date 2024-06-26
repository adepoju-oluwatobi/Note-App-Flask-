"""changed last login to created on

Revision ID: de127679abc1
Revises: 4ff0bdc6b082
Create Date: 2024-04-21 00:59:09.078366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'de127679abc1'
down_revision = '4ff0bdc6b082'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_on', sa.DateTime(), nullable=True))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=225),
               existing_nullable=False)
        batch_op.drop_column('last_login')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.alter_column('password',
               existing_type=sa.String(length=225),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('created_on')

    # ### end Alembic commands ###
