# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'STEM VN Wiki'
copyright = '2022, STEMVN'
author = 'STEM VN'

release = '2.0'
version = '2.0.0'

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

html_theme = 'sphinx_rtd_theme' # pip3 install sphinx_rtd_theme

html_logo = 'images/white_logo.png'

html_style = 'css/stemvn.css'

html_favicon = 'images/favicon.ico'

html_theme_options = {
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    # 'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # 'style_external_links': True,
    # 'vcs_pageview_mode': '',
    'style_nav_header_background': '#ff7337',
    # Toc options

    'collapse_navigation': True,
    'sticky_navigation': True,
    # 'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,

    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
}

html_context  = {
   'display_github' : True ,
   'github_user' : 'username' ,
   'github_repo' : 'reponame' ,
   'github_version' : 'master' 
}

html_static_path = ['_static']

html_css_files = [
    'custom.css'
]

epub_show_urls = 'footnote'
