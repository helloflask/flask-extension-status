# Flask Extension Status

## Add new extension

Clone the repo and install dependencies:

```bash
git clone https://github.com/greyli/flask-extension-status
cd flask-extension-status
pip install -r requirements.txt
```

Add the extension info to `extensions.yml`:
    
```yaml
flask-foo:
  repo: github_username/repo_name
  import_string: 'the import string of your extension'
```

Then run:

```bash
python gen.py
```

Commit and push the changes, then create a pull request.

## Extension health dashboard

<!-- TABLE_START -->

| Extension Repository | Latest version  |  Downloads | Build with latest Flask (3.x) |
| -------------------- | --------------- | ---------- | ----------------------------- |
| [helloflask/bootstrap-flask](https://github.com/helloflask/bootstrap-flask) | ![PyPI - Version](https://img.shields.io/pypi/v/bootstrap-flask) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/bootstrap-flask?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/bootstrap-flask.yml/badge.svg) |
| [helloflask/flask-ckeditor](https://github.com/helloflask/flask-ckeditor) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-ckeditor) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-ckeditor?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-ckeditor.yml/badge.svg) |
| [pallets-eco/flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-debugtoolbar) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-debugtoolbar?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-debugtoolbar.yml/badge.svg) |
| [maxcountryman/flask-login](https://github.com/maxcountryman/flask-login) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-login) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-login?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-login.yml/badge.svg) |
| [waynerv/flask-mailman](https://github.com/waynerv/flask-mailman) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-mailman) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-mailman?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-mailman.yml/badge.svg) |

<!-- TABLE_END -->

## About this project

## What can we do?

## Unmaintained extension and alternatives
