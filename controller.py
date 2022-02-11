import users_interface
import complex_c
import fract_c
import logging


def calc_complex():
    number_1 = users_interface.entry(complex)
    number_2 = users_interface.entry(complex)
    oper = users_interface.entry(str)
    result = complex_c.calc1(number_1,number_2,oper)
    logging.logg(number_1, number_2, oper, result)
    users_interface.exit(result)


def calc_fract():
    number_1 = users_interface.entry(float)
    number_2 = users_interface.entry(float)
    oper = users_interface.entry(str)
    result = fract_c.calc1(number_1, number_2, oper)
    logging.logg(number_1, number_2, oper, result)
    users_interface.exit(result)
