import pygments_styles

project = "Pygments Styles"
copyright = "Copyright &copy; 2025, Hsiaoming Yang"
author = "Hsiaoming Yang"

version = pygments_styles.__version__
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinx_design",
    "sphinx_iconify",
]
todo_include_todos = True
iconify_script_url = ""
sitemap_excludes = ["404/"]

extlinks = {
    "pull": ("https://github.com/lepture/pygments-styles/pull/%s", "pull request #%s"),
    "issue": ("https://github.com/lepture/pygments-styles/issues/%s", "issue #%s"),
}

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_public"]

html_title = project
html_theme = "shibuya"
html_baseurl = "https://pygments-styles.org/"
sitemap_url_scheme = "{link}"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
}

html_favicon = "_static/icon.svg"

html_theme_options = {
    "accent_color": "brown",
    "logo_target": "/",
    "light_logo": "_static/light-logo.svg",
    "dark_logo": "_static/dark-logo.svg",
    "twitter_creator": "lepture",
    "twitter_site": "lepture",
    "discussion_url": "https://github.com/lepture/pygments-styles/discussions",
    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/pygments-styles",
    "carbon_ads_code": "CE7DKK3W",
    "carbon_ads_placement": "pygments-styles",
    "globaltoc_expand_depth": 1,
    "nav_links": [
        {
            "title": "Sponsor me",
            "url": "https://github.com/sponsors/lepture",
            "external": True,
        },
    ],
}


html_context = {
    "source_type": "github",
    "source_user": "lepture",
    "source_repo": "pygments-styles",
    "buysellads_code": "CE7DKK3M",
    "buysellads_placement": "pygments-styles",
    "buysellads_container_selector": ".yue > section > section",
}
