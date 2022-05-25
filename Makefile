start:
	poetry run start

upgrade:
	poetry run alembic upgrade head

downgrade:
	poetry run alembic downgrade base

revision:
	poetry run alembic revision --autogenerate

lint:
	poetry run mypy hero_camp

format:
	poetry run isort hero_camp migrations tests
	poetry run black hero_camp migrations tests

test:
	poetry run pytest
