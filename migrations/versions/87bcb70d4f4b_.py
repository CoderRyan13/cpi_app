"""empty message

Revision ID: 87bcb70d4f4b
Revises: 
Create Date: 2024-05-22 15:32:28.631915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87bcb70d4f4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collector_area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('areaid', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collector_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quality_assurance_assignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('hq_id', sa.Integer(), nullable=True),
    sa.Column('time_period', sa.Date(), nullable=False),
    sa.Column('collector_price', sa.Float(), nullable=False),
    sa.Column('hq_price', sa.Float(), nullable=False),
    sa.Column('collector_comment', sa.String(length=255), nullable=True),
    sa.Column('hq_comment', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('working_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('time_period', sa.Date(), nullable=False),
    sa.Column('time_period_created', sa.Date(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('generic_outlier', sa.Float(), nullable=True),
    sa.Column('z_score_outlier', sa.Float(), nullable=True),
    sa.Column('inter_quartile_outlier', sa.Float(), nullable=True),
    sa.Column('outlier_status', sa.Enum('pending', 'approved', 'rejected'), nullable=True),
    sa.Column('flag', sa.Enum('IMPUTED', 'SUBSTITUTION', 'BACK_HISTORY', 'MANUAL_EDIT'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('assignment_id')
    )
    op.create_table('collector_outlet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpi_outlet_id', sa.Integer(), nullable=True),
    sa.Column('est_name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('long', sa.Float(), nullable=False),
    sa.Column('note', sa.String(length=1000), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('operating_hours', sa.String(length=255), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['collector_area.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpi_outlet_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('collector', 'HQ'), nullable=False),
    sa.Column('status', sa.Enum('activated', 'deactivated'), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['collector_area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collector_variety',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpi_variety_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('code', sa.String(length=80), nullable=False),
    sa.Column('approved_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('date_approved', sa.DateTime(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['approved_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['collector_product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpi_variety_id')
    )
    op.create_table('assignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('outlet_product_variety_id', sa.Integer(), nullable=True),
    sa.Column('variety_id', sa.Integer(), nullable=False),
    sa.Column('outlet_id', sa.Integer(), nullable=False),
    sa.Column('collector_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('is_monthly', sa.Integer(), nullable=False),
    sa.Column('is_headquarter', sa.Integer(), nullable=False),
    sa.Column('from_assignment_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('active', 'inactive'), nullable=False),
    sa.Column('create_date_time', sa.DateTime(), nullable=False),
    sa.Column('update_date_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['collector_area.id'], ),
    sa.ForeignKeyConstraint(['collector_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['outlet_id'], ['collector_outlet.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['assignment.id'], ),
    sa.ForeignKeyConstraint(['variety_id'], ['collector_variety.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('time_period', sa.Date(), nullable=False),
    sa.Column('collected_at', sa.DateTime(), nullable=True),
    sa.Column('collector_id', sa.Integer(), nullable=False),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('rejected', 'approved'), nullable=True),
    sa.Column('flag', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignment.id'], ),
    sa.ForeignKeyConstraint(['collector_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requested_substitution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('time_period', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('pending', 'approved', 'rejected'), nullable=False),
    sa.Column('requested_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignment.id'], ),
    sa.ForeignKeyConstraint(['requested_at'], ['collector_outlet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('assignment_id')
    )
    op.create_table('substitution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('variety_id', sa.Integer(), nullable=False),
    sa.Column('outlet_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignment.id'], ),
    sa.ForeignKeyConstraint(['outlet_id'], ['collector_outlet.id'], ),
    sa.ForeignKeyConstraint(['variety_id'], ['collector_variety.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('assignment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('substitution')
    op.drop_table('requested_substitution')
    op.drop_table('price')
    op.drop_table('assignment')
    op.drop_table('collector_variety')
    op.drop_table('user')
    op.drop_table('collector_outlet')
    op.drop_table('working_price')
    op.drop_table('quality_assurance_assignment')
    op.drop_table('collector_product')
    op.drop_table('collector_area')
    # ### end Alembic commands ###
