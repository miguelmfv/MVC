"""Criando a tabela intermediária de matrículas

Revision ID: 484e4a63e3cf
Revises: 231fd7b9683f
Create Date: 2024-10-24 13:50:36.215535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '484e4a63e3cf'
down_revision = '231fd7b9683f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matriculas',
    sa.Column('aluno_id', sa.Integer(), nullable=False),
    sa.Column('disciplina_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['aluno_id'], ['alunos.id'], ),
    sa.ForeignKeyConstraint(['disciplina_id'], ['disciplinas.id'], ),
    sa.PrimaryKeyConstraint('aluno_id', 'disciplina_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matriculas')
    # ### end Alembic commands ###
