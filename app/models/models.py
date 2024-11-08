from app import db

# Tabela intermediária de associação entre Aluno e Disciplina
matriculas = db.Table('matriculas',
    db.Column('aluno_id', db.Integer, db.ForeignKey('alunos.id'), primary_key=True),
    db.Column('disciplina_id', db.Integer, db.ForeignKey('disciplinas.id'), primary_key=True)
)

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    disciplinas = db.relationship('Disciplina', secondary=matriculas, backref='alunos')

    def __repr__(self):
        return f'<Aluno {self.nome}>'

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.nome}>'
