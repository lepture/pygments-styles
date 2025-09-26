from pygments.style import Style
from ._gruvbox import LightColors, build_token_styles


class GruvboxLightSoftStyle(Style):
    """
    Pygments style based on the Gruvbox Light (soft) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-light-soft"

    background_color = LightColors.bg0_s
    highlight_color = LightColors.bg2
    line_number_color = LightColors.gray

    styles = build_token_styles(LightColors)
