COMPOSE_RUN_APP := run --rm delivery
.DEFAULT_GOAL := help

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## Build application
	docker-compose build

generate_migration:  ## Generate new migrations. Using: make generate_migrations NAME="migration_name"
	docker-compose $(COMPOSE_RUN_APP) alembic revision --autogenerate -m '$(NAME)'

migrate:  ## Apply migrations
	docker-compose $(COMPOSE_RUN_APP) alembic upgrade head

downgrade_migration:  ## Downgrade latest migration
	docker-compose $(COMPOSE_RUN_APP) alembic downgrade -1

start:  ## Start application
	docker-compose up

isort:  ## Run isort
	docker-compose $(COMPOSE_RUN_APP) isort .

flake8:  ## Run flake8
	docker-compose $(COMPOSE_RUN_APP) flake8

pylint:  ## Run pylint
	docker-compose $(COMPOSE_RUN_APP) pylint src/

all_lint:  ## Run all linters
	docker-compose $(COMPOSE_RUN_APP) /bin/bash -c "isort . && flake8 && pylint ."
