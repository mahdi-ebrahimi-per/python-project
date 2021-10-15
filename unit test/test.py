

def sumN(x, y):
    return (x+y)

def same(x):
    return(x)

def equal(function, equalTo):
    return function == equalTo

# print(equal(sumN(32, 3), 15))

def funcReaction_ordinalNumberInput(functionName, arg_index = 0, number_range=(0, 100)):
        for i in range(number_range):
            print(same(i))


funcReaction_ordinalNumberInput(same, number_range=(10))