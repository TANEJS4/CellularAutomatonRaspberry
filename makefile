
activate:
	(\
		source ${HOME}/Projects/cellularAutomaton/.venv/bin/activate;\
		pip install -r requirement.txt;\
	)

test: activate
	python test.py