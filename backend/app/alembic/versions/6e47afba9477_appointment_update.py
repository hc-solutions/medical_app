"""appointment update

Revision ID: 6e47afba9477
Revises: cbe3fc70a369
Create Date: 2022-01-06 22:45:38.063224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e47afba9477'
down_revision = 'cbe3fc70a369'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient_appointments', sa.Column('scheduled_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient_appointments', 'scheduled_at')
    # ### end Alembic commands ###
