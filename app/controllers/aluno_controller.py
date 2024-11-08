from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models.models import Aluno
from app.forms import AlunoForm

# Lista todos os alunos
@app.route('/alunos')
def lista_alunos():
    alunos = Aluno.query.all()
    return render_template('alunos/lista.html', alunos=alunos)

# Cria um novo aluno
@app.route('/alunos/novo', methods=['GET', 'POST'])
def novo_aluno():
    form = AlunoForm()
    if form.validate_on_submit():
        aluno = Aluno(nome=form.nome.data)
        db.session.add(aluno)
        db.session.commit()
        flash('Aluno cadastrado com sucesso!', 'success')
        return redirect(url_for('lista_alunos'))
    return render_template('alunos/form.html', form=form)

# Edita um aluno existente
@app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    form = AlunoForm(obj=aluno)  # Preenche o formulário com os dados do aluno
    if form.validate_on_submit():
        aluno.nome = form.nome.data
        db.session.commit()
        flash('Aluno atualizado com sucesso!', 'success')
        return redirect(url_for('lista_alunos'))
    return render_template('alunos/form.html', form=form)

# Deleta um aluno
@app.route('/alunos/deletar/<int:id>', methods=['POST'])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    flash('Aluno removido com sucesso!', 'success')
    return redirect(url_for('lista_alunos'))
