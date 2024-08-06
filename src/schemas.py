from typing import List, Dict


class Product:
    def __init__(self, id: int, product_name: str, power: int, category: str):
        self.id = id
        self.name = product_name
        self.power = power
        self.category = category
        self.quantity = 1


class Inverter(Product):
    pass


class Controller(Product):
    pass


class SolarPanel(Product):
    pass


class SolarGenerator:
    def __init__(
            self,
            id: int,
            solar_panels: List[SolarPanel],
            controller: Controller,
            inverter: Inverter,
            power: int,
    ):
        self.id = id
        self.solar_panels = solar_panels
        self.controller = controller
        self.inverter = inverter
        self.power = power
        self.solar_panels_quantity = len(solar_panels)

    def inverter_to_dict(self) -> Dict:
        return {
            "generator_id": self.id,
            "id": self.inverter.id,
            "name": self.inverter.name,
            "power": self.inverter.power,
            "quantity": self.inverter.quantity
        }

    def controller_to_dict(self) -> Dict:
        return {
            "generator_id": self.id,
            "id": self.controller.id,
            "name": self.controller.name,
            "power": self.controller.power,
            "quantity": self.controller.quantity
        }

    def solar_panels_to_dict(self) -> List[Dict]:
        solar_panels = []
        for solar_panel in self.solar_panels:
            solar_panels.append({
                "generator_id": self.id,
                "id": solar_panel.id,
                "name": solar_panel.name,
                "power": solar_panel.power,
                "quantity": solar_panel.quantity
            })
        return solar_panels


