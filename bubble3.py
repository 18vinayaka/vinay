import random
import re
from collections import defaultdict

class MarkovChatbot:
    def __init__(self):
        self.model = defaultdict(list)
        self.start_words = []

    def train(self, text):
        sentences = re.split(r'[.!?]', text)
        for sentence in sentences:
            words = sentence.strip().split()
            if len(words) > 1:
                self.start_words.append(words[0])
                for i in range(len(words) - 1):
                    self.model[words[i]].append(words[i + 1])

    def generate_sentence(self):
        if not self.start_words:
            return "I don't know what to say yet! Train me with more words."
        word = random.choice(self.start_words)
        sentence = [word]
        while word in self.model and len(sentence) < 20:
            word = random.choice(self.model[word])
            sentence.append(word)
        return " ".join(sentence) + random.choice(['.', '!', '?'])

# Example usage
bot = MarkovChatbot()
training_text = "Hello there! How are you today? I love Python programming. Do you like coding?"
bot.train(training_text)

print("Chatbot: " + bot.generate_sentence())
