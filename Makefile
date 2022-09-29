.PHONY: run clean

run: setup
	export FLASK_DEBUG=1
	pipenv run flask run --host 0.0.0.0 --port 5000 --debugger

setup:
	pipenv install

# ssh -i "flask-nft-plus.pem" ubuntu@ec2-3-80-115-145.compute-1.amazonaws.com
