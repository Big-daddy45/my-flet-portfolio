import os
import webbrowser
import flet as ft

from components.card import info_card, section_title

# Unified technical color system
BG_DARK = "#0f172a"        # Deep Slate/Midnight Blue
ACCENT = "#38bdf8"         # Sharp technical cyan

# Dynamic list showing your progress (5 Completed, 3 Pending)
CERTIFICATES = [
    {
        "title": "MATLAB Onramp",
        "body": "Core foundations of MATLAB syntax, array manipulation, data import, and visualization fundamentals.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.SCHOOL_OUTLINED,
        "accent": ACCENT,
        "url": "certificates/matlab_onramp.pdf",  # Removed leading slash for easier OS path joining
        "completed": True,
    },
    {
        "title": "Simulink Onramp",
        "body": "Basics of creating, modifying, and simulating graphical block diagrams for dynamic systems.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.SETTINGS_OUTLINED,
        "accent": ACCENT,
        "url": "certificates/simulink_onramp.pdf",
        "completed": True,
    },
    {
        "title": "App Building Onramp",
        "body": "Foundations of designing and coding interactive user interfaces and layouts within MATLAB App Designer.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.APPS_OUTLINED,
        "accent": ACCENT,
        "url": "certificates/app_building_onramp.pdf",
        "completed": True,
    },
    {
        "title": "Explore Data with MATLAB Plots",
        "body": "Advanced methods for customizing data visualizations, annotating plots, and exporting high-quality graphics.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.BAR_CHART,
        "accent": ACCENT,
        "url": "certificates/explore_data_plots.pdf",
        "completed": True,
    },
    {
        "title": "MATLAB Desktop Tools & Troubleshooting",
        "body": "Optimizing the development environment, managing search paths, and debugging scripts efficiently.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.BUILD_OUTLINED,
        "accent": ACCENT,
        "url": "certificates/desktop_tools_troubleshooting.pdf",
        "completed": True,
    },
    {
        "title": "Machine Learning",
        "body": "Testing and training models to tackle real world problems.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.BOLT_OUTLINED,
        "accent": ACCENT,
        "url": "certificates/machine_learning_onramp.pdf",
        "completed": True,
    },
    {
        "title": "Make & Manipulate Matrices",
        "body": "Build new matrices from existing ones,create array functions, reshape arrays and indexing to extract submatrices.",
        "status": "Verified • Click to view certificate",
        "icon": ft.Icons.ADD_BOX,
        "accent": ACCENT,
        "url": "certificates/make_and_manipulate_matrices.pdf",
        "completed": True,
    },
    {
        "title": "MathWorks Course #8",
        "body": "Upcoming verification slot to complete the required engineering portfolio track.",
        "status": "In Progress / Pending Track",
        "icon": ft.Icons.HOURGLASS_EMPTY_ROUNDED,
        "accent": "#334155",
        "url": None,
        "completed": False,
    },
]


def view(page: ft.Page) -> ft.Control:
    
    # Native Python handler targeting your computer's local file system
    def handle_certificate_click(e):
        if e.control.data:
            # Build an explicit absolute path to your local file
            relative_path = os.path.join("assets", e.control.data)
            absolute_path = os.path.abspath(relative_path)
            
            # Force your computer's default browser/PDF viewer to open it directly
            webbrowser.open(f"file://{absolute_path}")

    cards_grid = []
    
    for cert in CERTIFICATES:
        card_container = ft.Container(
            content=info_card(
                title=cert["title"],
                body=cert["body"],
                icon=cert["icon"],
                accent=cert["accent"],
                footer=cert["status"],
            ),
            col={"xs": 12, "sm": 12, "md": 6, "lg": 6},
        )
        
        if cert["completed"]:
            card_container.data = cert["url"]  # Storing 'certificates/filename.pdf'
            card_container.on_click = handle_certificate_click
            card_container.tooltip = "Click to view official certificate PDF"
            card_container.mouse_cursor = ft.MouseCursor.CLICK
        else:
            card_container.tooltip = "Course slot pending"
            card_container.mouse_cursor = ft.MouseCursor.BASIC
            
        cards_grid.append(card_container)

    return ft.Container(
        padding=ft.padding.symmetric(horizontal=42, vertical=28),
        bgcolor=BG_DARK,  
        content=ft.Column(
            controls=[
                section_title(
                    "MATLAB Achievement Hub",
                ),
                ft.ResponsiveRow(
                    controls=cards_grid,
                    spacing=20,
                    run_spacing=20,
                ),
            ],
            spacing=24,
        ),
    )