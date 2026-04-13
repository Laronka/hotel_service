# Trabalho 3 de 11 — Testes de Componente em Python

## Como executar

Crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Rodando os testes

Testes de unidade:

```bash
pytest tests/unit
```

Todos os testes:

```bash
pytest
```

Os testes de componente deverão ser implementados em:

```text
tests/components/
```
