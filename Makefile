# Voice-Based Quiz Generator Makefile

.PHONY: help install setup test demo run clean test-all organize

# Default target
help:
	@echo "Voice-Based Quiz Generator"
	@echo "=========================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make setup      - Run full setup (install + configure)"
	@echo "  make test       - Test installation"
	@echo "  make test-all   - Run all tests in tests/ directory"
	@echo "  make demo       - Run demo without full setup"
	@echo "  make run        - Run the Streamlit application"
	@echo "  make clean      - Clean temporary files"
	@echo "  make organize   - Organize project structure"
	@echo "  make help       - Show this help message"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "Dependencies installed successfully!"

# Full setup
setup:
	@echo "Running full setup..."
	python setup.py
	@echo "Setup complete!"

# Test installation
test:
	@echo "Testing installation..."
	python tests/test_installation.py

# Run all tests
test-all:
	@echo "Running all tests..."
	python tests/test_installation.py
	python tests/verify_setup.py
	python tests/quick_test.py
	@echo "All tests completed!"

# Run demo
demo:
	@echo "Running demo..."
	python examples/demo.py

# Organize project structure
organize:
	@echo "Organizing project structure..."
	mkdir -p docs tests examples scripts assets
	@echo "Project structure organized!"

# Run the application
run:
	@echo "Starting Voice-Based Quiz Generator..."
	@echo "Open your browser to http://localhost:8501"
	streamlit run app.py

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.tmp" -delete
	find . -type f -name "*.mp3" -delete
	find . -type f -name "*.wav" -delete
	@echo "Cleanup complete!"

# Development helpers
dev-install:
	@echo "Installing development dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black flake8 pytest
	@echo "Development environment ready!"

# Format code
format:
	@echo "Formatting code..."
	black *.py
	@echo "Code formatted!"

# Lint code
lint:
	@echo "Linting code..."
	flake8 *.py --max-line-length=88 --ignore=E203,W503
	@echo "Linting complete!"

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	python -m venv venv
	@echo "Virtual environment created!"
	@echo "Activate with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"

# Install in virtual environment
venv-install: venv
	@echo "Installing in virtual environment..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@echo "Installation in virtual environment complete!"

# Quick start (for new users)
quickstart:
	@echo "Quick start setup..."
	@echo "1. Creating virtual environment..."
	python -m venv venv
	@echo "2. Installing dependencies..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@echo "3. Creating configuration..."
	cp .env.example .env
	@echo ""
	@echo "Quick start complete!"
	@echo ""
	@echo "Next steps:"
	@echo "1. Activate virtual environment: source venv/bin/activate"
	@echo "2. Edit .env file and add your OpenAI API key"
	@echo "3. Run: make run"
