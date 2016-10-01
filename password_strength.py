import sys
import string

from random import choice


bad_password = ['123456',
                'password',
                '12345678',
                'qwerty',
                '12345',
                '123456789',
                'football',
                '1234',
                '1234567',
                'baseball',
                'welcome', ]

personal_information = ['BMSTUfn11',
                        'fn11BMSTU07',
                        'BMSTUfn11199013', ]


def get_password_strength(password):
    if (password in bad_password):
        return 1
    if (len(password) < 8):
        return 2
    if (password.isdigit()):
        return 3
    if (password.isalpha()):
        return 4
    if (password.islower()):
        return 5
    if (password.isupper()):
        return 6
    if (password.startswith('qwerty')):
        return 7
    if (password in personal_information):
        return 8
    if (not ('$' in password) or ('@' in password) or ('#' in password)):
        return 9
    return 10


def generate_password(length=10):
    chars = string.ascii_letters + string.digits + '@#$'
    return ''.join(choice(chars) for _ in range(length))


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Password don't enter")
        print("Example: %s" % generate_password())
        exit()
    print(u' Class password is %s' % get_password_strength(str(sys.argv[1])))
