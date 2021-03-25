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
    print('Horizontal Histogram')
    print(f"progress {progress_count}\t: {'*'*progress_count}")
    print(f"Trailer {moduleT_count}\t: {'*'*moduleT_count}")
    print(f"Retriever {moduleR_count}\t: {'*'*moduleR_count}")
    print(f"Excluded {exclude_count}\t: {'*'*exclude_count}\n")
    print(f'{total_count} outcomes in total.')
    print('-'*60)

Main()