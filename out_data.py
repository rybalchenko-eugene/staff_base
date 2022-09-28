from encodings import utf_8




def save_as_excel(lst):
    with open('dir1.csv', 'w', encoding="utf-8") as d:
        for i in lst:
            d.write(f'{i}')

def print_dir(lst, ID = None):
        if ID == None: 
            for line in lst: print(line) 
        else:
            print(lst[ID]) 


