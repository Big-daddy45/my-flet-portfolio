import flet as ft

from components.navbar import build_navbar
from pages import certificates, home, projects

ROUTES = {
    "/": home.view,
    "/projects": projects.view,
    "/certificates": certificates.view,
}


def main(page: ft.Page) -> None:
    page.title = "Natangwe's Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "#151515"
    page.scroll = ft.ScrollMode.AUTO
    page.window_min_width = 360
    page.window_min_height = 640

    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.BLUE,
        visual_density=ft.VisualDensity.COMFORTABLE,
    )

    def render_route() -> None:
        route = page.route if page.route in ROUTES else "/"
        page.navigation_bar = None
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Column(
                    controls=[
                        build_navbar(page, route),
                        ROUTES[route](page),
                    ],
                    spacing=0,
                ),
                bgcolor="#151515",
                expand=True,
            )
        )
        page.update()

    def route_change(_: ft.RouteChangeEvent) -> None:
        render_route()

    # 1. Listen for future route changes (clicking navbar links)
    page.on_route_change = route_change
    
    # 2. FIX: Explicitly build and show the landing page right now on startup
    render_route()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")