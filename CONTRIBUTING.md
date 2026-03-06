# Contributing

## Setup

```bash
uv sync
pre-commit install
```

## Development workflow

Run the API locally:
```bash
uvicorn practicerepo.app:app --reload
```

Interactive docs available at `http://localhost:8000/docs`.

## Code style

- Line length: 120 characters
- Linter and formatter: ruff
- No defensive code — keep it simple and readable

Ruff runs automatically on commit via pre-commit. To run manually:
```bash
ruff check .
ruff format .
```

## Tests

```bash
pytest                          # all tests
pytest tests/unit/              # unit only
pytest tests/integration/       # integration only
pytest tests/functional/        # functional only
pytest tests/unit/test_models.py::test_item_valid  # single test
```

Tests are organized in three layers:
- **unit** — Pydantic model validation, no HTTP
- **integration** — each endpoint tested in isolation
- **functional** — multi-step flows (create → list, create → get)

The in-memory store is reset before every test via the `reset_store` fixture in `conftest.py`.

## Docker

```bash
docker build -t practicerepo .
docker run -p 8000:8000 practicerepo
```

## Project structure

```
src/practicerepo/
  app.py      ← FastAPI app and route handlers
  models.py   ← Pydantic models
tests/
  conftest.py
  unit/
  integration/
  functional/
```
