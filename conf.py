# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('src/communicity_toolbox/toolbox/'))
sys.path.insert(0, os.path.abspath('src/communicity_toolbox/'))
sys.path.insert(0, os.path.abspath('src/communicity_toolbox/docs'))
sys.path.insert(0, os.path.abspath('src/communicity_toolbox/docs/DataModels'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Toolbox'
copyright = '2023, Edgar Gracia Larrosa'
author = 'Edgar Gracia Larrosa'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx-jsonschema',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autoclass_content = 'both' # Both the class’ and the __init__ method’s docstring are concatenated and inserted. 

myst_enable_extensions = ["colon_fence"]
myst_ref_domains=("std", "py")

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # 'alabaster'
html_static_path = ['_static']
