release:
	@pipenv run black ./
	@rm -rf dist/
	@python setup.py sdist
	@twine upload dist/*
