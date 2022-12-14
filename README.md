# Test Task delivery-service

To build and run:

```
cp .env.example .env
make build
make start
make migrate
```

Docs will be available at http://localhost:8000/docs

To run linters:

```
make flake8
make pylint
```