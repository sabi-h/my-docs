# python-docs

## Git

### Git logs with graph
git log --all --graph


## npm

#### Learning Resources
- [Npm tutorials by codevolution](https://www.youtube.com/watch?v=6fj0cpmMiVg&list=PLC3y8-rFHvwhgWwm5J3KqzX47n7dwWNrq&ab_channel=Codevolution)


#### Create package.json
`npm init`


#### Install packages in package.json
`npm install`


## Deploy Package to PyPI
```Bash
    pip install cookiecutter twine
    git clone https://github.com/kragniz/cookiecutter-pypackage-minimal.git
    cookiecutter cookiecutter-pypackage-minimal/

    cd DIRECTORY_NAME
    python setup.py sdist bdist_wheel
    twine upload --skip-existing dist/*
```

## Lambda Layers
21 June 2021

- [AWS Lambda Layers Python Youtube](https://www.youtube.com/watch?v=cz8QjmgfGHc)


## Pipenv 
21 Apr 2021

#### Learning Resources:
- [Youtube video by Corey Schafer](https://www.youtube.com/watch?v=zDYL22QNiWk&ab_channel=CoreySchafer)
- [Article by RealPython](https://realpython.com/pipenv-guide/#pipenv-introduction)

### Usage
1. Go to your project root: `cd pipenv-tests`
2. Install a library: `pipenv install pandas`
3. Activate your enviornment: `pipenv shell`
4. Deactivate your environment: `exit`
5. Run python commands without activating enviornment: `pipenv run python`

### Install libraries using requirements.txt file
`pipenv install -r /path/to/requirements.txt`


### Install libraries for dev
`pipenv install pytest --dev`


### Uninstall libraries for dev
`pipenv uninstall pandas`


### Remove pipenv environement
`pipenv --rm`


### Recreate pipenv environement
- `pipenv --rm`
- `pipenv install`


### Check security vulnerablities
- `pipenv check`


### Lock the exact dependencies for Production
Once you're done testing, you want to specify exact version of library, for production. That is what Pipfile.lock is for.
- `pipenv lock`


### Install dependencies using Pipfile.lock
- `pipenv install --ignore-pipfile`


### Enviornment variables are auto-loaded by pipenv, using .env file
- Create `.env` file in project root, and pipenv will load them


### Dependency Graph
`pipenv graph`


### Output dependencies to requirments.txt
`pipenv lock -r > requirments.txt`


#### Explaination

2. When you install a package for the first time
    - Creates a new virtual enviornment for the project, if you arn't already in a virtual enviornment.
    - Creates Pipfile and Pipfile.lock

#### Pipfile and Pipfile.lock best practices:
- Don't have to specify library version
- Once a new library version is realeased, you install it and test
- Once tested and it works, you update the Pipfile.lock and push to production



## Google Cloud

### Read cloud function execution time from logs
```
gcloud functions logs read --project=sixty-odp-bridge-prod bridgetrigger --end-time=2022-08-10 --limit=1000 | grep  "Function execution took" | cut -c86-999 | cut -f1 -dm | sort -r -n | head -10
```


### PostgreSQL

#### Go inside postgres
    psql -U postgres


#### List all postgres users
    \du


#### Create Database
    create database test;


#### List database
    \l

#### Connect to database
    \c test
