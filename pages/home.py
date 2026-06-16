from pathlib import Path
import flet as ft

BG_DARK = "#0f172a"      
SURFACE_CARD = "#1e293b"  
ACCENT = "#38bdf8"        
TEXT_MAIN = "#f8fafc"     
MUTED = "#94a3b8"         

PROFILE_PHOTO = Path("assets/images/profile-original.jpg.jpeg")

def _social_button(label: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(label, size=12, weight=ft.FontWeight.W_600, color=TEXT_MAIN),
        width=36,
        height=36,
        bgcolor=SURFACE_CARD,
        border=ft.border.all(1, "#334155"),
        border_radius=8,  
        alignment=ft.Alignment(0, 0), 
    )


def _resume_button() -> ft.ElevatedButton:
    return ft.ElevatedButton(
        "Download CV",
        icon=ft.Icons.DASHBOARD_CUSTOMIZE_ROUNDED,
        style=ft.ButtonStyle(
            bgcolor=ACCENT,
            color=BG_DARK,  
            padding=ft.padding.symmetric(horizontal=22, vertical=14),
            shape=ft.RoundedRectangleBorder(radius=8),  
            elevation=4,
        ),
    )

def _profile_content() -> ft.Control:
    if PROFILE_PHOTO.exists():
        return ft.Image(
            src=f"images/{PROFILE_PHOTO.name}",
            fit="cover",
            width=280,
            height=280,
            border_radius=16,  
        )

    return ft.Column(
        controls=[
            ft.Icon(ft.Icons.CODE_ROUNDED, size=72, color=ACCENT),
            ft.Text(
                "NATANGWE", 
                size=20, 
                weight=ft.FontWeight.W_800, 
                color=TEXT_MAIN
            ),
        ],
        spacing=6,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )

def _hero_copy() -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text("HELLO, I'M", size=14, weight=ft.FontWeight.W_700, color=ACCENT),
            ft.Text("Natangwe", size=52, weight=ft.FontWeight.W_900, color=TEXT_MAIN),
            ft.Row(
                controls=[
                    ft.Text(
                        "And I'm an",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=TEXT_MAIN,
                    ),
                    ft.Text(
                        "Engineering student",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ACCENT,
                    ),
                ],
                spacing=8,
                wrap=True,
            ),
            ft.Container(height=4),  
            ft.Text(
                "Hi, I'm Natangwe Tuyapeni, I'm a mechanical engineering student "
                "specializing in python,JavaScript and Matlab "
                ",This portfolio serves as a weekly log of my contributions to my computer programmingI project.",
                size=14,
                color=MUTED,
                width=490,
            ),
            ft.Container(height=6),
            ft.Row(
                controls=[
                    _social_button("f"),
                    _social_button("X"),
                    _social_button("IG"),
                    _social_button("in"),
                ],
                spacing=10,
            ),
            ft.Container(height=6),
            _resume_button(),
        ],
        spacing=12,
        alignment=ft.MainAxisAlignment.CENTER,
    )


def _profile_glow() -> ft.Container:
    return ft.Container(
        content=_profile_content(),
        width=296,
        height=296,
        border_radius=20,
        alignment=ft.Alignment(0, 0),  # Reverted to your local environment syntax
        bgcolor=SURFACE_CARD,
        border=ft.border.all(2, "#334155"),
        shadow=ft.BoxShadow(
            blur_radius=30,
            spread_radius=-5,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 15),
        ),
    )


def view(_: ft.Page) -> ft.Container:
    return ft.Container(
        bgcolor=BG_DARK,
        padding=ft.padding.only(left=64, right=64, top=42, bottom=64),
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=_hero_copy(),
                    col={"xs": 12, "md": 6},
                    padding=ft.padding.only(top=24, bottom=24),
                ),
                ft.Container(
                    content=_profile_glow(),
                    col={"xs": 12, "md": 6},
                    alignment=ft.Alignment(0, 0),  
                    padding=ft.padding.only(top=24, bottom=24),
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=32,
            run_spacing=32,
        ),
    )