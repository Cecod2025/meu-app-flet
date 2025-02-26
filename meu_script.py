import flet as ft

def main(page: ft.Page):
    page.title = "App de Relatório"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome = ft.TextField(label="Nome", width=300)
    idade = ft.TextField(label="Idade", width=300)
    relatorio = ft.TextField(label="Relatório", multiline=True, width=300)

    def gerar_arquivo(e):
        dados = f"Nome: {nome.value}\nIdade: {idade.value}\nRelatório: {relatorio.value}"
        with open("relatorio.txt", "w") as f:
            f.write(dados)
        page.add(ft.Text("Arquivo gerado com sucesso!"))

    page.add(
        ft.Column(
            [
                nome,
                idade,
                relatorio,
                ft.ElevatedButton("Gerar Relatório", on_click=gerar_arquivo),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main, view=ft.WEB_BROWSER)