"""medical crud updated v3

Revision ID: 9f63f4afe62b
Revises: 74fcb8d6afe9
Create Date: 2021-12-13 19:29:31.198556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9f63f4afe62b"
down_revision = "74fcb8d6afe9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("patients", "birth_date", existing_type=sa.DATE(), nullable=True)
    op.alter_column(
        "patients", "medical_insurance", existing_type=sa.VARCHAR(), nullable=True
    )
    op.drop_constraint(
        "patients_first_name_middle_name_last_name_birth_date_medica_key",
        "patients",
        type_="unique",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "patients_first_name_middle_name_last_name_birth_date_medica_key",
        "patients",
        ["first_name", "middle_name", "last_name", "birth_date", "medical_insurance"],
    )
    op.alter_column(
        "patients", "medical_insurance", existing_type=sa.VARCHAR(), nullable=False
    )
    op.alter_column("patients", "birth_date", existing_type=sa.DATE(), nullable=False)
    # ### end Alembic commands ###
