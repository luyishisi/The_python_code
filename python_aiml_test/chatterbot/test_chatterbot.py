from chatterbot import ChatBot
chatbot = ChatBot("chcc")

chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")
while(True):
    message = raw_input("you say: ")
    chatbot.get_response(message)
