"""expiration in days was added to medical items

Revision ID: e550465f6d03
Revises: ee7527eaed8e
Create Date: 2022-01-06 23:59:44.225747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e550465f6d03'
down_revision = 'ee7527eaed8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_items', sa.Column('expires_in_days', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('medical_items', 'expires_in_days')
    # ### end Alembic commands ###
