from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models.models import Aluno, Disciplina
from app.forms import MatriculaForm

# Lista todos os alunos e suas disciplinas associadas
@app.route('/matriculas')
def lista_matriculas():
    # Busca apenas os alunos que estão matriculados em pelo menos uma disciplina
    alunos = Aluno.query.join(Aluno.disciplinas).all()
    return render_template('matriculas/lista.html', alunos=alunos)


# Cria uma nova matrícula (associação entre Aluno e Disciplina)
@app.route('/matriculas/nova', methods=['GET', 'POST'])
def nova_matricula():
    form = MatriculaForm()
    if form.validate_on_submit():
        aluno = Aluno.query.get(form.aluno_id.data)
        disciplina = Disciplina.query.get(form.disciplina_id.data)
        aluno.disciplinas.append(disciplina)  # Associa o aluno à disciplina
        db.session.commit()
        flash('Matrícula criada com sucesso!', 'success')
        return redirect(url_for('lista_matriculas'))
    return render_template('matriculas/form.html', form=form)

# Remove uma associação entre Aluno e Disciplina (Matrícula)
@app.route('/matriculas/deletar/<int:aluno_id>/<int:disciplina_id>', methods=['POST'])
def deletar_matricula(aluno_id, disciplina_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    disciplina = Disciplina.query.get_or_404(disciplina_id)
    aluno.disciplinas.remove(disciplina)  # Remove a associação entre aluno e disciplina
    db.session.commit()
    flash('Matrícula removida com sucesso!', 'success')
    return redirect(url_for('lista_matriculas'))


