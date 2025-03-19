import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Get version from package
try:
    from ConsoleM import __version__ as version
    release = version
except ImportError:
    release = '0.1.1'  # fallback version

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# Set up source and build directories
source_dir = os.path.abspath('.')
build_dir = os.path.abspath('_build')
api_dir = os.path.abspath('api')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ConsoleM'
copyright = '2025, Remi'
author = 'Remi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

# Template and static paths
templates_path = ['_templates']
html_static_path = ['_static']

# Files to exclude from build
exclude_patterns = [
    '_build',
    '_templates',
    '_static',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# -- Extension configuration ------------------------------------------------

# Autodoc configuration
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Output options
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
} 