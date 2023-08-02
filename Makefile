MAINFILE=ddoser.py

PYTHON=python3
PIP=pip3

create_venv:
	$(PYTHON) -m venv venv

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAINFILE)
