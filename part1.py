# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1833487        
# Date: 23/03/2021

def main():
    level_credit_list = []

    print('-'*60)
    pass_credit = int(input('Please Enter Your credits at pass: '))
    defer_credit = int(input('Please Enter Your credits at defer: '))
    fail_credit = int(input('Please Enter Your credits at fail: '))
    
    level_credit_list.extend([pass_credit, defer_credit, fail_credit])
    message = logic(level_credit_list) 
    
    print(message)
    print('-'*60)

def logic(lct):
    if (lct[0] == 0 and lct[1] <= 40) or (lct[0] == 20 and lct[1] <= 20) or (lct[0] == 40 and lct[1] == 0):
        message = 'Exclude'
    elif (lct[0] == 0 and lct[1] >= 60) or (lct[0] == 20 and lct[1] >= 40) or (lct[0] == 40 and lct[1] != 0) or (lct[0] == 60) or (lct[0] == 80):
        message = 'Do not progress - module retriever'
    elif (lct[0] == 100):
        message = 'Progress (module trailer)'
    elif (lct[0] == 120):
        message = 'Progress'
    return message

main()
