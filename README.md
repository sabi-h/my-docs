# python-docs

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


### Output dependencies to requirments.txt
`pipenv lock -r`


#### Explaination

2. When you install a package for the first time
    - Creates a new virtual enviornment for the project, if you arn't already in a virtual enviornment.
    - Creates Pipfile and Pipfile.lock

#### Pipfile and Pipfile.lock best practices:
- Don't have to specify library version
- Once a new library version is realeased, you install it and test
- Once tested and it works, you update the Pipfile.lock and push to production

