import string
from random import *

def gen_pass():
    pass_min = 16
    pass_max = 16
    all_char = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_char) for x in range(randint(pass_min, pass_max)))
    return password


passwd_var = gen_pass()
