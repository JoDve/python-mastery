'''Write a funcion name printTable() that takes a list of lists and display it 
 in a well-organized table with each column right- justified. 
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    ''' print the list of lists and don't return anything.'''
    for values in range(len(table[0])):
        y = ''
        # Add every values (index 0, index 1 and so on) of each list in each iteration 
        for index, items in enumerate(table):
            y += (table[index][values]).rjust(10)
        
        print(y)   

printTable(tableData)
