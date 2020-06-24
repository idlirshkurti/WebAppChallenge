# WebAppChallenge

pre-requisites:

- Git: https://git-scm.com/downloads
- Anaconda: https://www.anaconda.com/products/individual
- DB Browser for SQLite does __NOT__ need to be installed in the machine.


## Setting up the repository

In order to set up the repository please first clone the repo into a directory of choice. In order to do so you first need to have Git installed into your machine. Once you have Git installed then follow these steps using the _Anaconda Prompt_.

- Clone the repository into a directory z: by navigating to that directory using the _Anaconda Prompt_ and running the following command:

```console
git clone <location_of_bare_repository/WebAppChallenge>
```

- Once the repo is cloned its time to create a conda environment with the appropriate libraries installed as specified in _environment.yml_. Navigate to z/WebAppChallenge and create an empty directory called _envs_ by running:

```console
mkdir envs
```

Then make this your conda environment by running on your _Anaconda Prompt_ shell:

```console
conda env create -p envs -f environment.yml
```

This might take a couple of minutes as it will install the packages necessary, specified in the environment.yml file, for this repository to run. Once these 

```console
conda activate z/WebAppChallenge/envs
```

Once the conda environment is activated, you should be able to see the path of the environment in front of the current directory path in the conda prompt as shown below.

```console
(z/WebAppChallenge/envs) Idlirs-Laptop:WebAppChallenge idlirshkurti$ 
```

In order to run the application you must run _flask_app.py_ by running:


```console
python flask_app.py 
```

## App details

Once the app is run, a new tab on your browser should open at port localhost:5000. The front-end consists of the full table given as input in the bottom, a search bar on the left where you can search for a specific ID and the corresponding SQL query on the right hand side.
__Note__: This app was heavily influenced by this [blogpost](https://medium.com/@agilbert.agtech/a-slick-crud-application-built-using-python-with-flask-and-sqlite3-to-teach-simple-mysql-queries-bd75e1109582)

The data is stored in a database in the root directory as _example.db_. This database consists of 2 tables:
	- logs
	- task_data

The task_data table contains the data from the task_data.csv file in the input folder and the logs table contains the logs of the queries that have been conducted in this app. The queries are stored as strings in a SQL query type format with the corresponding datetime of the query. 

This app could just as easily have a search bar where the user could input exactly the SQL query they need, or maybe instead of one search bar for ID it could have 4 search bars for each column of the data. This could be easily implemented with the current code structure but for simplicity sake I went with one search bar for ID only just to indicate how this is possible. 


## Repository structure

The repository structure should look like the following diagram. 

The _flask_app.py_ is the main python script which runs the entire app. This calls the _sqlquery.py_ script in the functions directory which contains the necessary functions needed to create, read and render the example.db database. _flask_app.py_ then after doing so renders the table and results in the front end which is designed using the _sqldatabase.html_ script in the templates directory.

The _environment.yml_ file contains the libraries necessary for this project to run. These libraries, as explained previously are installed in the conda environment.


```
WebAppChallenge
│   README.md 
│	flask_app.py
│	environment.yml
│
└───functions
│   │   __init__.py
│   │   sqlquery.py
│   
└───templates
│   │   sqldatabase.html
│   
└───input
    │   task_data.csv


```




