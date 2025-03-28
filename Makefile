test: ## run tests
	python tests/test_base.py
	python tests/test_utils.py

clean-build: ## remove build artifacts
	rmdir /s /q build
	rmdir /s /q dist

dist: ## builds source and wheel package
	python setup.py sdist bdist_wheel

release: dist ## package and upload a release
	twine upload dist/*