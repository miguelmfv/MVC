from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models.models import Disciplina
from app.forms import DisciplinaForm

# Lista todas as disciplinas
@app.route('/disciplinas')
def lista_disciplinas():
    disciplinas = Disciplina.query.all()
    return render_template('disciplinas/lista.html', disciplinas=disciplinas)

# Cria uma nova disciplina
@app.route('/disciplinas/novo', methods=['GET', 'POST'])
def nova_disciplina():
    form = DisciplinaForm()
    if form.validate_on_submit():
        disciplina = Disciplina(nome=form.nome.data)
        db.session.add(disciplina)
        db.session.commit()
        flash('Disciplina cadastrada com sucesso!', 'success')
        return redirect(url_for('lista_disciplinas'))
    return render_template('disciplinas/form.html', form=form)

# Edita uma disciplina existente
@app.route('/disciplinas/editar/<int:id>', methods=['GET', 'POST'])
def editar_disciplina(id):
    disciplina = Disciplina.query.get_or_404(id)
    form = DisciplinaForm(obj=disciplina)
    if form.validate_on_submit():
        disciplina.nome = form.nome.data
        db.session.commit()
        flash('Disciplina atualizada com sucesso!', 'success')
        return redirect(url_for('lista_disciplinas'))
    return render_template('disciplinas/form.html', form=form)

# Deleta uma disciplina
@app.route('/disciplinas/deletar/<int:id>', methods=['POST'])
def deletar_disciplina(id):
    disciplina = Disciplina.query.get_or_404(id)
    db.session.delete(disciplina)
    db.session.commit()
    flash('Disciplina removida com sucesso!', 'success')
    return redirect(url_for('lista_disciplinas'))
