"""empty message

Revision ID: d7e98cb6f7f9
Revises: 
Create Date: 2018-10-08 20:44:22.483176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7e98cb6f7f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=200), nullable=False),
    sa.Column('country_code', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_key', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('act_temp', sa.Float(), nullable=True),
    sa.Column('min_temp', sa.Float(), nullable=True),
    sa.Column('max_temp', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('icon', sa.String(length=3), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('pressure', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_data')
    op.drop_table('weather_config')
    op.drop_table('cities')
    # ### end Alembic commands ###