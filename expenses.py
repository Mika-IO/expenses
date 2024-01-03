input_text = """
[17:21, 12/29/2023] Mikaio: 21,41 gasolina
[17:22, 12/29/2023] Mikaio: 209,04 parcela ar-condicionado
[17:23, 12/29/2023] Mikaio: 49,90 parcela da bicicleta
[17:31, 12/29/2023] Mikaio: 22,25 mercadin leite e skol beats
[17:50, 12/29/2023] Mikaio: 24,90 padaria
[09:36, 12/30/2023] AMOOR cara de ©ú ❤️❤️😎👍👌😭: 93,32 depilação do xibiu
[10:06, 12/30/2023] Mikaio: 66 espetinho
[18:02, 12/30/2023] Mikaio: 117 utilidades
[18:18, 12/30/2023] AMOOR cara de ©ú ❤️❤️😎👍👌😭: 130 vestido
[18:44, 12/30/2023] Mikaio: 4 mercadin
[18:57, 12/30/2023] AMOOR cara de ©ú ❤️❤️😎👍👌😭: 474 mercado
[20:40, 12/31/2023] Mikaio: 77 grego
[20:40, 12/31/2023] Mikaio: 13 mercadin
[20:40, 12/31/2023] Mikaio: 170 camisa
[21:04, 12/31/2023] AMOOR cara de ©ú ❤️❤️😎👍👌😭: 49,50 fralda
[12:26, 1/1/2024] Mikaio: 53 lanche duplo
[16:26, 1/1/2024] Mikaio: 105 openAI
[10:10, 1/3/2024] Mikaio: 9,95 amazon
[15:38, 1/3/2024] Mikaio: 62 matricula facul
[15:38, 1/3/2024] Mikaio: 37 hub usb
"""

import re


def processar_mensagens(texto):
    padrao_gasto = re.compile(
        r"\[\d{2}:\d{2}, \d{1,2}/\d{1,2}/\d{4}\] .+: (\d+,\d{2}|\d+) .+"
    )
    total_gasto = 0.0

    mensagens = texto.split("\n")
    for mensagem in mensagens:
        correspondencia = padrao_gasto.match(mensagem)
        if correspondencia:
            valor = correspondencia.group(1).replace(",", ".")
            try:
                total_gasto += float(valor)
            except ValueError:
                print(f"Não foi possível converter o valor: {valor}")

    return total_gasto


total = processar_mensagens(input_text)
print(total)
