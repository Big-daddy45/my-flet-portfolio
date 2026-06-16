import flet as ft


ROUTES = ["/", "/projects", "/certificates", "/vlogs"]
LABELS = {
    "/": "Home",
    "/projects": "Portfolio",
    "/certificates": "Skills",
    "/vlogs": "Contact",
}

# Matching the home page smart tech theme
ACCENT = "#38bdf8"        # Sharp technical cyan
TEXT_MAIN = "#f8fafc"     # Off-white crisp text


def _nav_link(page: ft.Page, route: str, active_route: str) -> ft.TextButton:
    active = route == active_route

    return ft.TextButton(
        content=ft.Text(
            LABELS[route],
            size=12,
            weight=ft.FontWeight.W_600 if active else ft.FontWeight.W_500,
            color=ACCENT if active else "#f4f4f4",
        ),
        on_click=lambda _: page.go(route),
        style=ft.ButtonStyle(
            overlay_color=ft.Colors.with_opacity(0.08, ft.Colors.CYAN),
            padding=ft.padding.symmetric(horizontal=6, vertical=4),
        ),
    )


def build_navbar(page: ft.Page, active_route: str) -> ft.Container:
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=42, vertical=24),
        content=ft.Row(
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan("Natangwe", style=ft.TextStyle(color=ACCENT)),
                        ft.TextSpan(" Tuyapeni", style=ft.TextStyle(color="#ffffff")),
                    ],
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(
                    controls=[_nav_link(page, route, active_route) for route in ROUTES]
                    + [
                        ft.IconButton(
                            icon=ft.Icons.SETTINGS_OUTLINED,
                            icon_color="#f4f4f4",
                            tooltip="Settings",
                        )
                    ],
                    spacing=2,
                    wrap=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True,
        ),
    )