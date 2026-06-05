# BoraJunto ✈️
**Plataforma web colaborativa para planeamento, organização e registo de viagens em grupo.**

---

## 🎯 Objetivo
Centralizar viagens, membros, convites, tarefas, documentos/comprovantes e fotos numa aplicação web privada para o grupo. Acabaram-se as planilhas perdidas e os grupos de mensagens caóticos; com o BoraJunto, cada detalhe da sua viagem fica organizado e acessível a todos os membros.

## 🎥 Integrantes
* Carlos Andre Sanches
* Carlos Daniel Gomes de Sá
* Felipe Emmanuel 
---

## 🛠️ Tecnologias Utilizadas
O sistema foi construído utilizando uma stack tecnológica robusta e moderna baseada em Python:
* **Python 3.10+** (Linguagem base)
* **Flask** (Framework Web micro, utilizando Application Factory e Blueprints)
* **Flask-SQLAlchemy** (ORM para base de dados)
* **Flask-Login** (Gestão de sessão de utilizadores)
* **Flask-Admin** (Painel administrativo corporativo)
* **Flask-WTF** (Formulários e validações de segurança CSRF)
* **Jinja2** (Motor de templates)
* **Bootstrap** (Framework CSS de interface)
* **SQLite** (Base de dados leve e portátil)
* **pytest** (Framework de testes automatizados)
* **python-dotenv** (Gestão de variáveis de ambiente)

---

## ✅ Funcionalidades
* Registo e Autenticação segura de utilizadores.
* Criação e gestão de viagens (destinos, datas, cronogramas).
* Envio de convites seguros por link para novos membros.
* Mural de logística (Tarefas) com atribuição de responsáveis e status.
* Upload de documentos e comprovativos com controlo rigoroso de extensões.
* Galeria colaborativa de fotos.
* Backoffice (Painel Admin) protegido para gestão total de dados (CRUD).
* Controlo estrito de permissões (apenas membros acedem à viagem).

---

## 📁 Estrutura do Projeto
O código utiliza o padrão arquitetural de **Application Factory** e divide as suas responsabilidades em **Blueprints**:
* `app.py`: O ponto de entrada que inicializa a aplicação.
* `borajunto/ext/`: Extensões Flask inicializadas de forma isolada (DB, Login, WTF, Admin).
* `borajunto/models/`: Representações das tabelas da base de dados via SQLAlchemy.
* `borajunto/forms/`: Definições dos formulários de entrada de dados.
* `borajunto/views/`: Blueprints com as rotas para gerir Viagens, Auth, Ficheiros e Tarefas.
* `borajunto/services/`: Lógicas complexas isoladas das rotas (ex: permissões e uploads).
* `templates/` e `static/`: Ficheiros visuais e de estilo do frontend.
* `tests/`: Suíte completa de testes modulares com `pytest`.

---

## 🚀 Como Instalar (Windows)
Siga os passos abaixo no terminal da raiz do projeto:

1. Crie o ambiente virtual:
python -m venv venv

2. Ative o ambiente virtual:
.\venv\Scripts\activate
(Nota: Caso o Windows bloqueie, rode "Set-ExecutionPolicy Unrestricted -Scope CurrentUser" e tente novamente)

3. Instale todas as dependências do projeto:
python -m pip install -e ".[dev,test]"

---

## ⚙️ Como Executar

1. Inicie o servidor do Flask:
flask run

2. Aceda ao site no seu navegador:
http://127.0.0.1:5000

3. Para aceder ao Painel Administrativo (é necessário fazer login primeiro no site):
http://127.0.0.1:5000/admin
