#TODO: calculator with nested expressions [using parenthesis]
import re


print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""

    # if there has been a previous calculation, use it as prompt
    if previous == 0:
        equation = input("Enter equation")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        # eval is DANGEROUS -> interprets python code too
        # use re first to remove anything that is not a number or symbol
        equation = re.sub('[a-zA-Z,.:()+" "]', '', equation)

        if previous == 0
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while run:
        perform_math()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
