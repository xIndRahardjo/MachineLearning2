.PHONY: install install-dev test lint clean

install:
	python -m pip install -e .

install-dev:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src tests

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
