# Sentient Robotics — Makefile
# Advanced Humanoid Whole-Body Control Platform

.PHONY: help install install-dev lint format test clean build deploy

help: ## Show this help message
	@echo "Sentient Robotics — Build System"
	@echo "================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install sentient-robotics package
	pip install -e .

install-dev: ## Install with development dependencies
	pip install -e ".[dev]"

install-deploy: ## Install with deployment dependencies
	pip install -e ".[deploy]"

install-teleop: ## Install with teleoperation dependencies
	pip install -e ".[teleop]"

lint: ## Run linters (ruff, black --check, isort --check)
	ruff check sentient_sonic/ decoupled_wbc/
	black --check sentient_sonic/ decoupled_wbc/
	isort --check sentient_sonic/ decoupled_wbc/

format: ## Format code (black, isort)
	black sentient_sonic/ decoupled_wbc/
	isort sentient_sonic/ decoupled_wbc/

test: ## Run tests
	python -m pytest tests/ -v --tb=short

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

build: ## Build package
	python -m build

deploy-check: ## Verify deployment configuration
	@echo "Checking Sentient-SONIC deployment configuration..."
	python -c "import sentient_sonic; print('sentient_sonic OK')"
	@echo "Deployment check passed."

download-checkpoints: ## Download pretrained model checkpoints
	python download_from_hf.py

docs: ## Build documentation
	cd docs && make html
