import os
import shutil


TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Laboratório Hacker de Campinas - #{0}</title>
</head>
<body>
    <h1>Item #{0}</h1>
    <img src="assets/item.jpeg" />
    <h2>Nenhum item cadastrado com esse número de patrimônio.</h2>
    <p>Substitua o conteúdo desse arquivo com as informações relevantes sobre o item cadastrado com esse número de patrimônio.</p>
    <p>Adicione qualquer arquivo estático relacionado ao item (fotos, arquivos de manuais de operação, vídeos, etc) dentro do diretório <strong>/{0}/assets</strong></p>
</body>
</html>
"""


def main():
    for idx in range(1, 101):
        patrimonio = f"{idx:04}"
        os.makedirs(f"docs/{patrimonio}/assets", exist_ok=True)

        original = "item.jpeg"
        target = f"docs/{patrimonio}/assets/item.jpeg"
        shutil.copyfile(original, target)

        with open(f"docs/{patrimonio}/index.html", "w") as content:
            content.write(TEMPLATE.format(patrimonio))


if __name__ == "__main__":
    main()
