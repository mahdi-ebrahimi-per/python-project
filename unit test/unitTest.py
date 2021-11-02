import unittest
from colorama import Fore, Back, Style


class UnitTestTools(unittest.TestCase):

    def __init__(self):
        pass

    def equal(self, function, equalTo, PASS_FALED=True):
        
        if PASS_FALED:
            if function == equalTo:
                return (Fore.GREEN + "PASS" + Fore.RESET) 

            else:
                return (Fore.RED + "FALED" + Fore.RESET)

        return function == equalTo


    def funcReaction(self, functionName, *function_args):
            args = []
            for i in function_args:
                args.append(i)

            for i in range(len(args)):
                # print( functionName(i) )
                pass

#________________________


def sumN(x, y):
    return (x+y)

def same(x):
    return(x)



test = UnitTestTools()

print(test.equal( sumN(12, 3), 15))
print(test.equal(sumN(12, 3), 12))
print(test.equal(sumN(12, 3), 45))
print(test.equal(sumN(12, 3), 0))




# test.funcReaction(sum, [2, 5], [1 , 5])
    # 2 + 1 = 3
    # 2 + 5 = 7
    # 5 + 1 = 6
    # 5 + 5 = 10