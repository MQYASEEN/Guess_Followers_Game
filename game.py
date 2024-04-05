from art import logo,vs
import random
from data_format import data
import os
os.system("CLS")
print(logo)
score=0
should_continue=True
f_q=random.choice(data)

def get_data(question):
    """Extract data of question from dictonary"""
    name=question['name']
    description=question['description']
    location=question['country']
    return f'{name} {description} from {location}'
def compare(guess,f_f,s_f):
    """Compare Both Entities followers and find you choose correct answer or not"""
    if f_f>s_f:
        return guess=='a'
    else:
        return guess=='b'
while should_continue:
    s_q=random.choice(data)

    if f_q==s_q:
        f_q=random.choice(data)
    print(f'A.Compare {get_data(f_q)}')
    print(vs)
    print(f'B.Against {get_data(s_q)}')
    f_followers=f_q['follower_count']
    s_followers=s_q['follower_count']
    guess=input('Who has more followers on instagram A or B:').lower()
    check_answer=compare(guess,f_followers,s_followers)
    if check_answer:
        if guess=='a':
            f_q=f_q
        else:
            f_q=s_q
        score +=1
        os.system("CLS")
        print(logo)
        print(f"You are Right! You score is :{score}")
    else:
        should_continue=False
        os.system("CLS")
        print(f'You are Wrong ! You Final Score is {score}')