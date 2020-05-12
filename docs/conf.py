# -*- coding: utf-8 -*-

import os
import sys
import time

from wg_package.version import get_version


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = '{{cookiecutter.project_slug}}'
copyright = '2020-{}, {{cookiecutter.author}}'.format(time.strftime('%Y'))
author = '{{cookiecutter.author}}'


# This is working only for one-version rtd. i.e. only on `latest` rtd version.
# Hard code for RTD build.
# No other ways were found to send this info to the RTD build.
# Please change according to the target branch.
os.environ['BUILD_BRANCH'] = 'refs/heads/develop'

_version = get_version()
# The full project version, used as the replacement for |release| and e.g. in the HTML templates.
release = _version.py

# The major project version, used as the replacement for |version|.
version = '{}.{}'.format(_version.major, _version.minor)


# -- General configuration ---------------------------------------------------

needs_sphinx = '2.2'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'm2r'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

language = 'ru'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Magic to run sphinx-apidoc automatically -----------------------------

# See https://github.com/rtfd/readthedocs.org/issues/1139 on which this is based.

def run_apidoc(_):
    from sphinx.ext import apidoc
    apidoc.main(['-f', '-T', '-M', '-o', '.', '../{{cookiecutter.project_slug}}',])


def setup(app):
    """Override sphinx setup to trigger sphinx-apidoc."""
    app.connect('builder-inited', run_apidoc)