from pygments.style import Style
from ._gruvbox import DarkColors, build_token_styles


class GruvboxDarkMediumStyle(Style):
    """
    Pygments style based on the Gruvbox Dark (medium) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-dark-medium"

    background_color = DarkColors.bg
    highlight_color = DarkColors.bg1
    line_number_color = DarkColors.gray

    styles = build_token_styles(DarkColors)
