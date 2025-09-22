import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def compile_sample(filename: str, cssclass: str='highlight'):
    lang = filename.split(".")[0]
    options = {"linespans": lang, "cssclass": cssclass}
    if lang == "javascript":
        options["hl_lines"] = [7, 15, 16, 17]
    elif lang == "c":
        options["linenos"] = True
        options["hl_lines"] = [12, 13, 14]

    formatter = HtmlFormatter(**options)
    with open(os.path.join(ROOT_PATH, f"samples/{filename}"), encoding="utf-8") as f:
        text = f.read()
        lexer = get_lexer_by_name(lang, stripall=True)
        html = highlight(text, lexer, formatter)

    return (
        f'<div class="sample" data-lang="{lang}"><div class="sample-name">{lang}</div>'
        f'<div class="sample-code">{html}</div></div>'
    )


def compile_samples(cssclass: str='highlight'):
    samples_html = []
    filenames = sorted(os.listdir(os.path.join(ROOT_PATH, "samples")))
    for filename in filenames:
        if filename.endswith(".sample"):
            samples_html.append(compile_sample(filename, cssclass))
    return "\n".join(samples_html)


def build_samples_select():
    html = '<div class="samples-select">'
    filenames = sorted(os.listdir(os.path.join(ROOT_PATH, "samples")))
    html += (
        '<div class="samples-select-lang">'
        '<label for="samples-select-lang">Language</label>'
        '<select id="samples-select-lang">'
    )
    for filename in filenames:
        if filename.endswith(".sample"):
            lang = filename.replace(".sample", "")
            if lang == 'python':
                html += f'<option value="{lang}" selected>{lang}</option>'
            else:
                html += f'<option value="{lang}">{lang}</option>'

    html += '</select></div>'
    filenames = sorted(os.listdir(os.path.join(ROOT_PATH, "src/pygments_styles")))
    html += (
        '<div class="samples-select-style">'
        '<label for="samples-select-style">Style</label>'
        '<select id="samples-select-style">'
    )

    css = ''
    for name in filenames:
        if name.endswith('.py') and not name.startswith('__'):
            style = name.replace('_', '-').replace('.py', '')
            if style == 'one-dark-pro':
                html += f'<option value="{style}" selected>{style}</option>'
            else:
                html += f'<option value="{style}">{style}</option>'

            formatter = HtmlFormatter(style=style, cssclass=style)
            css += formatter.get_style_defs(f".{style}")

    html += '</select></div></div>\n'
    with open(os.path.join(ROOT_PATH, "docs/_static/pygments-styles.css"), "w") as f:
        f.write(css)

    with open(os.path.join(ROOT_PATH, "docs/_templates/selector.html"), "w") as f:
        f.write(html)


def build_docs_samples():
    build_samples_select()
    html = compile_samples('one-dark-pro')
    with open(os.path.join(ROOT_PATH, "docs/_templates/samples.html"), "w") as f:
        f.write(html)



def debug_samples(style: str):
    samples_html = compile_samples()
    with open(
        os.path.join(ROOT_PATH, "scripts/templates/index.html"), encoding="utf-8"
    ) as f:
        template: str = f.read()
        template = template.replace("<!-- samples -->", samples_html)

    with open(
        os.path.join(ROOT_PATH, "scripts/templates/style.css"), encoding="utf-8"
    ) as f:
        css = f.read()

    formatter = HtmlFormatter(style=style)
    css += formatter.get_style_defs(".highlight")
    template = template.replace("<!-- style -->", f"<style>{css}</style>")
    return template


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        build_docs_samples()
    else:
        style = sys.argv[1]
        html = debug_samples(style)
        with open(os.path.join(ROOT_PATH, ".venv/demo.html"), "w") as f:
            f.write(html)
