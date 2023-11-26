from pathlib import Path

from jinja2 import Template

basedir = Path(__file__).parent

extensions = {
    'apiflask': {'repo': 'apiflask/apiflask', 'import_string': 'from apiflask import APIFlask'},
    'bootstrap-flask': { 'repo': 'helloflask/bootstrap-flask', 'import_string': 'from apiflask import APIFlask'},
    'flask-ckeditor': { 'repo': 'helloflask/flask-ckeditor', 'import_string': 'from flask_ckeditor import CKEditor'},
    'flask-debugtoolbar': { 'repo': 'pallets-eco/flask-debugtoolbar', 'import_string': 'from flask_debugtoolbar import DebugToolbarExtension'},
    'flask-login': {'repo': 'maxcountryman/flask-login', 'import_string': 'from flask_login import LoginManager'},
    'flask-mailman': { 'repo': 'waynerv/flask-mailman', 'import_string': 'from flask_mailman import Mail'},
}

workflow_template = """
name: test {{ repo }}

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  workflow_dispatch:

jobs:
  test:
    strategy:
      matrix:
        python-versions: ['3.12']
        os: [ubuntu-latest, macos-latest, windows-latest]
    {% raw %}runs-on: ${{ matrix.os }}{% endraw %}

    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: {% raw %}${{ matrix.python-versions }}{% endraw %}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install {{ package_name }} flask

      - name: Test import
        run:
          python -c "{{ import_string }}"

"""

table_header = """
| Extension | Latest PyPI version  | PyPI downloads/month | Build with Flask 3.x |
| --------- | -------------------- | -------------------- | -------------------- |"""

table_row_template = "| [{{ repo }}](https://github.com/{{ repo }}) " \
"| ![PyPI - Version](https://img.shields.io/pypi/v/{{ package_name }}) " \
"| ![PyPI - Downloads](https://img.shields.io/pypi/dm/{{ package_name }}?color=black) " \
"| ![build](https://github.com/greyli/flask-extension-status/actions/workflows/{{ package_name }}.yml/badge.svg) |"


def gen_workflow(package_name, repo, import_string):
    template = Template(workflow_template)
    return template.render(
        package_name=package_name,
        repo=repo,
        import_string=import_string
    )


def update_readme_table():
    readme_file = basedir / 'README.md'
    
    new_table = ''
    for package_name, info in extensions.items():
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
    for package_name, info in extensions.items():
        repo = info['repo']
        import_string = info['import_string']
        workflow = gen_workflow(package_name, repo, import_string)
        with open(basedir / f'.github/workflows/{package_name}.yml', 'w') as f:
            f.write(workflow)
    update_readme_table()
