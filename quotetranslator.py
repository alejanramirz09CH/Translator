import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.window.width = 500
    page.window.height = 500

    quotes = {
        "en": "You miss 100 percent of the shots you don't take",
        "es": "Pierdes el 100 por ciento de los tiros que no haces",
        "fr": "Vous manquez 100 pour cent des tirs que vous ne prenez pas"
    }

    quote_text = ft.Text(
        value=quotes["en"],
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER
    )

    def change_language(e: ft.Event[ft.RadioGroup]):
        quote_text.value = quotes[e.control.value]
        quote_text.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Quote Translator",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Image(
                        src="waynegretzky.png",
                        width=150,
                        height=150,
                    ),

                    quote_text,

                    ft.Text("Select a language:"),

                    ft.RadioGroup(
                        value="en",
                        on_change=change_language,
                        content=ft.Column(
                            controls=[
                                ft.Radio(value="en", label="English"),
                                ft.Radio(value="es", label="Spanish"),
                                ft.Radio(value="fr", label="French"),
                            ]
                        )
                    ),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main=main, assets_dir="assets")