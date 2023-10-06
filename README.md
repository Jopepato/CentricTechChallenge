# Centric Software - Machine learning task

This repository has been created by José Pérez-Parras Toledano, to execute the technical challenge from Centric Software.
Documentation can be found in this README file, as well as instructions on how to run the different parts of the task.
Data has been saved in the repository as well, so that everything is in one place.

I have created a repository to store some of the functions used throughout the notebook for future reuse of them. I have also
converted this repository into a python package so that we can use the different functions in the jupyter notebook. This is a simplification
of what a python package would look like, I would usually use `cookiecutter` for this as it's a template for python repositories,
but not add complexity to the task and to save some time, I've just added the necessary items and files for the task.

## How to install dependencies
I've created a Makefile file to make things simpler, to create an environment with the packages used to run the notebook and the task
simply run the following commands:
```
make create_environment
source centric/bin/activate
make install_requirements
make add_kernel_to_jupyter
make dev_install
```

Once we have run those commands we will be able to run the cells in the jupyter notebook.

## Task 1 and 2


## Task 3 - CI/CD Deployment plan

This task can be found in `docs/Task_3.md`.
I have made a summary of the deployment plan both for CICD and the model deployment. I have also included some visual representations
of the approaches to help visualize them. These are simple approach that will need to be improved throughout time and to be modified to follow the
team best practices and technologies that are currently being used. But they work as a template on how it could be done.

## Task 4 - SQL and Django ORM query

This task can be found in `docs/Task_4.md`.
There has been created a source code and a test to check that the Django ORM query is working properly,
the source code for retrieving the relevant information from the schema can be seen in: `source/dataset/orm.py` while the test
can be seen in `tests/test_orm.py`. To run the test and check that is working properly, just run:
```
make run_unit_tests
```

As you will see, everything will be in green, meaning that the test is running properly and the orm query is working.