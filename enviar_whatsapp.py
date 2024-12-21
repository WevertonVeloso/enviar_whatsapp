#para executar o script via ssh utilize o comando xvfb-run ~/faz-script/bin/python3 enviar_whatsapp.py
#precisa instalar o xvfb.

import os
from random import randint, choice
import pywhatkit as kit

mensagens = [
    "meu amor! Que seu dia seja cheio de luz e alegria. 🌞❤️",
    "Você é o meu porto seguro, minha paz e meu amor eterno. 🥰",
    "Só queria te lembrar de como sou grato por ter você na minha vida. 💕",
    "Você é meu sonho realizado e a razão da minha felicidade. 🌟",
    "Te amo mais do que as palavras podem expressar. Obrigado por ser você! 🌹",
    "Espero que saiba que, não importa o que aconteça, sempre estarei ao seu lado. 🤗",
    "Você faz meu coração bater mais forte todos os dias. 💓",
    "Minha vida ficou muito mais bonita desde que você chegou. 🌈",
    "Não existe lugar no mundo onde eu preferiria estar do que ao seu lado. 🌍",
    "Você é minha inspiração diária. Obrigado por me tornar uma pessoa melhor. 💌",
    "Cada momento com você é um presente que guardo no coração. 🎁",
    "Você ilumina minha vida como o sol ilumina a manhã. ☀️",
    "Te amo hoje, amanhã e para sempre. Nada mudará isso. 🕊️",
    "Se eu tivesse que escolher novamente, escolheria você mil vezes. ❤️",
    "Minha vida é completa porque você faz parte dela. Obrigado por existir. 🌹",
    "Eu sou o que sou hoje por causa do amor que você me dá. Te amo! 💖",
    "A cada dia que passa, meu amor por você cresce ainda mais. 🌱",
    "Você faz até os dias comuns parecerem extraordinários. 🌟",
    "Te amar é a coisa mais fácil e natural do mundo. 😘",
    "Meu coração pertence a você, hoje e sempre. 💕",
    "Mal posso esperar para te abraçar novamente. Sentir sua presença é meu maior conforto. 🤗",
    "Você é a melhor parte de mim. Te amo infinitamente. 💞",
    "Nada me faz mais feliz do que ver o seu sorriso. Você ilumina tudo ao seu redor. 🌻",
    "Obrigado por ser minha parceira de vida e minha melhor amiga. 👫❤️",
    "Com você, eu aprendi o verdadeiro significado de amor e felicidade. 🌺",
    "Meu dia melhora só de ouvir a sua voz. Você é meu refúgio. 🎶",
    "Nenhuma palavra pode descrever o quanto você é importante para mim. 🌸",
    "Você é a resposta para todas as minhas orações. Te amo eternamente. 🙏",
    "Cada momento ao seu lado é um pedaço do paraíso. 🌈",
    "Não existe ninguém no mundo que eu ame mais do que você, apenas elisa. ❤️",
    "Obrigado por ser minha rocha, meu apoio e meu tudo. 🪨",
    "Minha vida é muito melhor porque você está nela. Te amo demais. 💖",
    "Você é o segundo maior presente que Deus poderia ter me dado. Obrigado por tudo. 🎁",
    "Só de pensar em você, meu coração se enche de alegria. 💓",
    "Te amar é a melhor decisão que já tomei na minha vida. 💍",
    "Você é minha alma gêmea, meu destino e meu amor eterno. 🌟",
    "Quando penso em você, só consigo sentir gratidão. Você é tudo pra mim. 🌹",
    "Meu amor por você é infinito, como as estrelas no céu. 🌌",
    "Estar com você é como estar em casa, onde meu coração pertence. 🏡",
    "Você e elisa são a razão pela qual acordo todos os dias com um sorriso. 😊"
]

os.environ["DISPLAY"] = ":0"
NUMERO = os.getenv("NUMERO") # numero do destinatário seguindo o formato +5531999999999


def enviar_mensagem(HORA, MINUTO, MENSAGEM):
 

 try:
     kit.sendwhatmsg(NUMERO, MENSAGEM, HORA, MINUTO, wait_time=120)
     print("Mensagem enviada com sucesso!")
 except Exception as e:
     print(f"Erro ao enviar mensagem: {e}")

while True:
 MENSAGEM = choice(mensagens)
 HORA = randint(8, 17)
 MINUTO = randint(10, 30)

 if __name__ == "__main__":
  enviar_mensagem(HORA, MINUTO, MENSAGEM)

 os.system("sleep 300")
 os.system("kill -9 $(pidof firefox-esr)")
