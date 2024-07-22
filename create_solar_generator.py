from itertools import combinations
from typing import List

from schemas import SolarGenerator


def create_solar_generator(products: list) -> List[SolarGenerator]:
    # separa os produtos por categoria
    solar_panels = [product for product in products if product.category == 'solar_panel']
    inverters = [product for product in products if product.category == 'inverter']
    controllers = [product for product in products if product.category == 'controller']

    solar_panel_kits = []

    solar_generator_id = 1000

    # Agrupando produtos por marca
    brands = {}
    for solar_panel in solar_panels:
        brand = solar_panel.name
        if brand not in brands:
            brands[brand] = []
        brands[brand].append(solar_panel)

    # Gerando combinações para cada marca
    for brand, product_list in brands.items():
        for i in range(1, len(product_list) + 1):
            for combination in combinations(product_list, i):
                solar_panel_kits.append(list(combination))

    solar_generators = []

    for solar_panel_kit in solar_panel_kits:
        kit_power = sum(solar_panel.power for solar_panel in solar_panel_kit)

        for controller in controllers:
            if controller.power == kit_power:
                for inverter in inverters:
                    if inverter.power == kit_power:
                        solar_generators.append(
                            SolarGenerator(
                                id=solar_generator_id,
                                solar_panels=solar_panel_kit,
                                inverter=inverter,
                                controller=controller,
                                power=kit_power
                            )
                        )
                        solar_generator_id += 1

    return solar_generators
