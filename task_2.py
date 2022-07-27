import math
def is_kvadart_meth():
    side = int(input("Type 1 side cm: "))
    Perimetr = side + side + side + side
    Plosha = side * side
    Diagonal = math.sqrt(2*side)
    print('\n',"Perimetr: ",Perimetr, '\n' ,"Plosha: ", Plosha, '\n', "Diagonal: ", Diagonal)

print(is_kvadart_meth())