:description: How to use Pygments styles with Sphinx documentation.

Sphinx
=======

Sphinx uses Pygments_ for syntax highlighting in code blocks. Pygments is
a popular library for code coloring, supporting a wide range of programming
languages and styles.

Each Sphinx theme comes with a default Pygments style, which determines how
code blocks are rendered.

This means that when you select a theme, it automatically applies its own
color scheme to all code examples.

.. _Pygments: https://pygments.org/

Configuration
-------------

If you want to customize the appearance of code blocks, you can override the
default Pygments style by specifying your preferred styles in ``conf.py``.

For example:

.. code-block:: python
    :caption: conf.py

    pygments_style = "one-light"
    pygments_dark_style = "one-dark-pro"

This allows you to maintain your chosen theme while adapting code highlighting to
your personal preferences or to better match your project’s design.
