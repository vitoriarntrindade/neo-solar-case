from typing import List, Union, Optional, Type
import requests
import csv

from schemas import Inverter, Controller, SolarPanel, SolarGenerator


def factory_product_schemas(category: str) -> Optional[Type[Union[Inverter, Controller, SolarPanel]]]:
    return {
        'inverter': Inverter,
        'controller': Controller,
        'solar_panel': SolarPanel
    }.get(category)


def get_data_and_organize(url: str) -> List[object]:
    """
    Faz uma requisição HTTP GET para a URL fornecida e organiza os dados em categoriase transforma em objetos.

    Args:
        url (str): URL para a qual a requisição será feita.

    Returns:
        dict: Um dicionário com três listas: 'paineis', 'inversores' e 'controladores'.
    """

    response = requests.get(url)

    # Converter a resposta para JSON
    data = response.json()

    products = []

    category_translation = {
        'Inversor': 'inverter',
        'Controlador de carga': 'controller',
        'Painel Solar': 'solar_panel'
    }

    for product in data:
        category = product.get('Categoria')
        translated_category = category_translation.get(category)
        product_factory = factory_product_schemas(translated_category)

        products.append(
            product_factory(
                id=product['Id'],
                product_name=product.get('Produto', ''),
                power=product.get('Potencia em W', None),
                category=translated_category
            )
        )

    return products


def save_generators_in_csv(solar_generators: List[SolarGenerator],
                           filename="geradores_configurados.csv") -> None:
    """
    Salva a lista de geradores em um arquivo CSV.

    Args:
        solar_generators (list of dict): Lista de geradores a serem salvos.
        filename (str, optional): Nome do arquivo CSV onde os dados serão salvos.
                                  Padrão é "geradores_configurados.csv".
    """
    # Definir os campos para o CSV
    fields = ["ID Gerador", "Potência do Gerador (em W)", "ID Produto", "Nome do Produto", "Quantidade"]

    # Abrir o arquivo CSV para escrita
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)

        for solar_generator in solar_generators:
            for solar_panel in solar_generator.solar_panels:
                writer.writerow([solar_generator.id, solar_panel.power, solar_panel.id, solar_panel.name, '1'])
            writer.writerow(
                [solar_generator.id, solar_generator.inverter.power, solar_generator.inverter.id, solar_generator.inverter.name, '1']
            )
            writer.writerow(
                [solar_generator.id, solar_generator.controller.power, solar_generator.controller.id, solar_generator.controller.name, '1']
            )
