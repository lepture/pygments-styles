from pygments.style import Style
from ._gruvbox import LightColors, build_token_styles


class GruvboxLightMediumStyle(Style):
    """
    Pygments style based on the Gruvbox Light (medium) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-light-medium"

    background_color = LightColors.bg
    highlight_color = LightColors.bg1
    line_number_color = LightColors.gray

    styles = build_token_styles(LightColors)
