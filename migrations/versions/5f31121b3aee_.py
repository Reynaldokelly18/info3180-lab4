"""empty message

Revision ID: 5f31121b3aee
Revises: 
Create Date: 2024-03-06 23:02:07.825362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f31121b3aee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
