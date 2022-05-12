"""Sphinx configuration."""
project = "Python Test Project"
author = "Willi Meierhof"
copyright = "2022, Willi Meierhof"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
