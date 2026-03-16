# Sistema de Catálogo e Estoque (Monólito)

Esta é uma API construída em Python e desenvolvida para gerenciar o catálogo de produtos e o controle de estoque. O projeto segue a arquitetura de Monólito, utilizando o padrão de separação por responsabilidades (Models, Schemas, Controllers).

## 💻 Tecnologias Utilizadas:

* **Python 3**
* **FastAPI:** Framework web rápido e moderno para a construção da API.
* **SQLAlquemy:** ORM (Objeect Relational Mapper) para a comunicação com o banco de dados.
* **SQLite:** Banco de dados em arquivo físico ('catalogo.db'), ideal para desenvolvimento e testes locais sem necessidade de infraestrutura de rede.
* **Uvicorn:** Servidor web para rodar a aplicação FastAPI. Inicializar com uvicorn main:app --reload no terminal (analisar se a venv está ativa), em seguida seguir a URL informada no terminal.

** 📁 Estrutura do Projeto:

O projeto está organizado na seguinte estrutura de diretórios para manter a separação de responsabilidades:

```text
/
├── controllers/          # Rotas e regras de negócio da API
│   └── produto.py
├── models/               # Entidades e tabelas do Banco de Dados
│   └── produto.py
├── schemas/              # Validação de dados de entrada/saída (DTOs)
│   └── produto.py
├── database.py           # Configuração e conexão com o banco SQLite
└── main.py               # Ponto de entrada que inicializa a aplicação