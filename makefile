PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip3


run: install
	- $(PYTHON) src/main.py

venv/bin/python3:
	- python3 -m venv venv

install: venv/bin/python3
	- $(PIP) install -r requirements.txt
