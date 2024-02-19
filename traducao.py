from translate import Translator

class Tradutor:
    #Realiza a tradução de mensagens para PT-BR
    def __init__(self):
        self.tradutor = Translator(to_lang="pt")

    def traduzir(self, frase):
        #traduz a frase para PT-BR
        traducao = self.tradutor.translate(frase)
        return traducao