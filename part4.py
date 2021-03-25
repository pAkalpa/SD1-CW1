# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1833487        
# Date: 23/03/2021

moduleT_count = 0
moduleR_count = 0
exclude_count = 0
progress_count = 0
total_count = 0

def Main():
    print('-'*60)
    print('Staff Version with Histogram\n')
    while True:
        ValidateInput()
        option = str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: "))
        print('')
        while option not in ['y','q']:
                print("Invalid Option! Please Enter 'y' or 'q'")
                option = str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: "))
                print('')
        else:
            if option == 'q':
                break
            else:
                pass
    HistogramGenerator()

def ValidateInput():
    range_credit_list = [0, 20, 40, 60, 80, 100, 120]
    global total_count
    while True:
        level_credit_list = []
        while True:
            try:
                pass_credit = int(input('Enter your total PASS credits: '))
                if pass_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')

        while True:
            try:
                defer_credit = int(input('Enter your total DEFER credits: '))
                if defer_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        while True:
            try:
                fail_credit = int(input('Enter your total FAIL credits: '))
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
    
    total_count += 1
    Logic(level_credit_list)

def Logic(lct):
    global progress_count, moduleT_count, moduleR_count, exclude_count
    if (lct[0] == 0 and lct[1] <= 40) or (lct[0] == 20 and lct[1] <= 20) or (lct[0] == 40 and lct[1] == 0):
        message = 'Exclude'
        exclude_count += 1
    elif (lct[0] == 0 and lct[1] >= 60) or (lct[0] == 20 and lct[1] >= 40) or (lct[0] == 40 and lct[1] != 0) or (lct[0] == 60) or (lct[0] == 80):
        message = 'Do not progress - module retriever'
        moduleR_count += 1
    elif (lct[0] == 100):
        message = 'Progress (module trailer)'
        moduleT_count += 1
    elif (lct[0] == 120):
        message = 'Progress'
        progress_count += 1
    print(message)

def HistogramGenerator():
    print('-'*60)
    print(f'''Vertical Histogram\nProgress {progress_count} | Trailer {moduleT_count} | Retriever {moduleR_count} | Excluded {exclude_count}''')
    space2 = " "*6
    space1 = " "*5
    p_outcome = [progress_count,moduleT_count,moduleR_count,exclude_count]

    # ref: AllTech(2018). console horizontal histogram in python 😀.Available at:https://www.youtube.com/watch?v=h_qlWgIvOZo (Accessed: 25 March 2021).
    for i in p_outcome:
        while not all (i <= 0 for i in p_outcome):
            toPrint = ''
            for j in range(4):
                if p_outcome[j] > 0:
                    toPrint += space1+'*\t'
                    p_outcome[j] -= 1
                else:
                    toPrint += space1+'\t'+space2
            print(toPrint)

    print(f'{total_count} outcomes in total.')
    print('-'*60)

Main()