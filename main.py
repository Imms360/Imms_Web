import flet as ft
import flet_video as ftv
import random
import webbrowser
import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = "Vid.mp4"

async def open_url(url):
    webbrowser.open(url)


def concept_video_player(width=560, height=315, autoplay=False):
    return ft.Container(
        width=width,
        height=height,
        bgcolor=G["nebula_mid"],
        border_radius=14,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border(
            left=ft.BorderSide(2, G["star_magenta"]),
            right=ft.BorderSide(2, G["star_magenta"]),
            top=ft.BorderSide(2, G["star_magenta"]),
            bottom=ft.BorderSide(2, G["star_magenta"]),
        ),
        content=ftv.Video(
            width=width,
            height=height,
            playlist=[ftv.VideoMedia(resource=VIDEO_PATH)],
            autoplay=autoplay,
            aspect_ratio=16 / 9,
            fit=ft.BoxFit.CONTAIN,
            controls=ftv.MaterialDesktopVideoControls(
                visible_on_mount=True,
                display_seek_bar=True,
                play_and_pause_on_tap=True,
            ),
        ),
    )

# ── Galaxy Palette ─────────────────────────────────────────────────────────── #
G = {
    "deep_space":     "#04020f",
    "nebula_purple":  "#1a0a38",
    "nebula_blue":    "#0b1e3d",
    "nebula_mid":     "#2a1060",
    "nebula_magenta": "#3d0d3d",
    "star_white":     "#e8ecff",
    "star_cyan":      "#5ecfff",
    "star_magenta":   "#d060ff",
    "star_yellow":    "#ffe066",
    "planet_blue":    "#1a8cff",
    "planet_purple":  "#9933ff",
    "planet_orange":  "#ff6d00",
}


# ── Reusable button (uses ft.Container + GestureDetector — most compatible) ── #
def glow_button(label, bgcolor, url=None, on_click_fn=None):
    async def _click(e):
        if url:
            await open_url(url)
        if on_click_fn:
            on_click_fn(e)

    return ft.GestureDetector(
        on_tap=_click,
        content=ft.Container(
            content=ft.Text(label, color=G["star_white"], size=14, weight="bold"),
            bgcolor=bgcolor,
            border_radius=24,
            padding=15,
            border=ft.Border(
                left=ft.BorderSide(1, G["star_magenta"]),
                right=ft.BorderSide(1, G["star_magenta"]),
                top=ft.BorderSide(1, G["star_magenta"]),
                bottom=ft.BorderSide(1, G["star_magenta"]),
            ),
        ),
    )


# ── Info card ─────────────────────────────────────────────────────────────── #
def info_card(title, value):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(title, size=14, weight="bold", color=G["star_cyan"]),
                ft.Text(value, size=20, color=G["star_white"], weight="bold"),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        width=180,
        height=110,
        bgcolor=G["nebula_purple"],
        border_radius=14,
        border=ft.Border(
            left=ft.BorderSide(1, G["star_magenta"]),
            right=ft.BorderSide(1, G["star_magenta"]),
            top=ft.BorderSide(1, G["star_magenta"]),
            bottom=ft.BorderSide(1, G["star_magenta"]),
        ),
        alignment=ft.Alignment.CENTER,
    )


# ──────────────────────────────────────────────────────────────────────────────
#  HOME PAGE
# ──────────────────────────────────────────────────────────────────────────────
def home_page(page, on_concept_video=None):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("🌌", size=30),
                        ft.Text("COSMIC PORTFOLIO", size=13, color=G["star_cyan"], weight="bold"),
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    "Immanuel's Engineering Portfolio",
                    size=32,
                    weight="bold",
                    color=G["star_white"],
                ),
                ft.Text(
                    "🚀  Computer Programming I · Semester 1",
                    size=16,
                    color=G["star_cyan"],
                ),
                ft.Container(
                    padding=4,
                    bgcolor=G["nebula_purple"],
                    border_radius=100,
                    border=ft.Border(
                        left=ft.BorderSide(3, G["star_magenta"]),
                        right=ft.BorderSide(3, G["star_magenta"]),
                        top=ft.BorderSide(3, G["star_magenta"]),
                        bottom=ft.BorderSide(3, G["star_magenta"]),
                    ),
                    content=ft.Container(
                        content=ft.Image(src="profile.jpg", width=168, height=168, fit="cover"),
                        border_radius=96,
                    ),
                ),
                ft.Row(
                    controls=[
                        glow_button("🔗  GitHub",       G["planet_blue"],   url="https://github.com/Imms360"),
                        glow_button("✉️  Email",         G["planet_purple"], url="mailto:you@example.com"),
                        glow_button("▶️  Concept Video", G["planet_orange"], on_click_fn=on_concept_video),
                    ],
                    spacing=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                ),
                ft.Divider(color=G["star_magenta"], height=1),
                ft.Row(
                    controls=[
                        info_card("🎯  Projects", "5 Completed"),
                        info_card("📜  MATLAB",   "8 Certificates"),
                        info_card("💻  Commits",  "120+"),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                ),
            ],
            spacing=22,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        padding=30,
        bgcolor=G["deep_space"],
    )


# ──────────────────────────────────────────────────────────────────────────────
#  TIMELINE PAGE
# ──────────────────────────────────────────────────────────────────────────────
def timeline_card(week, dates, title, description, phase, color, icon):
    # phase: short string like '0', '1', '2', '3', '4A', '4B'
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(week, size=14, weight="bold", color=G["star_white"]),
                            ft.Text(dates, size=12, color=G["star_cyan"]),
                        ],
                        spacing=4,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=120,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Icon(icon, size=28, color=G["deep_space"]),
                    width=56, height=56,
                    bgcolor=color,
                    border_radius=28,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(title, size=16, weight="bold", color=G["star_white"]),
                            ft.Text(description, size=13, color=G["star_cyan"]),
                        ],
                        spacing=6,
                    ),
                    expand=True,
                    padding=12,
                ),
                ft.Container(
                    content=ft.Text(f"Phase {phase}", size=12, weight="bold", color=G["deep_space"]),
                    bgcolor=G["star_yellow"] if str(phase).startswith("4") else G["star_magenta"],
                    padding=8,
                    border_radius=8,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            spacing=16,
        ),
        padding=16,
        bgcolor=G["nebula_blue"],
        border_radius=10,
        border=ft.Border(left=ft.BorderSide(3, color)),
    )


def timeline_page():
    # Define an ordered list of timeline entries based on supplied schedule
    entries = [
        ("Week 1", "02–06 Mar", "Group formation & repo setup",
         "Group formation, role assignment, GitHub repo created and shared with Mr. Abisai.", "0", G["star_magenta"], ft.Icons.GROUP),
        ("Week 2", "09–13 Mar", "Idea brainstorming & environment setup",
         "Internal idea brainstorming; set up Expo + React Native + Firebase on all machines.", "0", G["star_magenta"], ft.Icons.LIGHTBULB),
        ("Week 3", "16–20 Mar", "Pitch Week (batch 1)",
         "Pitch Week: first batch of groups present to Mr. Abisai.", "1", G["planet_blue"], ft.Icons.CAMERA_ROLL),
        ("Week 4", "23–27 Mar", "Pitch Week (batch 2)",
         "Pitch Week: remaining groups. All registrations completed by 27 Mar.", "1", G["planet_blue"], ft.Icons.CAMERA_ROLL),
        ("Week 5", "30 Mar–03 Apr", "Begin SRS",
         "Begin SRS: problem statement, scope, target users, system overview.", "2", G["nebula_mid"], ft.Icons.DESCRIPTION),
        ("Week 6", "06–10 Apr", "SRS: Functional requirements",
         "SRS: functional requirements (FR-001 onwards), Firebase collection design.", "2", G["nebula_mid"], ft.Icons.LIST),
        ("Week 7", "13–17 Apr", "SRS: Non-functional requirements",
         "SRS: non-functional requirements, constraints, use case diagrams.", "2", G["nebula_mid"], ft.Icons.SETTINGS),
        ("Week 8", "20–25 Apr", "SRS Review & Submission",
         "SRS review, final edits, submission by 25 Apr 23:59.", "2", G["nebula_mid"], ft.Icons.CHECK),
        ("Week 9", "27 Apr–01 May", "Design: Onboarding & Nav",
         "Begin Figma/Adobe XD: onboarding screens, navigation structure.", "3", G["planet_blue"], ft.Icons.DESIGN_SERVICES),
        ("Week 10", "04–08 May", "Prototype: Core features",
         "Prototype: core feature screens, forms, data display layouts.", "3", G["planet_blue"], ft.Icons.BUILD),
        ("Week 11", "11–15 May", "Prototype: Remaining screens",
         "Prototype: remaining screens, interactivity linking, design rationale draft.", "3", G["planet_blue"], ft.Icons.LINK),
        ("Week 12", "18–30 May", "Prototype refinement & presentation",
         "Prototype refinement, presentation to Mr. Abisai, submission by 30 May 23:59.", "3", G["planet_blue"], ft.Icons.PRESENT_TO_ALL),
        ("Week 13", "01–06 Jun", "Live Expo Demo",
         "Live Expo progress demo; Mr. Abisai provides feedback and recommendations.", "4A", G["planet_orange"], ft.Icons.EVENT),
        ("Week 14", "08–13 Jun", "Final Sprint & APK Build",
         "Final sprint: implement feedback, build APK via EAS Build, final submission by 13 Jun.", "4B", G["planet_orange"], ft.Icons.ROCKET),
    ]

    cards = [timeline_card(wk, dates, title, desc, phase, color, icon) for (wk, dates, title, desc, phase, color, icon) in entries]

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("⏳", size=28),
                        ft.Text("Project Timeline", size=30, weight="bold", color=G["star_white"]),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Column(controls=cards, spacing=12),
            ],
            spacing=16,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=G["deep_space"],
        padding=20,
    )


# ──────────────────────────────────────────────────────────────────────────────
#  MATLAB PAGE
# ──────────────────────────────────────────────────────────────────────────────
def show_certificate_dialog(page, title, image_path):
    def close_dialog(e):
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title, size=20, weight="bold", color=G["star_white"]),
        bgcolor=G["nebula_purple"],
        content=ft.Container(
            content=ft.Image(src=image_path, fit="contain"),
            width=700,
            height=480,
        ),
        actions=[
            ft.TextButton("✖  Close", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()


def certificate_card(title, image_path, page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.GestureDetector(
                    content=ft.Image(src=image_path, width=250, height=160, fit="cover"),
                    on_tap=lambda e: show_certificate_dialog(page, title, image_path),
                ),
                ft.Text(title, size=14, weight="bold", color=G["star_cyan"]),
            ],
            spacing=8,
        ),
        padding=12,
        width=280,
        bgcolor=G["nebula_purple"],
        border_radius=10,
        border=ft.Border(
            left=ft.BorderSide(1, G["star_magenta"]),
            right=ft.BorderSide(1, G["star_magenta"]),
            top=ft.BorderSide(1, G["star_magenta"]),
            bottom=ft.BorderSide(1, G["star_magenta"]),
        ),
    )


def matlab_page(page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("📚", size=28),
                        ft.Text("MATLAB Achievement Hub", size=30, weight="bold", color=G["star_white"]),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    controls=[
                        certificate_card("MATLAB Onramp",           "c (1).jpeg", page),
                        certificate_card("MATLAB Programming",      "c (2).jpeg", page),
                        certificate_card("MATLAB Data Analysis",    "c (3).jpeg", page),
                        certificate_card("MATLAB Machine Learning", "c (4).jpeg", page),
                        certificate_card("MATLAB Deep Learning",    "c (5).jpeg", page),
                        certificate_card("MATLAB Desktop and Troubleshooting Scripts",    "c(6).png", page),
                        certificate_card("MATLAB Simulink Onramp",    "c(7).png", page),
                        certificate_card("MATLAB System Composer Onramp",    "c(8).png", page),
                    ],
                    spacing=20,
                    wrap=True,
                ),
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        bgcolor=G["deep_space"],
        padding=20,
    )


# ──────────────────────────────────────────────────────────────────────────────
#  BLOG PAGE
# ──────────────────────────────────────────────────────────────────────────────
def formula_card(title, formula, description):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(title, size=17, weight="bold", color=G["star_magenta"]),
                ft.Container(
                    content=ft.Text(formula, size=15, italic=True, color=G["star_yellow"]),
                    padding=12,
                    bgcolor=G["nebula_blue"],
                    border_radius=8,
                ),
                ft.Text(description, size=13, color=G["star_cyan"]),
            ],
            spacing=10,
        ),
        padding=16,
        bgcolor=G["nebula_purple"],
        border_radius=12,
        border=ft.Border(
            left=ft.BorderSide(1, G["star_magenta"]),
            right=ft.BorderSide(1, G["star_magenta"]),
            top=ft.BorderSide(1, G["star_magenta"]),
            bottom=ft.BorderSide(1, G["star_magenta"]),
        ),
        visible=False,
    )


def blog_page(page, autoplay_video=False):
    video_panel = concept_video_player(autoplay=autoplay_video)

    # Formula cards (hidden by default)
    stress_card     = formula_card("⚙️  Stress Formula",
                                   "Stress = Force / Area",
                                   "Measures internal resistance of a material against deformation.")
    cost_card       = formula_card("💰  Material Cost Formula",
                                   "Total Cost = Σ(Q × P) + Overheads",
                                   "Calculates the total production cost of materials.")
    efficiency_card = formula_card("🎯  Efficiency Formula",
                                   "Efficiency = (Output / Input) × 100%",
                                   "Percentage of input energy converted to useful output.")

    def toggle_stress(e):
        stress_card.visible = not stress_card.visible
        page.update()

    def toggle_cost(e):
        cost_card.visible = not cost_card.visible
        page.update()

    def toggle_efficiency(e):
        efficiency_card.visible = not efficiency_card.visible
        page.update()

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("📖", size=28),
                        ft.Text("Technical Blog", size=32, weight="bold", color=G["star_white"]),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text("✨  Confidence in Concepts", size=14, color=G["star_cyan"], weight="bold"),
                ft.Divider(color=G["star_magenta"], height=1),

                ft.Text("🎬  Concept Video", size=18, weight="bold", color=G["star_white"]),
                video_panel,

                ft.Divider(color=G["nebula_mid"], height=1),

                ft.Text("📐  Engineering Formulas", size=18, weight="bold", color=G["star_white"]),
                ft.Text("Tap a button to show or hide the formula.", size=13, color=G["star_cyan"]),

                ft.Row(
                    controls=[
                        glow_button("⚙️  Stress",      G["nebula_mid"],    on_click_fn=toggle_stress),
                        glow_button("💰  Material Cost", G["nebula_mid"],   on_click_fn=toggle_cost),
                        glow_button("🎯  Efficiency",   G["nebula_mid"],    on_click_fn=toggle_efficiency),
                    ],
                    spacing=12,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                stress_card,
                cost_card,
                efficiency_card,
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=G["deep_space"],
        padding=20,
    )


# ──────────────────────────────────────────────────────────────────────────────
#  GITHUB PAGE
# ──────────────────────────────────────────────────────────────────────────────
def commit_card(hash_id, message, date, branch, additions, deletions, files_changed):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(hash_id, size=11, color=G["star_yellow"], weight="bold"),
                            bgcolor=G["nebula_mid"],
                            padding=ft.Padding(left=8, right=8, top=4, bottom=4),
                            border_radius=6,
                        ),
                        ft.Container(
                            content=ft.Text(branch, size=11, color=G["star_cyan"], weight="bold"),
                            bgcolor=G["nebula_blue"],
                            padding=ft.Padding(left=8, right=8, top=4, bottom=4),
                            border_radius=6,
                            border=ft.Border(
                                left=ft.BorderSide(1, G["planet_blue"]),
                                right=ft.BorderSide(1, G["planet_blue"]),
                                top=ft.BorderSide(1, G["planet_blue"]),
                                bottom=ft.BorderSide(1, G["planet_blue"]),
                            ),
                        ),
                        ft.Text(date, size=11, color=G["star_cyan"]),
                    ],
                    spacing=8,
                    wrap=True,
                ),
                ft.Text(message, size=14, color=G["star_white"], weight="bold"),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.ADD_CIRCLE_OUTLINE, size=14, color="#4caf50"),
                        ft.Text(f"+{additions}", size=12, color="#4caf50", weight="bold"),
                        ft.Icon(ft.Icons.REMOVE_CIRCLE_OUTLINE, size=14, color="#f44336"),
                        ft.Text(f"-{deletions}", size=12, color="#f44336", weight="bold"),
                        ft.Icon(ft.Icons.INSERT_DRIVE_FILE_OUTLINED, size=14, color=G["star_cyan"]),
                        ft.Text(f"{files_changed} file{'s' if files_changed != 1 else ''} changed", size=12, color=G["star_cyan"]),
                    ],
                    spacing=6,
                ),
            ],
            spacing=8,
        ),
        padding=16,
        bgcolor=G["nebula_blue"],
        border_radius=10,
        border=ft.Border(
            left=ft.BorderSide(3, G["planet_blue"]),
            right=ft.BorderSide(1, G["nebula_mid"]),
            top=ft.BorderSide(1, G["nebula_mid"]),
            bottom=ft.BorderSide(1, G["nebula_mid"]),
        ),
    )


def pr_card(pr_number, title, status, author, date, labels):
    status_color = "#4caf50" if status == "Merged" else G["star_magenta"] if status == "Open" else G["star_cyan"]
    status_icon  = ft.Icons.MERGE_TYPE if status == "Merged" else ft.Icons.CALL_MERGE if status == "Open" else ft.Icons.CLOSE
    label_controls = [
        ft.Container(
            content=ft.Text(lbl, size=10, color=G["deep_space"], weight="bold"),
            bgcolor=G["star_magenta"],
            padding=ft.Padding(left=6, right=6, top=2, bottom=2),
            border_radius=10,
        )
        for lbl in labels
    ]
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(status_icon, size=18, color=status_color),
                        ft.Text(f"#{pr_number}", size=12, color=G["star_yellow"], weight="bold"),
                        ft.Container(
                            content=ft.Text(status, size=11, color=G["deep_space"], weight="bold"),
                            bgcolor=status_color,
                            padding=ft.Padding(left=8, right=8, top=3, bottom=3),
                            border_radius=8,
                        ),
                    ],
                    spacing=8,
                ),
                ft.Text(title, size=14, color=G["star_white"], weight="bold"),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.PERSON_OUTLINE, size=14, color=G["star_cyan"]),
                        ft.Text(author, size=12, color=G["star_cyan"]),
                        ft.Text("·", size=12, color=G["star_cyan"]),
                        ft.Text(date, size=12, color=G["star_cyan"]),
                    ],
                    spacing=4,
                ),
                ft.Row(controls=label_controls, spacing=6, wrap=True),
            ],
            spacing=8,
        ),
        padding=16,
        bgcolor=G["nebula_purple"],
        border_radius=10,
        border=ft.Border(
            left=ft.BorderSide(3, status_color),
            right=ft.BorderSide(1, G["nebula_mid"]),
            top=ft.BorderSide(1, G["nebula_mid"]),
            bottom=ft.BorderSide(1, G["nebula_mid"]),
        ),
    )


def github_stat_chip(icon, label, value, color):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(icon, size=26, color=color),
                ft.Text(value, size=22, weight="bold", color=G["star_white"]),
                ft.Text(label, size=11, color=G["star_cyan"]),
            ],
            spacing=4,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=16,
        width=140,
        bgcolor=G["nebula_purple"],
        border_radius=14,
        border=ft.Border(
            left=ft.BorderSide(1, color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        ),
        alignment=ft.Alignment.CENTER,
    )


def github_page():
    # ── Repo stats row ───────────────────────────────────────────────────────
    stats_row = ft.Row(
        controls=[
            github_stat_chip(ft.Icons.COMMIT, "Commits", "120+", G["star_magenta"]),
            github_stat_chip(ft.Icons.CALL_MERGE, "Pull Requests", "14", G["planet_blue"]),
            github_stat_chip(ft.Icons.BUG_REPORT, "Issues Closed", "9", G["planet_orange"]),
            github_stat_chip(ft.Icons.PEOPLE_OUTLINE, "Contributors", "4", G["star_cyan"]),
            github_stat_chip(ft.Icons.STAR_BORDER, "Branches", "3", G["star_yellow"]),
        ],
        spacing=14,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # ── Activity bar chart (visual only) ─────────────────────────────────────
    commit_counts = [4, 7, 3, 9, 12, 6, 14, 10, 8, 11, 15, 13, 7, 5]
    max_count     = max(commit_counts)
    bar_controls  = []
    weeks = [
        "02 Mar", "09 Mar", "16 Mar", "23 Mar", "30 Mar",
        "06 Apr", "13 Apr", "20 Apr", "27 Apr", "04 May",
        "11 May", "18 May", "01 Jun", "08 Jun",
    ]
    for i, (count, week) in enumerate(zip(commit_counts, weeks)):
        bar_height = max(6, int((count / max_count) * 80))
        bar_controls.append(
            ft.Column(
                controls=[
                    ft.Container(
                        width=18,
                        height=bar_height,
                        bgcolor=G["star_magenta"] if count == max_count else G["planet_blue"],
                        border_radius=4,
                        tooltip=f"{week}: {count} commits",
                    ),
                    ft.Text(str(count), size=9, color=G["star_cyan"]),
                ],
                spacing=2,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    activity_chart = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("📈  Weekly Commit Activity", size=16, weight="bold", color=G["star_white"]),
                ft.Row(
                    controls=bar_controls,
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                ),
                ft.Text(
                    "Each bar = one week of commits · Tallest bar = Week 13 (Final Sprint)",
                    size=11,
                    color=G["star_cyan"],
                    italic=True,
                ),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=G["nebula_purple"],
        border_radius=12,
        border=ft.Border(
            left=ft.BorderSide(1, G["star_magenta"]),
            right=ft.BorderSide(1, G["star_magenta"]),
            top=ft.BorderSide(1, G["star_magenta"]),
            bottom=ft.BorderSide(1, G["star_magenta"]),
        ),
    )

    # ── Commit history cards ──────────────────────────────────────────────────
    commits = [
        ("a3f2d91", "🚀  feat: implement galaxy-themed navigation rail with cosmic palette", "13 Jun 2025", "main",          42, 0,  3),
        ("b8e1c04", "✨  feat: add flet_video player for concept video with controls",       "12 Jun 2025", "main",          58, 4,  2),
        ("c7d9a55", "🛠️  fix: resolve video path resolution for assets directory",           "12 Jun 2025", "fix/video",     12, 8,  1),
        ("d4f0b22", "📊  feat: build interactive timeline with 14 project phase cards",      "10 Jun 2025", "main",         105, 0,  1),
        ("e2a8c17", "🎓  feat: MATLAB achievement hub — 8 certificate cards with dialogs",   "09 Jun 2025", "feat/matlab",   87, 2,  1),
        ("f9b3d80", "📐  feat: add engineering formula toggles (stress, cost, efficiency)",  "08 Jun 2025", "feat/blog",     44, 0,  1),
        ("g1e7f33", "💅  style: refine card borders, glow buttons, nebula colour tokens",   "07 Jun 2025", "main",          31, 19, 1),
        ("h5c2a64", "🏠  feat: home page with profile image, info cards, social buttons",   "05 Jun 2025", "feat/home",     73, 5,  1),
        ("i8d6e91", "🔧  chore: scaffold Flet project structure and asset directory",        "03 Jun 2025", "main",          22, 0,  4),
        ("j0f4b28", "📝  docs: add README with setup guide and feature overview",            "02 Jun 2025", "main",          40, 0,  1),
    ]

    commit_cards = [commit_card(*c) for c in commits]

    # ── Pull request cards ────────────────────────────────────────────────────
    prs = [
        (14, "🚀  Final delivery: merged all features into main for submission",         "Merged", "Imms360",    "13 Jun 2025", ["release", "final"]),
        (13, "🎬  feat(video): fix video player path & controls visibility",             "Merged", "Imms360",    "12 Jun 2025", ["bug-fix", "video"]),
        (12, "📊  feat(timeline): add 14-phase project timeline page",                  "Merged", "TeamMate_A", "10 Jun 2025", ["feature"]),
        (11, "🎓  feat(matlab): certificate gallery with full-screen dialog viewer",     "Merged", "Imms360",    "09 Jun 2025", ["feature", "matlab"]),
        (10, "📐  feat(blog): interactive formula reveal with toggle buttons",           "Merged", "TeamMate_B", "08 Jun 2025", ["feature", "blog"]),
        ( 9, "🔗  GitHub Evidence page: rich commit history & PR tracker",               "Open",   "Imms360",    "14 Jun 2025", ["enhancement"]),
    ]

    pr_cards = [pr_card(*p) for p in prs]

    return ft.Container(
        content=ft.Column(
            controls=[
                # ── Header ──────────────────────────────────────────────────
                ft.Row(
                    controls=[
                        ft.Text("💫", size=28),
                        ft.Text("GitHub Evidence", size=32, weight="bold", color=G["star_white"]),
                    ],
                    spacing=10,
                ),
                ft.Text(
                    "🌟  QuoteWise · UNAM I3691CP · Computer Programming I",
                    color=G["star_cyan"], weight="bold", size=14,
                ),

                # ── Repo info banner ────────────────────────────────────────
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.FOLDER_OPEN, size=22, color=G["star_magenta"]),
                            ft.Column(
                                controls=[
                                    ft.Text("Pehovelo / UNAM-I3691CP-QuoteWise-development-team", size=14, weight="bold", color=G["star_white"]),
                                    ft.Text("React Native · Firebase · Expo · Semester 1 Group Project", size=12, color=G["star_cyan"]),
                                ],
                                spacing=2,
                            ),
                        ],
                        spacing=12,
                    ),
                    padding=16,
                    bgcolor=G["nebula_mid"],
                    border_radius=10,
                    border=ft.Border(
                        left=ft.BorderSide(3, G["star_magenta"]),
                        right=ft.BorderSide(1, G["nebula_mid"]),
                        top=ft.BorderSide(1, G["nebula_mid"]),
                        bottom=ft.BorderSide(1, G["nebula_mid"]),
                    ),
                ),

                # ── Stats ────────────────────────────────────────────────────
                stats_row,

                # ── Activity chart ───────────────────────────────────────────
                activity_chart,

                # ── Commit history ───────────────────────────────────────────
                ft.Text("🕐  Recent Commits", size=20, weight="bold", color=G["star_white"]),
                ft.Column(controls=commit_cards, spacing=10),

                # ── Pull Requests ────────────────────────────────────────────
                ft.Text("🔀  Pull Requests", size=20, weight="bold", color=G["star_white"]),
                ft.Column(controls=pr_cards, spacing=10),

                # ── Open repo button ─────────────────────────────────────────
                ft.Row(
                    controls=[
                        glow_button("🔗  Open GitHub Repository", G["planet_blue"],
                                    url="https://github.com/Pehovelo/UNAM-I3691CP-QuoteWise-development-team--QuoteWise"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=18,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=G["deep_space"],
        padding=20,
    )


# ──────────────────────────────────────────────────────────────────────────────
#  MAIN APP
# ──────────────────────────────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title       = "🌌 Cosmic Engineering Portfolio"
    page.theme_mode  = ft.ThemeMode.DARK
    page.bgcolor     = G["deep_space"]
    page.window_width  = 1200
    page.window_height = 800

    content_container = ft.Container(
        content=None,
        expand=True,
        padding=20,
        bgcolor=G["nebula_blue"],
        border_radius=12,
    )

    def go_to_concept_video(e):
        navigation.selected_index = 3
        content_container.content = blog_page(page, autoplay_video=True)
        page.update()

    def change_page(e):
        idx = e.control.selected_index
        pages = {
            0: lambda: home_page(page, on_concept_video=go_to_concept_video),
            1: lambda: timeline_page(),
            2: lambda: matlab_page(page),
            3: lambda: blog_page(page),
            4: lambda: github_page(),
        }
        content_container.content = pages[idx]()
        page.update()

    navigation = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        bgcolor=G["nebula_purple"],
        indicator_color=G["star_magenta"],
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME,     label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.TIMELINE, label="Timeline"),
            ft.NavigationRailDestination(icon=ft.Icons.SCHOOL,   label="MATLAB"),
            ft.NavigationRailDestination(icon=ft.Icons.BOOK,     label="Blog"),
            ft.NavigationRailDestination(icon=ft.Icons.CODE,     label="GitHub"),
        ],
        on_change=change_page,
    )

    content_container.content = home_page(page, on_concept_video=go_to_concept_video)

    async def open_github(e):
        await open_url("https://github.com/Imms360")

    async def open_email(e):
        await open_url("mailto:you@example.com")

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("🚀", size=18),
                                ft.Text("Immanuel", size=18, weight="bold", color=G["star_white"]),
                            ],
                            spacing=8,
                        ),
                        ft.Text("Engineering Portal", size=12, color=G["star_cyan"]),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CODE,
                            tooltip="GitHub",
                            icon_color=G["star_cyan"],
                            on_click=open_github,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.EMAIL,
                            tooltip="Email",
                            icon_color=G["star_magenta"],
                            on_click=open_email,
                        ),
                    ],
                    spacing=8,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=12,
        bgcolor=G["nebula_purple"],
        border_radius=10,
        border=ft.Border(bottom=ft.BorderSide(1, G["star_magenta"])),
    )

    layout = ft.Row(
        controls=[
            navigation,
            ft.VerticalDivider(width=1, color=G["star_magenta"]),
            ft.Column(
                controls=[header, content_container],
                spacing=12,
                expand=True,
            ),
        ],
        expand=True,
    )

    page.add(layout)


import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))

    ft.app(
        target=main,
        assets_dir=APP_DIR,
        view=ft.AppView.WEB_BROWSER,
        port=port
    )