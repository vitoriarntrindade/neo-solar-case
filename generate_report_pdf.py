import os
from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Nome do arquivo PDF
file_pdf = "relatorio_semanal_geradores.pdf"

ROOT_PATH = Path(__file__).parent


def generate_report_pdf(solar_generators, arquivo_pdf=file_pdf):
    # Cria um objeto Canvas

    path_pdf = f'{ROOT_PATH}/email_marketing_{datetime.now()}.pdf'

    # Verificando se o diretório do arquivo PDF existe; se não, cria o diretório
    folder_pdf = os.path.dirname(path_pdf)
    if folder_pdf and not os.path.exists(folder_pdf):
        os.makedirs(folder_pdf)

    c = canvas.Canvas(arquivo_pdf, pagesize=letter)
    largura, altura = letter

    # Título do relatório
    title = "Relatório semanal de geradores configurados"
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, altura - 40, title)

    # Conteúdo do relatório
    c.setFont("Helvetica", 12)
    texto = f"Quantidade de Geradores configurados: {len(solar_generators)}"
    c.drawString(30, altura - 70, texto)

    # Salva o PDF
    c.save()
