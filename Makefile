VIRTUAL_ENV ?= venv
PIP=$(VIRTUAL_ENV)/bin/pip
PYTHON=$(VIRTUAL_ENV)/bin/python
PYTEST=$(VIRTUAL_ENV)/bin/pytest
RUFF=$(VIRTUAL_ENV)/bin/ruff
TOX=$(VIRTUAL_ENV)/bin/tox
TWINE=$(VIRTUAL_ENV)/bin/twine
PYTHON_MAJOR_VERSION=3
PYTHON_MINOR_VERSION=13
PYTHON_VERSION=$(PYTHON_MAJOR_VERSION).$(PYTHON_MINOR_VERSION)
PYTHON_MAJOR_MINOR=$(PYTHON_MAJOR_VERSION)$(PYTHON_MINOR_VERSION)
PYTHON_WITH_VERSION=python$(PYTHON_VERSION)
SOURCES=rotatepdf/ tests/
BUILD=$(VIRTUAL_ENV)/bin/python -m build


$(VIRTUAL_ENV):
	$(PYTHON_WITH_VERSION) -m venv $(VIRTUAL_ENV)
	$(PIP) install -e .[dev]

virtualenv: $(VIRTUAL_ENV)

test: $(VIRTUAL_ENV)
	$(TOX)

pytest: $(VIRTUAL_ENV)
	$(PYTEST)

lint/ruff/check: $(VIRTUAL_ENV)
	$(RUFF) check $(SOURCES)

lint/ruff/format-check: $(VIRTUAL_ENV)
	$(RUFF) format --check $(SOURCES)

format/ruff/check: $(VIRTUAL_ENV)
	$(RUFF) check --fix $(SOURCES)

format/ruff:
	$(RUFF) format $(SOURCES)
	$(RUFF) check --fix $(SOURCES)

lint: lint/ruff/check lint/ruff/format-check

format: format/ruff

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +
