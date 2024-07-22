import datetime
import os
from typing import List

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from pathlib import Path

from schemas import SolarGenerator

ROOT_PATH = Path(__file__).parent


def create_pdf_with_table(solar_generators: List[SolarGenerator]) -> None:
    path_pdf = f'{ROOT_PATH}/email_marketing_{datetime.datetime.now()}.pdf'

    # Verificando se o diretório do arquivo PDF existe; se não, cria o diretório
    folder_pdf = os.path.dirname(path_pdf)
    if folder_pdf and not os.path.exists(folder_pdf):
        os.makedirs(folder_pdf)

    # Criando o documento PDF
    doc = SimpleDocTemplate(path_pdf, pagesize=letter)
    elements = []

    products_dict_list = []

    for solar_generator in solar_generators:
        for solar_panel in solar_generator.solar_panels_to_dict():
            products_dict_list.append(solar_panel)
        products_dict_list.append(solar_generator.inverter_to_dict())
        products_dict_list.append(solar_generator.controller_to_dict())

    # Lendo o arquivo CSV usando pandas
    df = pd.DataFrame(products_dict_list)

    df.columns = ["ID Gerador", "ID Produto", "Nome do Produto", "Potência do Gerador (em W)", "Quantidade"]

    # Convertendo o DataFrame para uma lista de listas
    table_data = [df.columns.tolist()] + df.values.tolist()

    # Criando a tabela
    table = Table(table_data, repeatRows=1)  # repeatRows=1 para repetir o cabeçalho em todas as páginas

    # Adicionando estilo à tabela
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFD700')),  # Amarelo suave da NeoSolar para o cabeçalho
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Cor do texto do cabeçalho
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#FFFFE0")),  # Fundo branco para o corpo da tabela
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Tamanho da fonte do cabeçalho
    ]))

    # Adicionando a tabela ao documento
    elements.append(table)

    # Construindo o documento PDF
    doc.build(elements)
