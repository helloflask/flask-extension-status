# Flask Extension Status

*Let's hope the CI of this repository will pass someday.*

It's a status dashboard for Flask extension. In the [Extension status](#extension-status) table, each extension has a build badge to show whether it can be built with the latest Flask version. Feel free to add new extensions or update the info of existing extensions (see [How to add an extension?](#how-to-add-an-extension) for details)

For a project that is not maintained anymore, we will list them in the [Unmaintained extension and alternatives](#unmaintained-extension-and-alternatives) section and provide some alternatives. If you have a extension but don't have time to maintain it, you can consider donating it to the [pallets-eco organzation](https://github.com/pallets-eco).

Want to help a Flask extension? Check the [What can I do to help?](#what-can-i-do-to-help) section. Let's make Flask ecosystem better together!

## Extension status

<!-- TABLE_START -->

| Extension Repository | Latest version  |  Downloads | Build with latest Flask |
| -------------------- | --------------- | ---------- | ----------------------- |
| [helloflask/bootstrap-flask](https://github.com/helloflask/bootstrap-flask) | ![PyPI - Version](https://img.shields.io/pypi/v/bootstrap-flask) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/bootstrap-flask?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/bootstrap-flask.yml/badge.svg) |
| [helloflask/flask-ckeditor](https://github.com/helloflask/flask-ckeditor) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-ckeditor) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-ckeditor?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-ckeditor.yml/badge.svg) |
| [pallets-eco/flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-debugtoolbar) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-debugtoolbar?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-debugtoolbar.yml/badge.svg) |
| [maxcountryman/flask-login](https://github.com/maxcountryman/flask-login) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-login) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-login?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-login.yml/badge.svg) |
| [waynerv/flask-mailman](https://github.com/waynerv/flask-mailman) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-mailman) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-mailman?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-mailman.yml/badge.svg) |

<!-- TABLE_END -->

## How to add an extension?

Clone the repo and install dependencies:

```bash
git clone https://github.com/greyli/flask-extension-status
cd flask-extension-status
pip install -r requirements.txt
```

Add the extension info to `extensions.yml`:

```yaml
flask-foo:  # PyPI package name
  repo: github_username/repo_name  # GitHub repository
  init_string: 'from flask_foo import Foo; Foo(app)'  # extension initialization
```

Then run:

```bash
python gen.py
```

Commit and push the changes, then create a pull request.

## What can I do to help?

## Common compatibility issues

## Unmaintained extension and alternatives
