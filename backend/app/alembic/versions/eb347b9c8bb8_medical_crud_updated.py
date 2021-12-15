"""medical crud updated

Revision ID: eb347b9c8bb8
Revises: 6a7ed0eb2c05
Create Date: 2021-12-13 17:40:36.633720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb347b9c8bb8'
down_revision = '6a7ed0eb2c05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('without_documents', sa.Boolean(), nullable=True))
    op.alter_column('patients', 'medical_insurance',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'medical_insurance',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('patients', 'without_documents')
    # ### end Alembic commands ###