# BoraJunto ✈️
**Plataforma web colaborativa para planejamento, organização e registro de viagens em grupo.**

---

## 🎯 Objetivo
Centralizar viagens, membros, convites, tarefas, documentos/comprovantes e fotos em uma aplicação web privada para o grupo. Chega de usar planilhas perdidas e grupos de mensagens caóticos; com o BoraJunto, cada detalhe da sua viagem fica organizado e acessível a todos os membros.

## 🎥 Integrantes
* Carlos Andre Sanches
* Carlos Daniel Gomes de Sá
* Felipe Emmanuel
---

## 🛠️ Tecnologias Utilizadas
O sistema foi construído utilizando um stack tecnológico robusto e moderno baseado em Python:
* **Python 3.10+** (Linguagem base)
* **Flask** (Framework Web micro, utilizando Application Factory e Blueprints)
* **Flask-SQLAlchemy** (ORM para banco de dados)
* **Flask-Login** (Gerenciamento de sessão de usuários)
* **Flask-WTF** (Formulários e validações de segurança CSRF)
* **Jinja2** (Motor de templates)
* **Bootstrap 5** (Framework CSS de interface)
* **SQLite** (Banco de dados leve e portátil)
* **pytest** (Framework de testes automatizados)
* **python-dotenv** (Gerenciamento de variáveis de ambiente)

---

## ✅ Funcionalidades do MVP
* Cadastro de usuários
* Login/logout seguro
* Perfil do usuário
* Criação de viagens (definindo destinos e datas)
* Listagem das viagens do usuário
* Painel detalhado (Dashboard) da viagem
* Geração de convites seguros por link
* Entrada e associação de novos membros por convite
* Mural de logística (Tarefas)
* Atribuição de responsáveis nas tarefas
* Alteração de status dinâmico de tarefas (Pendente, Fazendo, Concluído)
* Upload de documentos/comprovantes com controle de extensões
* Download seguro de arquivos e verificação de privilégios de membro
* Galeria colaborativa de fotos com pré-visualização (timeline)
* Controle estrito de acesso por membro/dono da viagem
* Testes automatizados cobrindo os módulos principais

## ❌ Funcionalidades fora do escopo (Não implementadas no MVP)
* Divisão de custos financeiros
* Comentários diretos em fotos
* Botões de curtidas
* Chat interno de texto
* Notificações via e-mail ou push
* Exportação em PDF de cronogramas
* Integrações externas com APIs de turismo (Hotéis, Voos, Clima)

---

## 📁 Estrutura do Projeto
O código utiliza o padrão arquitetural de **Application Factory** e divide suas responsabilidades em **Blueprints**:
* `app.py`: O ponto de entrada que inicializa a aplicação.
* `borajunto/`: O pacote principal do projeto contendo a lógica de negócios.
* `borajunto/ext/`: Extensões Flask inicializadas de forma isolada (Configuração, DB, Login, WTF).
* `borajunto/models/`: Representações das tabelas do banco de dados via SQLAlchemy (Classes).
* `borajunto/forms/`: Definições dos formulários com Flask-WTF.
* `borajunto/views/`: Blueprints e rotas principais para gerenciar Viagens, Auth, Arquivos e Tarefas.
* `borajunto/services/`: Lógicas isoladas e funções de utilidade (como manipulação física de uploads).
* `templates/`: Páginas em HTML utilizando Jinja2 e integração visual com Bootstrap.
* `static/`: Arquivos CSS nativos, imagens e JavaScript complementar.
* `tests/`: Suíte completa de testes automatizados modulares com `pytest`.
* `instance/uploads/`: Diretório ignorado pelo controle de versão para armazenamento de uploads reais.

---

## 🚀 Como Instalar
Siga os passos abaixo para configurar o projeto no **Windows PowerShell**:

1. Crie o ambiente virtual:
```powershell
python -m venv venv
