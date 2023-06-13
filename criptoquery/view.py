
def test_input(list_of_valid_inputs, input_question):
    list_of_valid_inputs = list(map(lambda x: x.upper(), list_of_valid_inputs))
    str_input = input(input_question).upper()
    while str_input not in list_of_valid_inputs:
        print('Debe ser una de las siguientes opciones', list_of_valid_inputs)
        str_input = input(input_question)
    return str_input

def output(status, data, code, cripto, fiat):
    if status == True:
        print(f'1 {cripto} vale {data:.2f} {fiat}')
    else:
        print("|", code, "|\n", data)
