"""Initial database

Revision ID: 2405c8380524
Revises: 
Create Date: 2023-02-24 10:58:00.850089

"""
from alembic import op
import sqlalchemy as sa
from passlib.hash import sha256_crypt

# revision identifiers, used by Alembic.
revision = '2405c8380524'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    users_table = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('workers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('tasks', sa.Integer(), nullable=False),
    sa.Column('last_task_at', sa.DateTime(), nullable=True),
    sa.Column('total_time', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('base_filename', sa.String(length=64), nullable=False),
    sa.Column('config', sa.JSON(), nullable=False),
    sa.Column('geojson', sa.JSON(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.Column('requested_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('requests', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('base_filename')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('res_data', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    # Registers the default admin user
    op.bulk_insert(users_table,
    [
        {
            'id':1,
            'admin': True,
            'email': 'admin',
            'password': sha256_crypt.encrypt('admin'),
            'name': 'Administrator',
            'company': 'CityZones'
        }
    ]
)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('tasks')
    op.drop_table('workers')
    op.drop_table('users')
    # ### end Alembic commands ###