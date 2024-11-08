from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField, SubmitField,StringField
from app.models.models import Aluno, Disciplina

class AlunoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class DisciplinaForm(FlaskForm):
    nome = StringField('Nome da Disciplina', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class MatriculaForm(FlaskForm):
    aluno_id = SelectField('Aluno', coerce=int, validators=[DataRequired()])
    disciplina_id = SelectField('Disciplina', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def __init__(self):
        super(MatriculaForm, self).__init__()
        self.aluno_id.choices = [(aluno.id, aluno.nome) for aluno in Aluno.query.all()]
        self.disciplina_id.choices = [(disciplina.id, disciplina.nome) for disciplina in Disciplina.query.all()]


class AlunosDisciplinaForm(FlaskForm):
    disciplina_id = SelectField('Selecione a Disciplina', coerce=int)
    submit = SubmitField('Ver Alunos')

    def __init__(self):
        super(AlunosDisciplinaForm, self).__init__()
        self.disciplina_id.choices = [(disciplina.id, disciplina.nome) for disciplina in Disciplina.query.all()]