from tkinter import *
import string as stg
import spacy as spy
from spacy.lang.pt.stop_words import STOP_WORDS

pont = stg.punctuation
stop_words = STOP_WORDS
stop_words
len(stop_words)

pln = spy.load('pt_core_news_sm')
def preprocessamento(texto):
  texto = texto.lower()
  documento = pln(texto)
  
  lista = []
  for token in documento:
    #lista.append(token.text)
    lista.append(token.lemma_)

  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pont]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
  return lista



actualMessage = ""


def analiseIa(message):
    if (message == "ola"):
        return "Olá, tudo bem?"
    else:
        return "Else"
    

def iaMessage(messageUser, iaWrite):
    iaWrite.insert("end","  I. A.: " + analiseIa(messageUser) + "\n")


def sendMessage(textSend, textWrite, message):
    textWrite.insert("end","Você: " + str(textSend.get("1.0","end-1c")) + "\n")
    message = str(textSend.get("1.0","end-1c"))
    print(message)
    print(type(message))
    textSend.delete("1.0","end")
    iaMessage(message, textWrite)


window = Tk()

txt = Text(window, height=5, width=30)
txt.pack()

btn = Button(window, text="Send", command=lambda: sendMessage(txt, txtMsg, actualMessage))
btn.pack()

txtMsg = Text(window, height=20, width=30)
txtMsg.pack()

window.mainloop()