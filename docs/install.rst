:description: Here is the guide on how to install Pygments Styles package.

.. _install:

Installation
============

.. rst-class:: lead

   Install the **pygments-styles** as a Python package.

----

``pygments-styles`` is a curated collection of Pygments_ styles,
derived from VS Code themes and carefully adapted with manual
improvements to ensure optimal compatibility with Pygments.

.. _Pygments: https://pygments.org/

package install
---------------

``pygments-styles`` is conveniently available as a Python package on
PyPI and can be easily installed using pip and uv.

.. tab-set::
    :class: outline

    .. tab-item:: :iconify:`devicon:pypi` pip

        .. code-block:: bash

            pip install pygments-styles

    .. tab-item:: :iconify:`material-icon-theme:uv` uv

        .. code-block:: bash

            uv add pygments-styles

requirements.txt
----------------

If you're tracking dependencies in ``requirements.txt``, you can create a separate
requirements file for your documentation, such as ``requirements-docs.txt``, and
add ``pygments-styles`` to that file to ensure it is included in your documentation
build.

pyproject.toml
--------------

If you're tracking dependencies in ``pyproject.toml``, just put it in:


.. code-block:: toml
    :caption: pyproject.toml

    dependencies = [
        # ... other packages
        "pygments-styles",
    ]
