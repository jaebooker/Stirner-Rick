# compose_flask/app.py
from flask import Flask
from redis import Redis
from flask import render_template
from stirner_chain import *
import random
import re

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

word = ['One', 'Wave', 'Two', 'Wave', 'Red', 'Wave', 'Blue', 'Wave']
with open('./stirner.txt') as w:
    stirner_text = w.read()
with open('./trends.txt') as w:
    trend_text = w.read()
trend_list = trend_text.split()
word_list = re.split("\W*[^\'\w+\']", stirner_text)
with open('./rick_lines.csv') as input_file:
    text_list = input_file.read()
    # lines = [line.split(",", 2) for line in input_file.readlines()]
    # text_list = [" ".join(line) for line in lines]
#rick_roll = re.sub("^\d+\s|\s\d+\s|\s\d+$", "", text_list)
rick_rolled = re.split("\W*[^\'\w+\']", text_list)
def histogram(words):
    #words_list = re.split("(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", words)
    #words_list = re.split("\W*[^\'\w+\']", words)
    #thanks to Martijn Pieters for the above split
    word_dictionary = {}
    counter = len(words)
    i = 0
    while i < counter:
        word_dictionary[words[i]] = 1
        n = i+1
        while n < counter:
            if words[i] == words[n]:
                word_dictionary[words[i]] += 1
                words.pop(n)
                counter -= 1
                n -= 1
            n += 1
        i += 1
    return word_dictionary

def stirner_speaks(stirner_words, trend_words):
    trend_word = stirner_text[random.randrange(0,len(trend_words))]
    stirner_sentence = markdown2(stirner_words, 20)
    stirner_string = ""
    for i in stirner_sentence:
        stirner_string += " "
        stirner_string += i.lower()
    stirner_string += " "
    stirner_string += trend_word
    return stirner_string

@app.route('/')
def hello():
    redis.incr('hits')
    this_string = stirner_speaks(rick_rolled, word_list)
    return render_template('index.html', message=this_string)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
