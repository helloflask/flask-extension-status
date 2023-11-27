from pathlib import Path

from jinja2 import Template
import yaml

basedir = Path(__file__).parent

workflow_template = """
name: {{ package_name }}

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install {{ package_name }} flask

      - name: Test initialization
        run:
          python -c "from flask import Flask; app = Flask(__name__); {{ init_string }}"

"""

table_header = """
| Extension Repository | Latest version  |  Downloads | Build with latest Flask (3.x) and Python (3.12.x) |
| -------------------- | --------------- | ---------- | ------------------------------------------------- |"""

table_row_template = "| [{{ repo }}](https://github.com/{{ repo }}) " \
"| ![PyPI - Version](https://img.shields.io/pypi/v/{{ package_name }}) " \
"| ![PyPI - Downloads](https://img.shields.io/pypi/dm/{{ package_name }}?color=darkgrey) " \
"| [![build](https://github.com/greyli/flask-extension-status/actions/workflows/{{ package_name }}.yml/badge.svg)](https://github.com/greyli/flask-extension-status/actions/workflows/{{ package_name }}.yml) |"


def get_extensions():
    with open(basedir / 'extensions.yml') as f:
        extensions = yaml.safe_load(f)
        # sort extensions by name
        extensions = dict(sorted(extensions.items(), key=lambda item: item[0]))
        return extensions 

def gen_workflow(package_name, repo, init_string):
    template = Template(workflow_template)
    return template.render(
        package_name=package_name,
        repo=repo,
        init_string=init_string
    )


def update_readme_table():
    readme_file = basedir / 'README.md'
    
    new_table = ''
    for package_name, info in get_extensions().items():
        repo = info['repo']
        new_table += Template(table_row_template).render(
            package_name=package_name,
            repo=repo
        ) + '\n'

    table_start_string = '<!-- TABLE_START -->'
    table_end_string = '<!-- TABLE_END -->'

    table_start_delimiter = readme_file.read_text().find(table_start_string)
    table_end_delimiter = readme_file.read_text().find(table_end_string)
    before_table = readme_file.read_text()[:table_start_delimiter]
    after_table = readme_file.read_text()[table_end_delimiter + len(table_end_string):]

    with open(readme_file, 'w') as f:
        f.write(
            before_table +
            '<!-- TABLE_START -->' +
            '\n' +
            table_header +
            '\n' +
            new_table +
            '\n<!-- TABLE_END -->' +
            after_table
        )


if __name__ == '__main__':
    for package_name, info in get_extensions().items():
        repo = info['repo']
        init_string = info['init_string']
        workflow = gen_workflow(package_name, repo, init_string)
        with open(basedir / f'.github/workflows/{package_name}.yml', 'w') as f:
            f.write(workflow)
    update_readme_table()
