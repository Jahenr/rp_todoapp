RP Python typer cli tutorial application

I followed the Real Python tutorial to create a cli to-do application using typer.
url - https://realpython.com/python-typer-cli/#project-overview

The application allows you to add, list, complete, remove and clear all tasks that are added in the applications database.


Install:

To install the application first clone the repo and install the requirements by running:

python3 -m pip install requirements.txt

Once the modules and dependencies have been installed, change to the project directory and run:

python -m rptodo --help

This will display all of the options you may use.


Commands:

Command list
-------------------------------------------------
| init | add | list | complete | remove | clear |  
-------------------------------------------------


To initilise the database and store the json file in default or specified location run:

python -m rptodo init


To add a task to the todo application with a default priority number run:

python -m rptodo add My test task
    Tip: Not adding a priority number will default the priority to 2


To add a task with a priority number run(range is from 1 to 3):

python -m rptodo add My test task 2 -p1


To list tasks added run:

python -m rptodo list


To complete the task added and mark done as True run:

python -m rptodo complete <ID>
	Tip: Specify the id assigned to the task you want to mark as completed


To remove the task added run:

python -m rptodo remove <ID>


To clear all entries in the todo database run:

python -m rptodo clear




