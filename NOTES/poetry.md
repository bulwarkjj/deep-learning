# INDEX  
[Docs](#docs)  
[Common Commands](#common-poetry-commands)  
[trouble shooting](#trouble-shooting)
### DOCS  
- [Poetry doc page](https://python-poetry.org/docs/)
- [poetry env docs, includes pyenv use](https://python-poetry.org/docs/managing-environments/)
- [poetry cli commands](https://python-poetry.org/docs/cli/)
### COMMON POETRY COMMANDS  
- `poetry install` __installs deps from .toml file into current project__
- `poetry add <package>`  __installs specified package and updates the lock/toml file for project deps__  
- `poetry shell`  __activates the poetry venv (for IDE's make sure that you have the poetry env name as the python interpreter)__   
- `poetry update` __gets/installs the latest version of the deps (if they are not locked) and updates lock file with the newest version__
- `poetry env`  __used to get info of venv environment, use a different venv, clear venv's, etc. ref:[env docs](https://python-poetry.org/docs/managing-environments/)__
### Trouble shooting  
- if you get a python error stating that no such package exsits, import error, or package not found:
  - make sure your `poetry shell` is activated
    - if shell is active but still getting errors, make sure the pyhon interpreter is set to the poetry shell
  - if poetry shell is activated, then use `poetry install`.  someone may have added a new dep for the script and it needs to be added