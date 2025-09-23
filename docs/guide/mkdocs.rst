:description: Using Pygments for code highlighting in MkDocs.

MkDocs
======

MkDocs does not enable Pygments by default.

However, you can activate Pygments syntax highlighting
by enabling the appropriate Markdown extensions.

Configuration
-------------

You can enable Pygments syntax highlighting by using the
Markdown extension ``pymdownx.highlight`` and setting
``use_pygments: true``.

.. code-block:: yaml
    :caption: mkdocs.yml

    markdown_extensions:
      - pymdownx.superfences
      - pymdownx.highlight:
          use_pygments: true

Additionally, to enable syntax highlighting for Markdown fenced
code blocks, you must include the ``pymdownx.superfences``
extension.

Disable highlightjs
-------------------

By default, MkDocs uses ``Highlight.js`` for code highlighting.
To use Pygments instead, you must first disable ``Highlight.js``.

.. code-block:: yaml
    :caption: mkdocs.yml
    :emphasize-lines: 4

    theme:
      name: mkdocs
      locale: en
      highlightjs: false

Adding CSS
----------

Unlike Sphinx, MkDocs does not automatically include Pygments CSS styles.
To enable proper code highlighting, you need to add the CSS file manually.

Step 1: Generate the Pygments CSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose a Pygments style and generate the corresponding CSS file.
For example, to generate CSS using the ``github-light-default`` style:

.. code-block:: bash

    pygmentize -S github-light-default -f html -a .highlight > css/pygments.css

Step 2: Include the CSS in MkDocs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the generated CSS file to your MkDocs configuration so that it is included in your site:

.. code-block:: yaml
    :caption: mkdocs.yml

    extra_css:
      - css/pygments.css

Make sure to place the CSS file in the correct path (e.g., ``docs/css/pygments.css``) so that
MkDocs can find it.
