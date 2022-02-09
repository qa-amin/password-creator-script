import string
import random
import argparse


def creat_password(length, digit=False, lower=False, upper=False, pun=False):

    password = ''

    if digit:
        password += string.digits

    if lower:
        password += string.ascii_lowercase

    if upper:
        password += string.ascii_uppercase

    if pun:
        password += string.punctuation
    
    if password == '':
        password = string.digits

    random_letters = random.choices(password, k=length)

    password = ''.join(random_letters)

    return password

parse = argparse.ArgumentParser()

parse.add_argument(
    'length', type=int, help='length of password')

parse.add_argument(
    '-d', '--digit', help='length of password', action='store_true')

parse.add_argument(
    '-l', '--lower', help='length of password', action='store_true')

parse.add_argument(
    '-u', '--upper', help='length of password', action='store_true')

parse.add_argument(
    '-p', '--pun', help='length of password', action='store_true')

args = parse.parse_args()

print(creat_password(
    args.length, args.digit, args.lower, args.upper, args.pun
    ))
