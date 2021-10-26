SHELL=/bin/bash

VENV_NAME?=venv
VENV_BIN=$(shell pwd)/${VENV_NAME}/bin
VENV_ACTIVATE=. ${VENV_BIN}/activate

install-dep:
	pip install --upgrade pip
	pip install --upgrade -r requirements/dep.txt
	pip freeze > requirements.txt