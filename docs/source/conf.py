# Configuration file for the Sphinx documentation builder.
# from dashtools.version import __version__

__version__ = '1.8.0'
# -- Project information

project = 'DashTools'
author = 'Andrew Hossack'

version = __version__
release = __version__

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'agogo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
