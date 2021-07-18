# How to contribute to this project

> If you are interested in contributing to the development and maintenance of this package, it is recommended that you use [poetry](https://poetry.eustace.io) for dependency management and [pyenv](https://github.com/pyenv/pyenv) for python version management.

## Environment

Clone the project

```bash
$ git clone https://github.com/softbutterfly/wagtail-sb-socialnetworks.git
$ cd wagtail-sb-socialnetworks
```

Install the dependencies

```bash
$ poetry install
```

## Testing and coverage

You can run the tests with poetry

```bash
poetry run pytest --cov --cov-report =
poetry run coverage report
```

In case you want to run the tests in all versions you can use [`tox`] (https://tox.readthedocs.io/en/latest/)

## Do you want to send a PR?

Before making your first commit and submitting your pull request, run

```
bash
$ poetry run pre-commit install
```

Then do your commits on a regular basis.

## Code of Conduct

> Please note that this project is published with a Code of Conduct for collaborators. By participating in this project, you agree to abide by its terms.
