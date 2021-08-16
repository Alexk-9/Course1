import re

RE_EMAIL = re.compile(r'(?P<username>[\w.-]+)@(?P<domain>[\w.-]+\.[\w.-]+)')


def email_parse(email_address):
    if RE_EMAIL.match(email_address):
        return print(RE_EMAIL.match(email_address).groupdict())
    else:
        raise AttributeError(f'Wrong e-mail: {email_address}')


if __name__ == '__main__':
    while True:
        name = input('Введите e-mail:\n')
        try:
            email_parse(name)
        except AttributeError as err:
            print(err)
        break
