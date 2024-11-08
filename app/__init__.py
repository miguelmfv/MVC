from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import aluno_controller, disciplina_controller, index_controller, matricula_controller, alunos_por_disciplina_controller
