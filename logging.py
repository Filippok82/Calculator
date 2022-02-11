def logg(number_1,number_2, oper, result):
     with open('file_log.csv', 'a') as file:
        file.write(f'{number_1};{oper};{number_2};{result}\n')
