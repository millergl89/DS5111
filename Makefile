ENV = env
PYTHON = $(ENV)/bin/python3
PIP = $(ENV)/bin/pip
PYLINT = $(PYTHON) -m pylint
PYTEST = $(PYTHON) -m pytest

.PHONY: default env update lint test run test_enrich clean

default:
	@cat Makefile

env:
	python3 -m venv $(ENV)
	$(PYTHON) -m pip install --upgrade pip

update: env
	$(PIP) install -r requirements.txt

lint:
	$(PYLINT) bin/ lib/ tests/

test:
	$(PYTEST) -vv tests/

run:
	cat test_ids | $(PYTHON) -u bin/extract_transcripts.py | \
	$(PYTHON) -u bin/enrich_transcripts.py | \
	$(PYTHON) bin/validate_schema.py

test_enrich:
	cat mock_transcripts.jsonl | \
	$(PYTHON) -u bin/enrich_transcripts.py | \
	$(PYTHON) bin/validate_schema.py

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache
