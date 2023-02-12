# Gensim model with Flask API

## Install Requirements
```
$ pip install virtualenv
$ python -m venv {{virtual-environment-name}}
$ open env/scripts/activate.bat (windows)
$ pip install -r requirements.txt
```

## Testing trained model on REST API
```
$ python api.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

To run REST API, call the following url.
```
http://127.0.0.1:5000/?word={{CODE_PRODUIT}}
```
