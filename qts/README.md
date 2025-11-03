# FastAPI CI Demo (modificado)

[![CI Pipeline](https://github.com/your-username/fastapi-ci-sample/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/fastapi-ci-sample/actions/workflows/ci.yml)


## 📁 Estrutura do Projeto

```
fastapi-ci-sample/
│
├── app/
│   ├── __init__.py          # Inicialização do pacote
│   ├── main.py              # Aplicação FastAPI principal
│   ├── models.py            # Modelos de dados
│   ├── schemas.py           # Schemas Pydantic
│   └── api_client.py        # Cliente para API externa
│
├── tests/
│   ├── __init__.py          # Inicialização dos testes
│   ├── conftest.py          # Fixtures do Pytest
│   └── test_routes.py       # Testes das rotas
│
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de CI/CD
│
├── requirements.txt         # Dependências do projeto
├── pyproject.toml          # Configuração do Black
├── .flake8                 # Configuração do Flake8
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Documentação
```

## 🚀 Funcionalidades

A API disponibiliza os seguintes endpoints:

- **GET /** - Mensagem de boas-vindas
- **GET /data** - Lista todos os dados da API externa
- **GET /data/{id}** - Busca um dado específico por ID
- **POST /data** - Cria um novo dado (simulado)

## ⚙️ Requisitos

- Python 3.9+
- pip (gerenciador de pacotes Python)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/your-username/fastapi-ci-sample.git
cd fastapi-ci-sample
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🏃 Executando o Projeto

### Modo Desenvolvimento

Execute o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

Documentação interativa (Swagger): `http://localhost:8000/docs`

Documentação alternativa (ReDoc): `http://localhost:8000/redoc`

### Modo Produção

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🧪 Executando os Testes

Execute todos os testes:

```bash
pytest
```

Execute com verbosidade:

```bash
pytest -v
```

Execute com cobertura de código:

```bash
pytest --cov=app --cov-report=html
```

Execute testes específicos:

```bash
pytest tests/test_routes.py -v
```

## 🔧 Verificação de Qualidade de Código

### Formatação com Black

Verificar formatação:
```bash
black --check .
```

Formatar automaticamente:
```bash
black .
```

### Lint com Flake8

```bash
flake8 .
```

### Executar todas as verificações

```bash
black --check . && flake8 . && pytest
```

## 🔄 Integração Contínua (CI)

O projeto está configurado com GitHub Actions para executar automaticamente:

1. **Black** - Verificação de formatação de código
2. **Flake8** - Análise de lint e estilo
3. **Pytest** - Execução dos testes automatizados

O pipeline é acionado em:
- Push para branches `main` ou `master`
- Pull requests para `main` ou `master`

### Status do CI

O badge no topo deste README mostra o status atual do pipeline.

## 📚 API Externa

O projeto consome a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/) para demonstrar integração com serviços externos. Todos os testes utilizam mocks para não depender da API real.

## 🧪 Testes

Os testes incluem:

- ✅ Testes de sucesso para cada endpoint
- ❌ Testes de falha esperada para cada endpoint
- 🎭 Mocks da API externa (sem chamadas reais)
- 📦 Fixtures reutilizáveis
- 🔍 Cobertura de código

## 📋 Dependências Principais

- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI
- **httpx** - Cliente HTTP assíncrono
- **Pytest** - Framework de testes
- **pytest-mock** - Plugin para mocks
- **Black** - Formatador de código
- **Flake8** - Linter Python

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

## 👤 Autor

**Lauro Liberato Neto**



---



### Running the Application

To run the FastAPI application, use Uvicorn:

```
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Running Tests

To run the tests, use pytest:

```
pytest
```

