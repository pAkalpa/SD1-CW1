# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1833487        
# Date: 23/03/2021
def Main():
    print('-'*60)
    lct = ValidateInput()
    message = Logic(lct)
    print(message)
    print('-'*60)

def ValidateInput():
    range_credit_list = [0, 20, 40, 60, 80, 100, 120]

    while True:
        level_credit_list = []
        while True:
            try:
                pass_credit = int(input('Please Enter Your credits at pass: '))
                if pass_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            

            except ValueError:
                print('Integer required\n')

        while True:
            try:
                defer_credit = int(input('Please Enter Your credits at defer: '))
                if defer_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        while True:
            try:
                fail_credit = int(input('Please Enter Your credits at fail: '))
                if fail_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        level_credit_list.extend([pass_credit,defer_credit,fail_credit])            
        if sum(level_credit_list) == 120:
            break
        else:
            print('Total incorrect\n')
            level_credit_list.clear
    return level_credit_list

def Logic(lct):
    if (lct[0] == 0 and lct[1] <= 40) or (lct[0] == 20 and lct[1] <= 20) or (lct[0] == 40 and lct[1] == 0):
        message = 'Exclude'
    elif (lct[0] == 0 and lct[1] >= 60) or (lct[0] == 20 and lct[1] >= 40) or (lct[0] == 40 and lct[1] != 0) or (lct[0] == 60) or (lct[0] == 80):
        message = 'Do not progress - module retriever'
    elif (lct[0] == 100):
        message = 'Progress (module trailer)'
    elif (lct[0] == 120):
        message = 'Progress'
    return message

Main()