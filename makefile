clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

flake8:
	flake8 . --exclude=.venv

pytest:
	pytest . --cov=. $(pytest_args)

CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

test: flake8 pytest
	$(CODECOV)

compile_requirements:
	pipenv lock

.PHONY: build clean flake8 pytest test
