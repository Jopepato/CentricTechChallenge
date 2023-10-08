#Basic makefile for creating an environment, updating and installing dependencies
.PHONY: run

create_environment:
	python3.11 -m venv centricvenv
	@echo "Virtual environment successfully created"
	@echo "Activate it with the following command: source centricvenv/bin/activate"

add_kernel_to_jupyter:
	python -m ipykernel install --name=centricvenv

update_requirements:
	pip install pip-tools
	pip-compile requirements.in
	@echo "If you wish to install new requirements, run: make install_requirements"

install_requirements:
	pip install -r requirements.txt
	python -m ipykernel install --name=centricvenv

dev_install:
	pip install -e .

run_unit_tests:
	pytest tests/


lint:
	black centric/
	black tests/