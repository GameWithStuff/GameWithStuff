print('Press enter to proceed')
input('0\n')
def fibonacci(oneLessThanN,twoLessThanN):
    input(str(oneLessThanN + twoLessThanN) + "\n")
    fibonacci(twoLessThanN, twoLessThanN+oneLessThanN)
fibonacci(1,0)