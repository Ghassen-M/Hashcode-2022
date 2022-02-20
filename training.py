import os;
import itertools

def badPizza(pizza,l):
    for ingredient in pizza:
        if l.count(ingredient)==1:
            return True
    return False

with open('C:\\Users\\lenovo\\.vscode\\Hashcode\\a.txt') as f:
    lines = f.readlines()
    ing=[]
    for line in lines[1:]: 
        l=line.split()[1:]
        for i in l:
            ing.append(i)
    ingredientList=[]
    for i in ing:
        if i not in ingredientList:
            ingredientList.append(i)
    """ingredientList=list(dict.fromkeys([ingredient[0:] for line in lines[1:] for ingredient in line.split()[1:] ]))"""

    pizzas=[] 

    C=3
    allIngredients=len(ingredientList)+1
    for i in range(1, allIngredients):
        pizzas.extend([list(x) for x in itertools.combinations(ingredientList, i)])
    clientsFavList=[ line.split()[1:] for line in lines[1::2] ]
    clientsMehList=[ line.split()[1:] for line in lines[2::2] ]
    perfectPizza=[0,[]]
    for pizza in pizzas:
        potentialClients=0
        for clientCount in range(C):                 
            if badPizza(pizza,clientsMehList[clientCount])==False and set(clientsFavList[clientCount]).issubset(pizza):
                potentialClients+=1   
        if perfectPizza[0]<potentialClients:
            perfectPizza=[potentialClients,pizza]
    with open("C:\\Users\\lenovo\\.vscode\\Hashcode\\solution.txt", "w") as s:
        perfectIngredients=" ".join(perfectPizza[1])
        s.write(str(len(perfectPizza[1]))+" "+perfectIngredients)

