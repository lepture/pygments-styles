from pygments.style import Style
from ._gruvbox import LightColors, build_token_styles


class GruvboxLightHardStyle(Style):
    """
    Pygments style based on the Gruvbox Light (hard) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-light-hard"

    background_color = LightColors.bg0_h
    highlight_color = LightColors.bg1
    line_number_color = LightColors.gray

    styles = build_token_styles(LightColors)
