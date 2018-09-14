# vulnerable_flask_app

## Installation
```
pipenv --python 3.6.5 install
pipenv shell
pip install flask
```

## To run locally
```pipenv shell && export FLASK_APP=xss_flask.py && flask run```

## To expose the app to the rest of the network over port 80
```pipenv shell && export FLASK_APP=xss_flask.py && flask run --host=0.0.0.0 --port=80```
