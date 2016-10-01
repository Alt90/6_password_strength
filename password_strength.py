import sys
import string

from random import choice


password_blacklist = ['123456',
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


def if_not_simbol_in_password(password, simbpl_list):
    for simbol in simbpl_list:
        if (simbol in password):
            return False
    return True


def get_password_strength(password):
    if (password in password_blacklist):
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
    if (if_not_simbol_in_password(password, ['$', '@', '#'])):
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
