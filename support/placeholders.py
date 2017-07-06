import random

placeholders = {
    '<random>'      : random.randint(0, 10000),
    '<random_email>': 'r2d2+{}@gmail.com'.format(random.randint(0, 1000)),

    '<default_user>': 'vasya',
}