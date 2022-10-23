import platform
# OS Identification
platform_name = platform.system()  # Windows, Darwin, Linux

project = 'my project'
copyright = 'Shunya Sasaki'
author = 'Shunya Sasaki'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinxcontrib.blockdiag']
language = 'ja'
html_theme = 'sphinx_material'
html_static_path = ['_static']

# blockdiag
blockdiag_html_image_format = 'SVG'
blockdiag_html_image_format = 'SVG'