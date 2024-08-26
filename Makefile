all: lint

lint:
	ruff check backend
	black --check backend