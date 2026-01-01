import flet as ft

class CalculatorApp:
    def __init__(self):
        self.display = ft.TextField(
            value="",
            text_align=ft.TextAlign.RIGHT,
            read_only=True,
            text_size=26,
            expand=True,
        )

    def build(self, page: ft.Page):
        page.title = "حاسبة حسين البياتي"
        page.window_width = 360
        page.window_height = 520
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.padding = 10

        title = ft.Text(
            "حاسبة حسين البياتي",
            size=30,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )

        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"],
        ]

        grid = ft.Column(spacing=8)

        for row in buttons:
            grid.controls.append(
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text=key,
                            expand=True,
                            height=60,
                            on_click=self.on_button,
                        )
                        for key in row
                    ],
                    spacing=8,
                )
            )

        page.add(
            title,
            self.display,
            grid,
        )

    def on_button(self, e: ft.ControlEvent):
        text = e.control.text

        if text == "C":
            self.display.value = ""
        elif text == "=":
            try:
                exp = self.display.value.replace("×", "*").replace("÷", "/")
                self.display.value = str(eval(exp))
            except:
                self.display.value = "خطأ"
        else:
            self.display.value += text

        e.page.update()


def main(page: ft.Page):
    app = CalculatorApp()
    app.build(page)


# 🔹 هنا خارج أي دالة:
ft.run(main)
