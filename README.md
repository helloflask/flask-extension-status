# Flask Extension Status

Hello, Flask developers!

This is a project to monitor the status of Flask extensions. In the [Extension status](#extension-status) table, each extension has a build badge to show whether it can be built with the latest Flask and Python. Feel free to add new extensions or update the info of existing extensions (see [How to add an extension?](#how-to-add-an-extension) for details)

Want to help? You can just check the [GitHub Actions](https://github.com/greyli/flask-extension-status/actions) for the failed extensions and try to fix the issues. Welcome to dicuss in the [Discussions](https://github.com/greyli/flask-extension-status/discussions) section. No matter you want to share some notes
for [common compatibility issues](https://github.com/greyli/flask-extension-status/discussions/categories/notes) or you want to [ask for help](https://github.com/greyli/flask-extension-status/discussions/categories/q-a), we are glad to hear from you!

❤️ If you managed to save an extension, don't hesitate to [share with us](https://github.com/greyli/flask-extension-status/discussions/categories/show-and-tell)!

For a project that is abandoned/dead, we will remove it from the table and list them in the [Unmaintained extensions and alternatives](#unmaintained-extensions-and-alternatives) section. If you have an extension but don't have time to maintain it, you can consider donating it to the [pallets-eco organzation](https://github.com/pallets-eco). Thank you.

**Let's make Flask ecosystem better together!**


## Extension status

<!-- TABLE_START -->

| Extension Repository | Latest version  |  Downloads | Build with latest Flask (3.x) and Python (3.12.x) |
| -------------------- | --------------- | ---------- | ------------------------------------------------- |
| [helloflask/bootstrap-flask](https://github.com/helloflask/bootstrap-flask) | ![PyPI - Version](https://img.shields.io/pypi/v/bootstrap-flask) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/bootstrap-flask?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/bootstrap-flask.yml/badge.svg) |
| [jmcarp/flask-apispec](https://github.com/jmcarp/flask-apispec) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-apispec) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-apispec?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-apispec.yml/badge.svg) |
| [miracle2k/flask-assets](https://github.com/miracle2k/flask-assets) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-assets) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-assets?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-assets.yml/badge.svg) |
| [helloflask/flask-avatars](https://github.com/helloflask/flask-avatars) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-avatars) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-avatars?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-avatars.yml/badge.svg) |
| [python-babel/flask-babel](https://github.com/python-babel/flask-babel) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-babel) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-babel?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-babel.yml/badge.svg) |
| [pallets-eco/flask-caching](https://github.com/pallets-eco/flask-caching) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-caching) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-caching?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-caching.yml/badge.svg) |
| [helloflask/flask-ckeditor](https://github.com/helloflask/flask-ckeditor) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-ckeditor) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-ckeditor?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-ckeditor.yml/badge.svg) |
| [corydolphin/flask-cors](https://github.com/corydolphin/flask-cors) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-cors) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-cors?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-cors.yml/badge.svg) |
| [pallets-eco/flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-debugtoolbar) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-debugtoolbar?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-debugtoolbar.yml/badge.svg) |
| [maxcountryman/flask-login](https://github.com/maxcountryman/flask-login) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-login) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-login?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-login.yml/badge.svg) |
| [waynerv/flask-mailman](https://github.com/waynerv/flask-mailman) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-mailman) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-mailman?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-mailman.yml/badge.svg) |
| [marshmallow-code/flask-marshmallow](https://github.com/marshmallow-code/flask-marshmallow) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-marshmallow) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-marshmallow?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-marshmallow.yml/badge.svg) |
| [miguelgrinberg/flask-migrate](https://github.com/miguelgrinberg/flask-migrate) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-migrate) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-migrate?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-migrate.yml/badge.svg) |
| [miguelgrinberg/flask-moment](https://github.com/miguelgrinberg/flask-moment) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-moment) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-moment?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-moment.yml/badge.svg) |
| [MongoEngine/flask-mongoengine](https://github.com/MongoEngine/flask-mongoengine) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-mongoengine) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-mongoengine?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-mongoengine.yml/badge.svg) |
| [plangrid/flask-rebar](https://github.com/plangrid/flask-rebar) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-rebar) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-rebar?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-rebar.yml/badge.svg) |
| [flask-restful/flask-restful](https://github.com/flask-restful/flask-restful) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-restful) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-restful?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-restful.yml/badge.svg) |
| [python-restx/flask-restx](https://github.com/python-restx/flask-restx) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-restx) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-restx?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-restx.yml/badge.svg) |
| [miguelgrinberg/Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-socketio) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-socketio?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-socketio.yml/badge.svg) |
| [pallets/flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-sqlalchemy) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-sqlalchemy?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-sqlalchemy.yml/badge.svg) |
| [jarus/flask-testing](https://github.com/jarus/flask-testing) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-testing) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-testing?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-testing.yml/badge.svg) |
| [fedora-copr/flask-whooshee](https://github.com/fedora-copr/flask-whooshee) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-whooshee) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-whooshee?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-whooshee.yml/badge.svg) |
| [flask-wtf/flask-wtf](https://github.com/flask-wtf/flask-wtf) | ![PyPI - Version](https://img.shields.io/pypi/v/flask-wtf) | ![PyPI - Downloads](https://img.shields.io/pypi/dm/flask-wtf?color=darkgrey) | ![build](https://github.com/greyli/flask-extension-status/actions/workflows/flask-wtf.yml/badge.svg) |

<!-- TABLE_END -->


## Unmaintained extension and alternatives

| Unmaintained Extension  |  Recommended Alternatives |
| ----------------------- | ------------------------- |
| [mattupstate/flask-mail](https://github.com/mattupstate/flask-mail) | [waynerv/flask-mailman](https://github.com/waynerv/flask-mailman) |
| [thadeusb/flask-cache](https://github.com/thadeusb/flask-cache) | [pallets-eco/flask-caching](https://github.com/pallets-eco/flask-caching) |
| [noirbizarre/flask-restplus](https://github.com/noirbizarre/flask-restplus) | [python-restx/flask-restx](https://github.com/python-restx/flask-restx) |
| [mbr/flask-bootstrap](https://github.com/mbr/flask-bootstrap) | [helloflask/bootstrap-flask](https://github.com/helloflask/bootstrap-flask) |


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
