from flask import render_template, redirect, url_for, request
from app import app
from app.models.models import Disciplina
from app.forms import AlunosDisciplinaForm

# Controller para listar os alunos matriculados em uma disciplina específica
@app.route('/disciplinas/<int:id>/alunos')
def alunos_por_disciplina(id):
    disciplina = Disciplina.query.get_or_404(id)
    alunos = disciplina.alunos  # Acessa os alunos matriculados na disciplina
    return render_template('disciplinas/alunos_por_disciplina.html', disciplina=disciplina, alunos=alunos)

# Rota para selecionar uma disciplina e ver os alunos matriculados
@app.route('/disciplinas/selecionar', methods=['GET', 'POST'])
def selecionar_disciplina():
    form = AlunosDisciplinaForm()
    if form.validate_on_submit():
        # Redireciona para a rota que exibe os alunos matriculados na disciplina selecionada
        return redirect(url_for('alunos_por_disciplina', id=form.disciplina_id.data))
    return render_template('disciplinas/selecionar_disciplina.html', form=form)
