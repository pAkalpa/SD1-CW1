# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1833487        
# Date: 23/03/2021

moduleT_count = 0
moduleR_count = 0
exclude_count = 0
progress_count = 0
total_count = 0

pass_credit = 0
defer_credit = 0
fail_credit = 0

dataset = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20],[40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]

def Main():
    print('-'*60)
    print('Staff Version with Histogram\n')
    DirectInput()
    HistogramGenerator()

def ValidateInput():
    range_credit_list = [0, 20, 40, 60, 80, 100, 120]
    global total_count
    while True:
        level_credit_list = []
        while True:
            try:
                if pass_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')

        while True:
            try:
                if defer_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        while True:
            try:
                if fail_credit in range_credit_list:
                    break
                else:
                    print('Out of range\n')
            except ValueError:
                print('Integer required\n')
        
        level_credit_list.extend([pass_credit,defer_credit,fail_credit])
        # print(sum(level_credit_list)) # for debugging Purpose         
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
    print()
    print('-'*60)
    print('Horizontal Histogram')
    print(f"progress {progress_count}\t: {'*'*progress_count}")
    print(f"Trailer {moduleT_count}\t: {'*'*moduleT_count}")
    print(f"Retriever {moduleR_count}\t: {'*'*moduleR_count}")
    print(f"Excluded {exclude_count}\t: {'*'*exclude_count}\n")
    print(f'{total_count} outcomes in total.')
    print('-'*60)

def DirectInput():
    global pass_credit, defer_credit, fail_credit
    for i in range(len(dataset)):
        pass_credit = dataset[i][0]
        defer_credit = dataset[i][1]
        fail_credit = dataset[i][2]
        ValidateInput()

Main()