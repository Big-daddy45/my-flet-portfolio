import os
import webbrowser
import flet as ft

# --- Unified Technical Color System (Matched to home.py & certificates.py) ---
BG_DARK = "#0f172a"        # Deep Slate / Midnight Blue
SURFACE_CARD = "#1e293b"   # Slate Blue Card Background
ACCENT = "#38bdf8"         # Sharp Technical Cyan
TEXT_MAIN = "#f8fafc"      # Off-white Text
MUTED = "#94a3b8"          # Gray Muted Text

def view(page: ft.Page) -> ft.Container:
    page.title = "Computer Programming Projects"

    # ==========================================
    # PDF OPENING HANDLER (Matched to certificates.py logic)
    # ==========================================
    def handle_pdf_click(e):
        # Resolves the path to your assets folder cleanly across different OS environments
        relative_path = os.path.join("assets", "banking_code_export.pdf")
        absolute_path = os.path.abspath(relative_path)
        
        if os.path.exists(absolute_path):
            webbrowser.open(f"file://{absolute_path}")
        else:
            # Fallback if asset isn't found exactly where expected
            print(f"Error: PDF file not found at {absolute_path}")

    # ==========================================
    # TAB 1 CONTENT: CORRO-CHECK APP
    # ==========================================
    corro_check_content = ft.Column(
        scroll="auto",
        spacing=15,
        controls=[
            ft.Text("Semester Project: Corro-Check App", size=26, weight="bold", color=TEXT_MAIN),
            ft.Text("Role: Person 4 (Node.js Server & Roboflow API)", size=18, weight="bold", color=ACCENT),
            ft.Text(
                "As Person 4 on the backend team, my responsibility was building the Node.js backend server. "
                "This involved receiving photos uploaded from the React Native app, sending them to the Roboflow API "
                "for corrosion analysis, and returning the structured severity results back to the application. "
                "It was the most technical backend role in our team infrastructure.",
                color=MUTED,
                size=15
            ),
            ft.Container(height=15),
            
            # Media Stack: Video below the screenshot
            ft.Column(
                horizontal_alignment="center",
                spacing=25,
                controls=[
                    # 1. GitHub Commit Screenshot Slot
                    ft.Container(
                        bgcolor=SURFACE_CARD,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(1, "#334155"),
                        content=ft.Column(
                            horizontal_alignment="center",
                            controls=[
                                ft.Text("GitHub Commit Evidence", weight="bold", color=TEXT_MAIN),
                                ft.Image(
                                    src="images/commit_screenshot.png", 
                                    width=450,
                                    height=220,
                                    fit="contain"
                                )
                            ]
                        )
                    ),
                    # 2. Local Video Embed Slot
                    ft.Container(
                        bgcolor=SURFACE_CARD,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(1, "#334155"),
                        content=ft.Column(
                            horizontal_alignment="center",
                            controls=[
                                ft.Text("App Walkthrough Video", weight="bold", color=TEXT_MAIN),
                                ft.Markdown(
                                    "<video width='450' height='250' controls><source src='vlogs/project_walkthrough.mp4' type='video/mp4'></video>"
                                )
                            ]
                        )
                    )
                ]
            )
        ]
    )

    # ==========================================
    # TAB 2 CONTENT: PROGRAMMING CONCEPTS
    # ==========================================
    programming_concepts_content = ft.Column(
        scroll="auto",
        spacing=15,
        controls=[
            ft.Text("Programming Concepts", size=26, weight="bold", color=TEXT_MAIN),
            ft.Container(height=10),
            
            # --- Part 1: Banking App ---
            ft.Container(
                bgcolor=SURFACE_CARD,
                padding=20,
                border_radius=10,
                border=ft.border.all(1, "#334155"),
                content=ft.Column(
                    controls=[
                        ft.Text("1. Python Banking App Simulator", size=20, weight="bold", color=ACCENT),
                        ft.Text(
                            "This Python script implements a lightweight, terminal-based Banking System Simulator. "
                            "It utilizes a stateful loop to continuously handle user interactions until an explicit exit command is issued. "
                            "The codebase demonstrates fundamental Python concepts including checking account balance records, "
                            "simulating cash withdrawals, processing structured cash deposits, and validating monetary transfers.",
                            color=MUTED
                        ),
                        ft.Container(height=5),
                        ft.ElevatedButton(
                            content=ft.Text("View Banking Code PDF"),
                            icon="picture_as_pdf",
                            on_click=handle_pdf_click, # Fixed: Replaced 'url' with native handler click trigger
                            style=ft.ButtonStyle(
                                bgcolor=ACCENT,
                                color=BG_DARK,
                                shape=ft.RoundedRectangleBorder(radius=8),
                            )
                        )
                    ]
                )
            ),
            
            ft.Container(height=10),

            # --- Part 2: MATLAB Kinematics Calculator ---
            ft.Container(
                bgcolor=SURFACE_CARD,
                padding=20,
                border_radius=10,
                border=ft.border.all(1, "#334155"),
                content=ft.Column(
                    controls=[
                        ft.Text("2. MATLAB Kinematics Calculator", size=20, weight="bold", color=ACCENT),
                        ft.Text(
                            "This calculator was built using MATLAB to automate the solving of standard 1D and 2D kinematic equations. "
                            "The project demonstrates applied matrix operations, data visualization using plot functions, "
                            "and user-defined algorithmic scripts to calculate velocity, acceleration, and displacement vectors efficiently.",
                            color=MUTED
                        ),
                        ft.Container(height=10),
                        # MATLAB Screenshot Slot
                        ft.Image(
                            src="images/calculator.png", 
                            width=450,
                            height=250,
                            fit="contain"
                        )
                    ]
                )
            )
        ]
    )

    # ==========================================
    # VERTICAL NAVIGATION IMPLEMENTATION
    # ==========================================
    content_area = ft.Container(
        expand=True,
        padding=10,
        content=corro_check_content
    )

    def switch_tab(e):
        if e.control.data == "tab1":
            content_area.content = corro_check_content
        else:
            content_area.content = programming_concepts_content
        page.update()

    # Left-Side Sidebar
    sidebar_menu = ft.Column(
        width=210,
        spacing=15,
        controls=[
            ft.Text("Projects Menu", size=16, weight="bold", color=TEXT_MAIN),
            ft.ElevatedButton(
                content=ft.Text("Corro-Check App"),
                data="tab1",
                on_click=switch_tab,
                width=190,
                style=ft.ButtonStyle(
                    bgcolor=SURFACE_CARD,
                    color=TEXT_MAIN,
                    shape=ft.RoundedRectangleBorder(radius=6),
                )
            ),
            ft.ElevatedButton(
                content=ft.Text("Programming Concepts"),
                data="tab2",
                on_click=switch_tab,
                width=190,
                style=ft.ButtonStyle(
                    bgcolor=SURFACE_CARD,
                    color=TEXT_MAIN,
                    shape=ft.RoundedRectangleBorder(radius=6),
                )
            )
        ]
    )

    # --- Assembling View Container Layout ---
    return ft.Container(
        bgcolor=BG_DARK,
        padding=ft.padding.only(left=30, right=30, top=20, bottom=40),
        content=ft.Row(
            expand=True,
            vertical_alignment="start",
            controls=[
                sidebar_menu,
                ft.VerticalDivider(width=20, color="#334155"),
                content_area
            ]
        )
    )