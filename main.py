from desafio_rpa import Desafio

status_loop = 'ON'
state = 'INITIALIZATION'

bot = Desafio()


while status_loop=='ON':

    match state:
        
        case 'INITIALIZATION':   
            bot.acessa_site('https://rpachallenge.com/')
            state = 'GET'
            continue
        
        case 'GET':    
            dados = bot.download_arquivo()
            state = 'PROCESS'
            continue
        
        case 'PROCESS':
            bot.inicia_desafio()
            bot.inserindo_dados(dados)
            bot.captura_tempo()
            state = 'END'
            continue

        case 'END':
            bot.fecha_navegador()
            del bot
            status_loop ='OFF'
            continue

