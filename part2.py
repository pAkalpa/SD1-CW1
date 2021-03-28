# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1833487        
# Date: 23/03/2021
def Main(): # Main function
    print('-'*60) # print dashed line 60char's long
    lct = ValidateInput() # store return value and call fuction
    message = Logic(lct) # store retun value and call funtion with parsing previous returned value
    print(message) # print returned values from Logic function
    print('-'*60) # print dashed line 60char's long

def ValidateInput(): # use Inputs and Validation function
    range_credit_list = [0, 20, 40, 60, 80, 100, 120] # declare list of valid input ranges

    while True:
        level_credit_list = [] # declare list to store user inputs
        while True:
            try:
                pass_credit = int(input('Please Enter Your credits at pass: ')) # take user input and assign it to a variable
                if pass_credit in range_credit_list:
                    break # if condition True: break loop
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')

        while True:
            try:
                defer_credit = int(input('Please Enter Your credits at defer: ')) # take user input and assign it to a variable
                if defer_credit in range_credit_list:
                    break # if condition True: break loop
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        while True:
            try:
                fail_credit = int(input('Please Enter Your credits at fail: ')) # take user input and assign it to a variable
                if fail_credit in range_credit_list:
                    break # if condition True: break loop
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        level_credit_list.extend([pass_credit,defer_credit,fail_credit]) # extend list by adding variables         
        if sum(level_credit_list) == 120:
            break # if condition True: break loop
        else:
            print('Total incorrect\n')
            level_credit_list.clear # if condition False: clear list
    return level_credit_list # return varible

def Logic(lct): # Logic Fuction with parsed list as parameter
    if (lct[0] == 0 and lct[1] <= 40) or (lct[0] == 20 and lct[1] <= 20) or (lct[0] == 40 and lct[1] == 0):
        message = 'Exclude' # if condtion True: assign string to variable
    elif (lct[0] == 0 and lct[1] >= 60) or (lct[0] == 20 and lct[1] >= 40) or (lct[0] == 40 and lct[1] != 0) or (lct[0] == 60) or (lct[0] == 80):
        message = 'Do not progress - module retriever' # if condtion True: assign string to variable
    elif (lct[0] == 100):
        message = 'Progress (module trailer)' # if condtion True: assign string to variable
    elif (lct[0] == 120):
        message = 'Progress' # if condtion True: assign string to variable
    return message # return varible

Main() # calls main function