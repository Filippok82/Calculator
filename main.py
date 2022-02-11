import controller

select = input('Для вычисления комплексных чисел введите  1, для рациональных введите 2:')

if select == '1':
    controller. calc_complex()
if select == '2':
    controller. calc_fract()