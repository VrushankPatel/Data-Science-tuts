import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot', trainer=ChatterBotCorpusTrainer)
trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.english")
# trainer.train('/Users/vrushankpatel/Desktop/ml/vrp.yml')

# for files in os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/english'):
trainer.train(
    'chatterbot-corpus-master/chatterbot_corpus/data/english/vrp.yml')

while True:
    message = input("You : ")
    if message.strip() != "Bye" and message.strip() != "quit" and message.strip() != "get lost":
        reply = bot.get_response(message)
        print("ChatBot : ", reply)
    else:
        print("ChatBot : Bye")
        break
