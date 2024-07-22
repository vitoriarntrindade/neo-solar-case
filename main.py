from generate_report_pdf import generate_report_pdf
from utils import get_data_and_organize, save_generators_in_csv
from create_solar_generator import create_solar_generator
from email_service import EmailService
from generate_dataframe_pdf import create_pdf_with_table

# URL do Anexo B
PRODUCTS_URL_ENDPOINT = "https://case-1sbzivi17-henriques-projects-2cf452dc.vercel.app/"


def run():
    # Faz a request para o endpoint de produtos e retorna em objetos
    products = get_data_and_organize(url=PRODUCTS_URL_ENDPOINT)

    # Configura os geradores por kits
    solar_generators = create_solar_generator(products=products)

    # Cria arquivo CSV
    save_generators_in_csv(solar_generators=solar_generators, filename='geradores_configurados.csv')

    # Envia email de notificação da quantidade de geradores configurados
    email_service = EmailService()
    body = f"Quantidade de Geradores configurados nesta semana: {len(solar_generators)}"
    email_service.send(to_email='comercial@neosolar.png.com.br', subject='Relatorio Geradores', body=body,
                       cc=['suporte@neosolar.png.com.br'])

    # Cria um PDF para o email de notificação da quantidade de geradores configurados
    generate_report_pdf(solar_generators)

    # Cria Tabela em PDF para visualização dos geradores configurados ao time de  marketing.
    create_pdf_with_table(solar_generators)


if __name__ == '__main__':
    run()
