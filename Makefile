.PHONY: run clean

run: setup
	export FLASK_DEBUG=1
	pipenv run flask run --host 0.0.0.0 --port 5000

setup:
	pipenv install
