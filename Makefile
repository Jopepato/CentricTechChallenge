#Basic makefile for creating an environment, updating and installing dependencies
.PHONY: run

create_environment:
	python3.11 -m venv centric
	@echo "Virtual environment successfully created"
	@echo "Activate it with the following command: source centric/bin/activate"
add_kernel_to_jupyter:
	python -m ipykernel install --name=centric
update_requirements:
	pip install pip-tools
	pip-compile requirements.in
	@echo "If you wish to install new requirements, run: make install_requirements"
install_requirements:
	pip install -r requirements.txt
	python -m ipykernel install --name=centric