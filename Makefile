release:
	@poetry run black ./
	@poetry build
	@poetry publish
