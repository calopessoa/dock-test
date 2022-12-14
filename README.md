# E2E Automated Test for Dock Home Page

### Project that tests Dock access to its home page and fill its contact form to send it.
[![Dock - Financial Technologies](https://github.com/calopessoa/dock-test/actions/workflows/pipeline.yml/badge.svg)](https://github.com/calopessoa/dock-test/actions/workflows/pipeline.yml)

## Tools used:
- Python
- Pytest-BDD
- Playwright
- Github Actions (CI/CD)


## Usage:

To use this 2e2 tool, import the project:

```bash
git clone 'git@github.com:calopessoa/dock-test.git'
```
Then, move to the local folder:

```bash
cd dock-test
```
Then, install the dependencies, inside the virtual environment:

```bash
python3 -m venv .venv && source .venv/bin/activate
```
```bash
python3 -m pip install -r requirements.txt
```

Finally, run the script for Playwright (it'll run both test files, with and without BDD):

```bash
pytest
```

## To-Do:

Investigate how to test the accessibility tools
- this author recommends further improvement with the audio helper in english
