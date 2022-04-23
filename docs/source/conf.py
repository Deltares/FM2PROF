# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# add docs path to python sys.path to allow autodoc-ing a test_py_module
import os
import sys
sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "FM2PROF"
copyright = "2022 Deltares"
author = "Koen D. Berends"

# The full version, including alpha/beta/rc tags
release = "1.4.3"

# To enable to inject project name in source
import fm2prof
from fm2prof import __version__
from fm2prof.IniFile import IniFile

rst_epilog = f"""

.. |project| replace:: {project} 
.. |release| replace:: {release}
"""

for pname, ptype, phint, pvalue in IniFile().iter_parameters():

    if pvalue == "":

        pvalue = "Undefined"

    rst_epilog += f".. |default_{pname.lower()}| replace:: {pvalue}\n"

    rst_epilog += f".. |type_{pname.lower()}| replace:: {ptype}\n"

    rst_epilog += f".. |hint_{pname.lower()}| replace:: {phint}\n"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.images",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_immaterial"
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx_docs": ("https://www.sphinx-doc.org/en/master", None),
}

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- sphinx_immaterial.keys extension options
#
# optional key_map for example purposes
keys_map = {"my-special-key": "Awesome Key", "git": ""}

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]
html_css_files = ["stylesheets/extra.css"]
html_last_updated_fmt = ""
html_title = "FM2PROF Manual"
html_favicon = "_static/favicon.ico"  # colored version of material/bookshelf.svg
html_logo = "_static/logo_deltares.png"  # from https://gifer.com/en/Ybin

# -- HTML theme specific settings ------------------------------------------------

extensions.append("sphinx_immaterial")
html_theme = "sphinx_immaterial"

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/git-alt",
    },
    "site_url": "https://deltares.github.io/fm2prof/",
    "repo_url": "https://github.com/deltares/fm2prof/",
    "repo_name": "Fm2Prof",
    "repo_type": "github",
    "edit_uri": "blob/main/docs",
    # "google_analytics": ["UA-XXXXX", "auto"],
    "globaltoc_collapse": True,
    "globaltoc_includehidden": True,
    "features": [
        "navigation.expand",
        #"navigation.tabs",
        #"toc.integrate",
        "navigation.sections",
        #"navigation.instant",
        #"header.autohide",
        "navigation.top",
        #"navigation.tracking",
        #"search.highlight",
        #"search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "deltares",
            "primary": "indigo",
            "accent": "deep-orange",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo",
            "accent": "yellow",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://sphinx-immaterial.rtfd.io",
            "title": "ReadTheDocs",
            "aliases": [],
        },
        {
            "version": "https://jbms.github.io/sphinx-immaterial",
            "title": "Github Pages",
            "aliases": [],
        },
    ],
    "toc_title_is_page_title": True,
}  # end html_theme_options

# ---- Other documentation options -------------------------

todo_include_todos = True

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#%s",
        "",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/roles.html#%s", ""),
    "dudir": ("http://docutils.sourceforge.net/docs/ref/rst/directives.html#%s", ""),
}


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
