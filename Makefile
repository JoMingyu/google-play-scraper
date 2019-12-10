release:
	@python setup.py sdist
	@twine upload dist/*
