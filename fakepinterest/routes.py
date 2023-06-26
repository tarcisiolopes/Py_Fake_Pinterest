# rotas do site
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    return render_template("homepage.html", form=form_login)

@app.route("/criar_conta", methods=["GET", "POST"])
def criar_conta():
    form_criar_conta = FormCriarConta()
    return render_template("criar_conta.html", form=form_criar_conta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)