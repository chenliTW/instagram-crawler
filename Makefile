test:
		coverage run -m unittest discover
		coverage report
		coverage html

citest:
		coverage run -m unittest discover
		coverage xml
