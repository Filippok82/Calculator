

def entry(entry_type):
    choose_metod = 0
    if entry_type is complex:
        choose_metod = 1
        input_info ='комплексное число:'
    elif entry_type is float:
        choose_metod = 2
        input_info ='рациональное  число:'
    else:
        choose_metod = 0
        input_info ='операция(+-/*)'
    call={
        0: check_oper,
        1: check_complex,
        2: check_fraction,
    }
    while True:
        try:
            data = input(input_info)   
            return call[choose_metod](data)
        except Exception:
            continue
  

def check_complex(input):
    return complex(input)

def check_oper(input):    
    if input in ['+','-','*','/']:
        return str(input)
    else:
        return None

def  check_fraction(input):    
    return float(input)  


def exit(result):
    if type(result)== float:
        print(f'{result:.3f}')
    else:
        print(result)
    
