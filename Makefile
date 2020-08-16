APP_NAME=lists

clean:
	rm -rf .pytest_cache/ .coverage build/ dist/ ron_cipher*/ junit_test_report.xml

install-deps:
	pip install -r requirements.txt

test:
	python -s -m pytest tests/ --cov=$(APP_NAME)/ --cov-report term-missing --junitxml=junit_test_report.xml

lint:
	flake8 $(APP_NAME)/ tests/

format:
	black $(APP_NAME) --line-length 79

format-check:
	black $(APP_NAME) --check --line-length 79

build:
	python setup.py sdist bdist_wheel

local-test:
	pip uninstall -y list_manager
	make clean
	make build
	pip install dist/list_manager-*-py3-none-any.whl
