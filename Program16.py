logicgate = input('What logic gate would you like? ').upper()
input1 = int(input('What is the first input? '))
input2 = int(input('What is the second input? '))
def OR(in1, in2):
    if in1 or in2 == 1:
        output = 1
    else:
        output = 0
    return output
def AND(in1,in2):
    if in1 and in2 == 1:
        output = 1
    else:
        output = 0
    return output
def XOR(in1,in2):
    if in1 == in2:
        output = 0
    else:
        output = 1
    return output
def NOR(in1, in2):
    if in1 or in2 == 1:
        output = 0
    else:
        output = 1
    return output
def NAND(in1,in2):
    if in1 and in2 == 1:
        output = 0
    else:
        output = 1
    return output
if logicgate == 'OR':
    print('Result =', OR(input1, input2))
elif logicgate == 'AND':
    print('Result =', AND(input1, input2))
elif logicgate == 'XOR':
    print('Result =', XOR(input1, input2))
elif logicgate == 'NAND':
    print('Result =', NAND(input1, input2))
elif logicgate == 'NOR':
    print('Result =', NOR(input1, input2))