# Sync_Intern-s_Python_Project-4
# Chatbot using Python

import re
import l_r as long


def msg_p(u_msg, r_words, One_ans=False, req_words=[]):
    msg_cert = 0
    has_req_words = True

    # It counts word in predefined message
    for w in u_msg:
        if w in r_words:
            msg_cert += 1

    # For % of recognised word in user's message
    per = float(msg_cert) / float(len(r_words))

    # For checking * words in string
    for w in req_words:
        if w not in u_msg:
            has_req_words = False
            break
    
    # It should have required words or One ans
    if has_req_words or One_ans:
        return int(per * 100)
    else:
        return 0


def chk_msg(msg):
    h_list = {}
    # It simplifies ans making 
    def ans(bot_ans, l_words, One_ans=False, req_words=[]):
        nonlocal h_list
        h_list[bot_ans] = msg_p(msg, l_words, One_ans, req_words)

    # About Answers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ans('Hello! Sir/Ma\'am nice to meet you. ', ['hello', 'hi', 'hey', 'sup', 'heyo'], One_ans=True)
    ans('See you Sir/Ma\'am!', ['bye', 'goodbye'], One_ans=True)
    ans('I\'m fine. What about you?', ['how', 'are', 'you', 'doing'], req_words=['how'])
    ans('You\'re welcome!', ['thank', 'thanks'], One_ans=True)
    ans('Thank you very much!', ['i', 'love', 'code', 'palace'], req_words=['code', 'palace'])
    


    # While long answers
    ans(long.advice, ['give', 'advice'], req_words=['advice'])
    ans(long.eat, ['what', 'you', 'eat'], req_words=['you', 'eat'])
    ans(long.info,['give','information','info'], req_words=['information'])

    perfect_match = max(h_list, key=h_list.get)
    return long.unknown() if h_list[perfect_match] < 1 else perfect_match

# Gettin the answer
def get_ans(u_ip):
    split_ans = re.split(r'\s+|[,;?!.-]\s*', u_ip.lower())
    ans = chk_msg(split_ans)
    return ans

# Let's ready to testing my Shreyu's Bot
while True:
    print('Shreyu\'s Bot : ' + get_ans(input('You : ')))