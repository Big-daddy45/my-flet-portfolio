import flet as ft


def section_title(title: str, subtitle: str | None = None) -> ft.Column:
    controls: list[ft.Control] = [
        ft.Text(
            title,
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#ffffff",
        )
    ]

    if subtitle:
        controls.append(
            ft.Text(
                subtitle,
                size=15,
                color="#b8b8c2",
            )
        )

    return ft.Column(controls=controls, spacing=6)


def info_card(
    title: str,
    body: str,
    icon: str = ft.Icons.STAR_OUTLINE,
    accent: str = ft.Colors.TEAL,
    footer: str | None = None,
) -> ft.Container:
    controls: list[ft.Control] = [
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Icon(icon, color=ft.Colors.WHITE, size=22),
                    bgcolor=accent,
                    width=42,
                    height=42,
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                ),
                ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color="#ffffff",
                    expand=True,
                ),
            ],
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.Text(body, size=14, color="#c9c9d1"),
    ]

    if footer:
        controls.append(
            ft.Text(
                footer,
                size=12,
                weight=ft.FontWeight.W_500,
                color=accent,
            )
        )

    return ft.Container(
        content=ft.Column(controls=controls, spacing=14),
        padding=18,
        bgcolor="#202024",
        border=ft.border.all(1, "#34343a"),
        border_radius=8,
        shadow=ft.BoxShadow(
            blur_radius=12,
            spread_radius=0,
            color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
        expand=True,
    )


def chip(label: str, color: str = ft.Colors.TEAL) -> ft.Container:
    return ft.Container(
        content=ft.Text(label, size=12, weight=ft.FontWeight.W_500, color="#ffffff"),
        padding=ft.padding.symmetric(horizontal=10, vertical=6),
        border=ft.border.all(1, ft.Colors.with_opacity(0.45, color)),
        border_radius=20,
        bgcolor=ft.Colors.with_opacity(0.18, color),
    )
