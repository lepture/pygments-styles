import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def compile_sample(filename: str):
    lang = filename.split(".")[0]
    options = {"linespans": lang}
    if lang == 'javascript':
        options["hl_lines"] = [7, 15, 16, 17]
    elif lang == 'c':
        options["linenos"] = True
        options["hl_lines"] = [12, 13, 14]

    formatter = HtmlFormatter(**options)
    with open(os.path.join(ROOT_PATH, f"samples/{filename}"), encoding="utf-8") as f:
        text = f.read()
        lexer = get_lexer_by_name(lang, stripall=True)
        html = highlight(text, lexer, formatter)

    name = filename.replace(".sample", "")
    return (
        f'<div class="sample"><div class="sample-name">{name}</div>'
        f'<div class="sample-code">{html}</div></div>'
    )


def build_samples(style: str):

    samples_html = []
    filenames = sorted(os.listdir(os.path.join(ROOT_PATH, "samples")))
    for filename in filenames:
        if filename.endswith(".sample"):
            samples_html.append(compile_sample(filename))

    with open(os.path.join(ROOT_PATH, "scripts/templates/index.html"), encoding="utf-8") as f:
        template: str = f.read()
        template = template.replace("<!-- samples -->", "\n".join(samples_html))

    with open(os.path.join(ROOT_PATH, "scripts/templates/style.css"), encoding="utf-8") as f:
        css = f.read()

    formatter = HtmlFormatter(style=style)
    css += formatter.get_style_defs(".highlight")
    template = template.replace("<!-- style -->", f"<style>{css}</style>")
    return template


if __name__ == "__main__":
    import sys

    html = build_samples(sys.argv[1])
    with open(os.path.join(ROOT_PATH, ".venv/demo.html"), "w") as f:
        f.write(html)
