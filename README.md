
![Logo da Neosolar](https://www.neosolar.com.br/media/logo/stores/1/neosolar-logo.png)



# Projeto: Automatização da Criação de Geradores Solares

Este projeto visa automatizar a criação de geradores solares fotovoltaicos utilizando uma combinação específica de painéis solares, inversores e controladores de carga. O script realiza a configuração dos geradores, salva as informações em um arquivo CSV e cria relatórios em PDF para a equipe de marketing da Neosolar.

## Estrutura do Projeto

O script principal realiza as seguintes etapas:

1. **Obter Dados e Organizar**
2. **Configurar Geradores**
3. **Salvar Dados em CSV**
4. **Enviar notificação por email com a quantidade de geradores**
5. **Criar Tabela em PDF com os Geradores Configurados para uso do time de Marketing**

## Diagrama de Caso de Uso

![Diagrama de Caso de Uso](https://raw.githubusercontent.com/vitoriarntrindade/neo-solar-case/main/diagrams/use_case_diagram.png)


## Requisitos

Antes de executar o script, certifique-se de que você tem as seguintes bibliotecas instaladas:

- `requests`
- `pandas`
- `reportlab`

Você pode instalar essas dependências usando `pip`:

```bash
pip install -r requirements.txt
```
### Executando o projeto

Após instalar as dependências, basta rodar o arquivo main.py

```bash
python main.py
```

### Documentação


## 1. **get_data_and_organize**(url)

Descrição:

Faz uma requisição HTTP GET para a URL fornecida, organiza os dados em categorias 
e transforma em objetos.

Parâmetros:

    url (str): URL onde os dados estão disponíveis.

Retorno:

    Uma lista de Objetos (Inverter, Controller e SolarPanel).

## 2. **create_solar_generator**(products)

Descrição:

Prepara os dados dos geradores configurados a partir das listas de painéis, controladores e inversores. 
Gera combinações válidas de componentes que atendem aos requisitos para configuração de um Gerador.

Parâmetros:

    [Products] - Uma lista de Objetos (Inverter, Controller, SolarPanel)

Retorno:

    Uma lista de Objetos SolarGenerator.

## 3. **save_generators_in_csv**(solar_generators)

Descrição:

Salva as informações dos geradores configurados em um arquivo CSV.

Parâmetros:

    solar_generators (list): Lista de Objetos SolarGenerator.

![image](https://github.com/user-attachments/assets/a7457297-b8f4-4624-bda2-8432610dc3dd)



## 4. **email_service** = EmailService() 
email_service.send(solar_generators)

Descrição:

Simula o envio de um Email para equipe de marketing um relatório com a quantidade total de geradores 
configurados nesta semana. A Quantidade é inserida de forma dinâmica no email.

Parâmetros:

    email_service.send(to_email='comercial@neosolar.png.com.br', subject='Relatorio Geradores', body=body,
                       cc=['suporte@neosolar.png.com.br'])

Retorno:

         Enviando email para comercial@neosolar.png.com.br 
         Assunto: Relatorio Geradores 
         Conteúdo: Quantidade de Geradores configurados nesta semana: 3 
         cc: ['suporte@neosolar.png.com.br']

## 5. **generate_report_pdf**(solar_generators)    
    
Descrição:

Cria um arquivo PDF com um relatório com a quantidade total de geradores 
configurados nesta semana. A Quantidade é inserida de forma dinâmica no arquivo.
                
## 6. **create_pdf_with_table**()

Descrição:

Cria um arquivo PDF contendo uma tabela com os detalhes dos geradores configurados. Cada vez que 
o scrip roda, gera um novo arquivo nomeado dinamicamente.

![image](https://github.com/user-attachments/assets/d9d2692d-ff4b-4dee-b041-0161fb72e933)



### Arquivos Gerados

    geradores_configurados.csv: Arquivo CSV com dados dos geradores configurados.

    email_marketing.pdf: PDF contendo a tabela dos Geradores configurados a ser enviado ao time
    de marketing.

    relatorio_semanal_geradores.pdf: PDF contendo um relatório com a quantidade de geradores configurados na semana.

