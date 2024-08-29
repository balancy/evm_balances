all: dev

lint:
	ruff check backend
	black --check backend

dev:
	uv pip compile backend/pyproject.toml -o backend/requirements.txt  > /dev/null
	docker-compose up -d --build

prod:
	docker-compose -f docker-compose.yml up -d --build