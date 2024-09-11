# ## - **Importando Bibliotecas**

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ## - **Entrando no Indeed**


driver = webdriver.Chrome()
url_login = "https://br.indeed.com/"
driver.get(url_login)


# ## - **Pequisando Vagas**

def pesquisar(input_cargo, input_localidade):
    global url_login

    driver.get(url_login)

    try: #recusando cookies
        recusar_cookies = driver.find_element(By.ID, "onetrust-reject-all-handler")
        recusar_cookies.click()
    except:
        pass


    cargo = driver.find_element(By.ID, "text-input-what") #encontra a barra de pesquisa para cargos
    localidade = driver.find_element(By.ID, "text-input-where") #encontra a barra de pesquisa para localidade


    #Apaga qualquer texto que foi previamente escrito na barra de cargos
    cargo.send_keys(Keys.CONTROL + "a")
    cargo.send_keys(Keys.BACKSPACE)

    sleep(.5)


    #Apaga qualquer texto que foi previamente escrito na barra de localidade
    localidade.send_keys(Keys.CONTROL + "a")
    localidade.send_keys(Keys.BACKSPACE)

    sleep(.5)


    #Preenche as barras de pesquisa e realiza a pesquisa
    cargo.send_keys(input_cargo)
    localidade.send_keys(input_localidade)
    localidade.send_keys(Keys.ENTER)


# ## - **Definindo Função de Descrições de Vaga**


def raspar_dados():
    try: #Prourando título da vaga
        titulo = driver.find_element(By.CLASS_NAME, "jobsearch-JobInfoHeader-title-container.css-bbq8li.eu4oa1w0").text
    except:
        titulo = "[Segmento Não Identificado]"
        pass

    
    try: #Procurando nome da empresa
        empresa = driver.find_element(By.CLASS_NAME, "css-hon9z8.eu4oa1w0").text
    except:
        empresa = "[Segmento Não Identificado]"
        pass

    
    try: #Procurando a localizaçaõ da vaga
        localizacao = driver.find_element(By.ID, "jobLocationWrapper").text
    except:
        localizacao = "[Segmento Não Identificado]"
        pass

    
    try: #Procurando benefícios oferecidos
        beneficios = driver.find_element(By.ID, "benefits").text
    except:
        beneficios = "[Segmento Não Identificado]"
        pass

    
    try: #Procurando descrição da vaga
        descricao = driver.find_element(By.ID, "jobDescriptionText").text
    except:
        descricao = "[Segmento Não Identificado]"
        pass


    try: #Detalhes adicionais sobre a vaga
        detalhes = driver.find_element(By.ID, "jobDetailsSection").text
    except:
        detalhes = "[Segmento Não Identificado]"
        pass

    
    #Link para inscrição
    link_vaga = driver.current_url
    


    if titulo == "[Segmento Não Identificado]":
        pass


    texto = f'''# Título da Vaga:
{titulo}

# Empresa Contratante:
{empresa}

# Localização:
{localizacao}

# Benefícios:
{beneficios}

# Descrição da vaga:
{descricao}

# Detalhes adicionais:
{detalhes}

# Link da vaga:
{link_vaga}
'''

    return texto


# ## - **Iterando sobre Vagas**


def iterar_vagas(vagas_iteradas: list):

    lista_ul = driver.find_element(By.CSS_SELECTOR, ".css-zu9cdh.eu4oa1w0")
    lista_vagas = lista_ul.find_elements(By.XPATH, "./li")


    #Fechar aba de ativação de login
    try:
        ignore = lista_ul.find_element(By.ID, "mosaic-afterFifthJobResult")
        
        ignore_hamburguer = ignore.find_element(By.ID, "menu-button--menu--1")
        ignore_hamburguer.click()

        fechar = driver.find_element(By.CLASS_NAME, "css-1d4wshm.ehvvxyn1")
        fechar.click()

    except:
        pass



    for vaga in lista_vagas:
        try:
            vaga.click()
            
            sleep(3)

            dados_vaga = raspar_dados()
            vagas_iteradas.append(dados_vaga)

            sleep(.5)
        except:
            pass


def scrap_indeed(input_cargo, input_localidade):

    vagas_iteradas = []


    #Formatando cargo para url
    split_cargo = input_cargo.split()
    url_cargo = "+".join(split_cargo)

    #Formatando localidade para url
    split_localidade = input_localidade.split()
    url_localidade = "+".join(split_localidade)

    #Pegando a quantidade de páginas disponíveis 
    dadElement = driver.find_element(By.CLASS_NAME, "css-1g90gv6.eu4oa1w0")
    childrenElements = dadElement.find_elements(By.XPATH, "./li")
    num_pages = len(childrenElements)


    if num_pages == 0:
        iterar_vagas(vagas_iteradas)

    elif num_pages > 0:

        #Repetindo a função até a última página disponível
        for i in range(num_pages - 1): 
            url = f"https://br.indeed.com/jobs?q={url_cargo}&l={url_localidade}&start={i*10}"
            driver.get(url)
            sleep(2)


            #Fechar aba de ativação de login
            try:
                botao = driver.find_element(By.CLASS_NAME, "css-yi9ndv.e8ju0x51")
                botao.click()
            except:
                pass
            
            iterar_vagas(vagas_iteradas)
    
    
    return vagas_iteradas



