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
source centricvenv/bin/activate
make install_requirements
make add_kernel_to_jupyter
make dev_install
```

Once we have run those commands we will be able to run the cells in the jupyter notebook.

## Task 1 and 2

For these 2 tasks I've added functions to the source code, you can check those in the `centric` folder and the tests in `tests`.
As well as creating two notebooks, which is better to follow as they will have all the reasoning of the steps followed and will use
the functions declared in the source code. A problem encountered is the size of the data, which could not be added to the repository,
so you will have to run the first notebook: `data_loading_and_eda.ipynb` in order to create the different splits of the data that are later used
in the second notebook: `model_creation_and_validation.ipynb`. Those notebooks can be found in the folder `notebooks`.

Hopefully, the notebooks are clear enough, I've added a summary of the steps and conclusions at the beginning of each of them.
As well as watermarks to check the versions of the packages used.


## Task 3 - CI/CD Deployment plan

This task can be found in `docs/Task_3.md`.
I have made a summary of the deployment plan both for CICD and the model deployment. I have also included some visual representations
of the approaches to help visualize them. These are simple approach that will need to be improved throughout time and to be modified to follow the
team best practices and technologies that are currently being used. But they work as a template on how it could be done.

## Task 4 - SQL and Django ORM query

This task can be found in `docs/Task_4.md`.
The SQL query has been prettified but not tested in a proper system, as it's an indication on how to do the different joins
and extract the relevant information. For the Django ORM, as it's the first time using that ORM I've done my best while looking at the
documentation and online examples, it would be great to learn more about this if I were to join the team :)
