install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 gendiff

check-coverage:
	poetry run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml