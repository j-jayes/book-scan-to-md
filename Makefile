.PHONY: help setup install clean test lint format

help:
	@echo "Available commands:"
	@echo "  make setup      - Create virtual environment with uv"
	@echo "  make install    - Install dependencies"
	@echo "  make clean      - Remove generated files and cache"
	@echo "  make test       - Run tests (if available)"
	@echo "  make lint       - Run code linters"
	@echo "  make format     - Format code with black"

setup:
	uv venv
	@echo "Virtual environment created. Activate with: source .venv/bin/activate"

install:
	uv pip install -e .
	@echo "Dependencies installed successfully"

install-dev:
	uv pip install -e ".[dev]"
	@echo "Development dependencies installed successfully"

clean:
	rm -rf data/processed/*
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "Cleaned generated files and cache"

clean-all: clean
	rm -rf data/output/*
	@echo "Cleaned all generated files including outputs"

lint:
	ruff check scripts/
	@echo "Linting complete"

format:
	black scripts/
	@echo "Code formatted"

test:
	pytest tests/ -v
	@echo "Tests complete"
