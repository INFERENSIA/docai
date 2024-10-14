# from typing import Iterable
#
# from gradio.themes import Soft
# from gradio.themes.utils import colors, fonts, sizes
#
# gray = colors.Color(
#     name="dark",
#     c50="#f9fafb",
#     c100="#edeef0",
#     c200="#e1e2e6",
#     c300="#d5d6dd",
#     c400="#cacbd5",
#     c500="#acadb7",
#     c600="#313138",
#     c700="#25252b",
#     c800="#19191e",
#     c900="#0d0d11",
#     c950="#010104",
# )
#
# err_txt = "#f05656"
# gradient = "linear-gradient(90deg, *primary_400 20%, *secondary_500 80%)"
# gradient_muted = "linear-gradient(90deg, *primary_500 20%, *secondary_600 80%)"
#
# err_dark = "rgba(228, 98, 98, 1)"
# err_dark_muted = "rgba(228, 98, 98, 0.75)"
#
# err = "rgba(255, 93, 93, 1)"
# err_muted = "rgba(237, 80, 80, 1)"
#
#
# common = dict(
#     # element colours
#     color_accent="*primary_400",
#     # shadows
#     shadow_drop="0 0px 5px 1px rgb(0 0 0 / 0.05)",
#     shadow_drop_lg="0 0 10px 3px rgba(0 0 0 / 0.06)",
#     # layout atoms
#     block_label_margin="*spacing_xl",
#     block_label_padding="*spacing_xl",
#     block_label_shadow="none",
#     layout_gap="*spacing_xxl",
#     section_header_text_size="*text_lg",
#     # buttons
#     button_shadow="none",
#     button_shadow_active="*shadow_drop",
#     button_shadow_hover="none",
#     # button_large_radius="*radius_xxl",
#     # button_small_radius="*radius_xxl",
#     # -----
# )
# dark_mode = dict(
#     # body attributes
#     body_text_color_subdued_dark="*neutral_300",
#     # element colours
#     background_fill_secondary_dark="*neutral_950",
#     border_color_accent_dark="rgba(255,255,255,0)",
#     border_color_primary_dark="*neutral_600",
#     color_accent_soft_dark="*secondary_400",
#     # text
#     link_text_color_dark="*secondary_200",
#     link_text_color_active_dark="*secondary_300",
#     link_text_color_visited_dark="*secondary_400",
#     # layout atoms
#     block_label_background_fill_dark="*neutral_800",
#     block_label_border_width_dark="0px",
#     block_label_text_color_dark="*primary_200",
#     block_shadow_dark="none",
#     block_title_text_color_dark="*primary_200",
#     panel_border_width_dark="0px",
#     # component atoms
#     checkbox_background_color_selected_dark="*primary_400",
#     checkbox_border_color_focus_dark="*primary_400",
#     checkbox_border_color_selected_dark="*primary_500",
#     checkbox_label_background_fill_selected_dark="*primary_200",
#     checkbox_label_text_color_selected_dark="*neutral_700",
#     error_border_color_dark=err_dark,
#     error_text_color_dark="*neutral_100",
#     error_icon_color_dark=err_dark,
#     input_background_fill_dark="*neutral_600",
#     input_border_color_dark="*input_background_fill",
#     input_border_color_focus_dark="*input_background_fill",
#     input_placeholder_color_dark="*neutral_500",
#     loader_color_dark="*primary_200",
#     slider_color_dark="*primary_300",
#     stat_background_fill_dark="*secondary_100",
#     table_border_color_dark="*neutral_800",
#     table_even_background_fill_dark="*neutral_900",
#     table_odd_background_fill_dark="*neutral_800",
#     table_row_focus_dark="*neutral_600",
#     # buttons
#     button_primary_background_fill_dark=gradient,
#     button_primary_background_fill_hover_dark=gradient_muted,
#     button_secondary_background_fill_hover_dark="*neutral_700",
#     button_cancel_background_fill_dark=err_dark,
#     button_cancel_background_fill_hover_dark=err_dark_muted,
# )
# light_mode = dict(
#     background_fill_primary="*neutral_50",
#     background_fill_secondary="*neutral_50",
#     # body attributes
#     body_background_fill="*background_fill_primary",
#     body_text_color_subdued="*neutral_600",
#     border_color_accent="rgba(255,255,255,0)",
#     border_color_primary="*neutral_300",
#     color_accent_soft="*secondary_100",
#     # text
#     link_text_color="*secondary_400",
#     link_text_color_visited="*secondary_700",
#     # layout atoms
#     block_label_border_width="0px",
#     block_label_background_fill="white",
#     block_label_text_color="*primary_600",
#     block_shadow="none",
#     block_title_text_color="*primary_600",
#     panel_border_width="0px",
#     # component atoms
#     checkbox_background_color_selected="*primary_400",
#     checkbox_border_color_focus="*primary_400",
#     checkbox_border_color_selected="*primary_400",
#     checkbox_label_border_color="*primary_200",
#     error_background_fill="*background_fill_primary",
#     error_border_color=err_muted,
#     error_text_color="*neutral_800",
#     input_background_fill="*neutral_200",
#     input_border_color="*input_background_fill",
#     input_border_color_focus="*input_background_fill",
#     input_placeholder_color="*neutral_500",
#     loader_color="*primary_300",
#     slider_color="*primary_400",
#     stat_background_fill="*secondary_300",
#     table_even_background_fill="*neutral_100",
#     table_odd_background_fill="*neutral_300",
#     table_row_focus="*secondary_200",
#     # buttons
#     button_primary_background_fill=gradient_muted,
#     button_primary_background_fill_hover=gradient,
#     button_secondary_background_fill="*neutral_300",
#     button_secondary_background_fill_hover="*neutral_100",
#     button_cancel_background_fill=err_muted,
#     button_cancel_background_fill_hover=err,
#     button_cancel_text_color="*neutral_50",
# )
#
#
# class Kotaemon(Soft):
#     """
#     Official theme of Kotaemon.
#     Public version: https://huggingface.co/spaces/lone17/kotaemon
#     """
#
#     def __init__(
#         self,
#         *,
#         primary_hue: colors.Color | str = colors.emerald,
#         secondary_hue: colors.Color | str = colors.blue,
#         neutral_hue: colors.Color | str = gray,
#         spacing_size: sizes.Size | str = sizes.spacing_md,
#         radius_size: sizes.Size | str = sizes.radius_md,
#         text_size: sizes.Size | str = sizes.text_md,
#         font: fonts.Font
#         | str
#         | Iterable[fonts.Font | str] = (
#             fonts.GoogleFont("Quicksand"),
#             "ui-sans-serif",
#             "sans-serif",
#         ),
#         font_mono: fonts.Font
#         | str
#         | Iterable[fonts.Font | str] = (
#             fonts.GoogleFont("IBM Plex Mono"),
#             "ui-monospace",
#             "monospace",
#         ),
#     ):
#         super().__init__(
#             primary_hue=primary_hue,
#             secondary_hue=secondary_hue,
#             neutral_hue=neutral_hue,
#             spacing_size=spacing_size,
#             radius_size=radius_size,
#             text_size=text_size,
#             font=font,
#             font_mono=font_mono,
#         )
#         self.name = "kotaemons"
#         super().set(
#             **common,
#             **dark_mode,
#             **light_mode,
#         )








from typing import Iterable

from gradio.themes import Base
from gradio.themes.utils import colors, fonts, sizes

# Define custom colors
brand_blue = colors.Color(
    name="brand_blue",
    c50="#e6f3ff",
    c100="#ccebff",
    c200="#99d6ff",
    c300="#66c2ff",
    c400="#33adff",
    c500="#0099ff",
    c600="#007acc",
    c700="#005c99",
    c800="#003d66",
    c900="#001f33",
    c950="#000f1a",
)

brand_red = colors.Color(
    name="brand_red",
    c50="#ffe6e6",
    c100="#ffcccc",
    c200="#ff9999",
    c300="#ff6666",
    c400="#ff3333",
    c500="#ff0000",
    c600="#cc0000",
    c700="#990000",
    c800="#660000",
    c900="#330000",
    c950="#1a0000",
)

# Custom styles
common = dict(
    color_accent="*secondary_600",
    shadow_drop="0 2px 6px 0 rgba(0, 0, 0, 0.1)",
    shadow_drop_lg="0 4px 12px 0 rgba(0, 0, 0, 0.15)",
    block_label_margin="*spacing_sm",
    block_label_padding="*spacing_sm *spacing_md",
    block_label_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.05)",
    layout_gap="*spacing_xl",
    section_header_text_size="*text_lg",
    button_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1)",
    button_shadow_hover="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    button_shadow_active="inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)",
    button_large_radius="*radius_lg",
    button_small_radius="*radius_md",
)

light_mode = dict(
    # background_fill_primary="white",
    # background_fill_secondary="*neutral_50",
    # body_text_color="*neutral_900",
    # body_text_color_subdued="*neutral_700",
    # border_color_accent="*secondary_500",
    # border_color_primary="*neutral_200",
    # color_accent_soft="*secondary_100",
    # link_text_color="*secondary_700",
    # link_text_color_hover="*secondary_800",
    # link_text_color_visited="*secondary_900",
    # block_label_background_fill="*secondary_50",
    # block_label_text_color="*secondary_700",
    # block_title_text_color="*secondary_800",
    # checkbox_background_color_selected="*secondary_600",
    # checkbox_border_color_focus="*secondary_500",
    # checkbox_border_color_selected="*secondary_600",
    # input_background_fill="white",
    # input_border_color="*neutral_300",
    # input_border_color_focus="*secondary_500",
    # slider_color="*secondary_600",
    # button_primary_background_fill="*secondary_600",
    # button_primary_background_fill_hover="*secondary_700",
    # button_primary_text_color="white",
    # button_secondary_background_fill="white",
    # button_secondary_background_fill_hover="*neutral_100",
    # button_secondary_text_color="*secondary_700",
    # button_cancel_background_fill="*brand_red_500",
    # button_cancel_background_fill_hover="*brand_red_600",
    # button_cancel_text_color="white",
)

dark_mode = dict(
    background_fill_primary="*neutral_950",
    background_fill_secondary="*neutral_900",
    body_text_color="*neutral_100",
    body_text_color_subdued="*neutral_300",
    border_color_accent="*secondary_400",
    border_color_primary="*neutral_700",
    color_accent_soft="*secondary_900",
    link_text_color="*secondary_300",
    link_text_color_hover="*secondary_200",
    link_text_color_visited="*secondary_400",
    block_label_background_fill="*neutral_800",
    block_label_text_color="*secondary_200",
    block_title_text_color="*secondary_100",
    checkbox_background_color_selected="*secondary_400",
    checkbox_border_color_focus="*secondary_400",
    checkbox_border_color_selected="*secondary_500",
    input_background_fill="*neutral_800",
    input_border_color="*neutral_600",
    input_border_color_focus="*secondary_400",
    slider_color="*secondary_400",
    button_primary_background_fill="*secondary_500",
    button_primary_background_fill_hover="*secondary_400",
    button_primary_text_color="*neutral_950",
    button_secondary_background_fill="*neutral_800",
    button_secondary_background_fill_hover="*neutral_700",
    button_secondary_text_color="*secondary_200",
    button_cancel_background_fill="*brand_red_600",
    button_cancel_background_fill_hover="*brand_red_500",
    button_cancel_text_color="*neutral_100",
)

class Kotaemon(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = brand_blue,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.gray,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_md,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Roboto"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Roboto Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = "brand_theme"
        super().set(
            **common,
            **light_mode,
            **dark_mode,
        )

