from playwright.sync_api import sync_playwright
import time
from random import randint

#Variaveis
mensagem = ['Mensagem 1', 'Mensagem 2', 'Mensagem 3']
site = 'https://www.instagram.com'
caminho = 'Final do link do sorteio exemplo: "/p/c5ds7AsD6/" '
lista_login = ['Login1', 'Login2', 'Login3','Login4', 'Login5']
lista_senha = ['Senha1', 'Senha2', 'Senha3','Senha4', 'Senha5']
tamanho_lista = len(lista_login)
qtd_mensagem = len(mensagem) - 1
total_comentarios, total_minutos, total_segundos = 0, 0, 0

for k in range(tamanho_lista):
    pos_lista = k
    login = lista_login[pos_lista]
    senha = lista_senha[pos_lista]
    qtd_comentarios = randint(27,37)
    tempo_comentarios = 0    
    
    with sync_playwright() as p:
    
        navegador = p.chromium.launch(headless=False)
        page = navegador.new_page()
        page.goto(site)
        time.sleep(1)

        #Login
        page.fill('xpath=//*[@id="loginForm"]/div/div[1]/div/label/input', login)
        page.fill('xpath=//*[@id="loginForm"]/div/div[2]/div/label/input', senha)
        time.sleep(1.5)
        page.locator('xpath=//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)

        #Ir até o link
        page.goto(site + caminho)
        time.sleep(5)

        #Comentarios
        for i in range(qtd_comentarios):
            mensagem_exibida = randint(0,qtd_mensagem)
            delay_comentario = randint(7,20)
            delay_publicar = randint(2,5)
            #Digita o comentario
            page.get_by_placeholder('Adicione um comentário...').fill(mensagem[mensagem_exibida])
            time.sleep(delay_publicar)
            #Aperta em publicar
            page.get_by_text('Publicar').click()
            time.sleep(delay_comentario)

            tempo_comentarios += delay_comentario
            tempo_comentarios += delay_publicar
        
        time.sleep(5)
        break

    mintuos = tempo_comentarios // 60
    segundos = tempo_comentarios % 60

    print(f'O login {login} teve {qtd_comentarios} comentários e levou {mintuos} minutos e {segundos} segundos.')
    total_comentarios += qtd_comentarios
    total_minutos += mintuos
    total_segundos += segundos

print(f'Foram feitos no total {total_comentarios} comentários, e levou cerca de {total_minutos} minutos.')
