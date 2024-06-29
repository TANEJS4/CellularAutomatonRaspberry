
activate:
	(\
		source .venv/bin/activate;\
		pip install -r requirement.txt;\
	)

test:
	python test.py


visual:
	python visual.py