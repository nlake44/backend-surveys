# backend-surveys
Python backend for survey app

# Installation

sudo apt-get install python3

sudo apt-get install python3-venv

python3 -m venv env

source env/bin/activate

For Mac only: Add the following to .zshrc
```
alias python=/usr/local/bin/python3.8
alias pip=/usr/local/bin/pip3
PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.8/bin/
```

For Mac only:

```
source /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/virtualenv/activation/bash/activate.sh
```

sudo apt install python3-pip

For Mac only:

```
Get the get-pip.py script and run it.
```

pip install --upgrade pip

pip install django

# To run
source env/bin/activate


python3 manage.py runserver 0.0.0.0:8080

# Make Person API Calls
Send a request with the following parameter: APIKEY
where the API key is a UUID (primary key) from the APIKey model.

## Example
persons/1/?APIKEY=1234-1234-1234-1234

# Make Survey API Calls
Send a request with the correct UUID of the survey.
