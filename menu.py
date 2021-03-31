import part1 #import part1.py
import part2 #import part2.py
import part3 #import part3.py
import part4 #import part4.py
import part5 #import part5.py

def Main():
    pass

def menuInputValidation():
    while True:
        pass

def MenuUI():
    space1 = ' '*2 # no of spaces
    menuItemlist = ['Progression Outcome Predictor','Student Version',"Student Version (Validation)","Staff Version with Histogram",
                    "Vertical Histogram (optional extension)","Alternative Staff Version (optional extension)",
                   "Q/q","Exit Program"] # this list contains all the menu items
    print(f"+{'-'*55}+\n|\t{menuItemlist[0]}\t|\n+{'-'*5}+{'-'*49}+".expandtabs(14))
    print(f"|{space1 + '1' + space1}|{space1 + menuItemlist[1]}{' '*32}|\n|{space1 + '2' + space1}|{space1 + menuItemlist[2]}{' '*19}|")
    print(f"|{space1 + '3' + space1}|{space1 + menuItemlist[3]}{' '*19}|\n|{space1 + '4' + space1}|{space1 + menuItemlist[4]}{' '*8}|")
    print(f"|{space1 + '5' + space1}|{space1 + menuItemlist[5]} |\n| {menuItemlist[6]} |{space1 + menuItemlist[7]}{' '*35}|")
    option = str(input(f"+{'-'*5}+{'-'*49}+\nPlease Select an Option:"))

Main()