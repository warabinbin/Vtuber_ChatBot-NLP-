from janome.tokenizer import Tokenizer
import json,os
from markov_test import test
import re
import libmstdn


text_file = 'SigureUi.txt'
json_file = 'Vtuber_markov.json'

def tokenize(text):
    t = Tokenizer()
    lines = text.split('\n')
    words = ' '.join(lines)
    tokens = t.tokenize(words)
    markov_dic = make_markov_dic(tokens)

    return markov_dic

def make_markov_dic(tokens):
    tmp = ['@']
    dic = {}
    for token in tokens:
        word = token.base_form
        if word == '　' or word == ' ' or word == '「' or word == '」' or word == '\n':
            continue
        tmp.append(word)
        if len(tmp) < 3:
            continue
        if len(tmp) > 3:
            tmp = tmp[1:]
        word1, word2, word3 = tmp
        if not word1 in dic:
            dic[word1] = {}
        if not word2 in dic[word1]:
            dic[word1][word2] = {}
        if not word3 in dic[word1][word2]:
            dic[word1][word2][word3] = 0
        dic[word1][word2][word3] += 1
        if word == '。':
            tmp = ['@']
            continue

    return dic


# 設定
HOST = "memphis.ibe.kagoshima-u.ac.jp"
TOKEN = "cdb1f80db7498a9d6e11a9d5e8cbaa3cb4ee6d9a8a7c71c45e6ed580a469736d"

# 正規表現
def remove_html_tags(content):
    return re.sub("<[^>]*>", "", content).strip()

# id判別
def is_to_me(status, my_id):
    for mention in status["mentions"]:
        if mention["id"] == my_id:
            return True
        return False

# リプ生成
def generate_reply(status, my_name):
    if not os.path.exists('../src/' + json_file):
        try:
            bindata = open('../src/' + text_file, 'rb').read()
            text = bindata.decode('utf-8')
        except Exception as e:
            print('error!',e)
            exit(0)

        markov_dic = tokenize(text)
        json.dump(markov_dic, open('../src/' + json_file, 'w', encoding='utf-8'))
    else:
        markov_dic = json.load(open('../src/' + json_file, 'r'))

    received_text = remove_html_tags(status["content"])
    toot_from = status["account"]["username"]

    if "!p" in received_text:
        return "\n" + test(markov_dic)
    else:
        return "\n" + "ごめんなさい, よくわかりません"

# Main
api = libmstdn.MastodonAPI(mastodon_host=HOST, access_token=TOKEN)

account_info = api.verify_account()
my_id = account_info["id"]
my_name = account_info["username"]
print("Started bot, name: {}, id: {}".format(my_name, my_id))

stream = api.get_user_stream()
for status in stream:
    if is_to_me(status, my_id):
        received_text = remove_html_tags(status["content"])
        toot_id = status["id"]
        toot_from = status["account"]["username"]
        print("received from {}: {}".format(toot_from, received_text))

        reply_text = "@{} {}".format(toot_from, generate_reply(status, my_name))
        api.toot(reply_text, toot_id)
        print("post to {}: {}".format(toot_from, reply_text))


