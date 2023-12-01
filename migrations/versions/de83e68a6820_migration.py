"""migration

Revision ID: de83e68a6820
Revises: 
Create Date: 2023-12-01 07:27:13.746279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de83e68a6820'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marketing_dealer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marketing_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('article', sa.String(length=30), nullable=True),
    sa.Column('ean_13', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('min_recommended_price', sa.Float(), nullable=True),
    sa.Column('recommended_price', sa.Float(), nullable=True),
    sa.Column('category_id', sa.Float(), nullable=True),
    sa.Column('ozon_name', sa.String(length=150), nullable=True),
    sa.Column('name_1c', sa.String(length=150), nullable=True),
    sa.Column('wb_name', sa.String(length=150), nullable=True),
    sa.Column('ozon_article', sa.String(length=30), nullable=True),
    sa.Column('wb_article', sa.String(length=30), nullable=True),
    sa.Column('ym_article_td', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marketing_dealerprice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_key', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('product_url', sa.String(), nullable=True),
    sa.Column('product_name', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('dealer_id', sa.Integer(), nullable=False),
    sa.Column('markup', sa.Boolean(), nullable=True),
    sa.Column('unclaimed', sa.Boolean(), nullable=True),
    sa.Column('postponed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['marketing_dealer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_key')
    )
    op.create_table('marketing_productdealerkey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_markup', sa.TIMESTAMP(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('dealer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['marketing_dealer.id'], ),
    sa.ForeignKeyConstraint(['key'], ['marketing_dealerprice.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['marketing_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marketing_productdealerkey')
    op.drop_table('marketing_dealerprice')
    op.drop_table('marketing_product')
    op.drop_table('marketing_dealer')
    # ### end Alembic commands ###
