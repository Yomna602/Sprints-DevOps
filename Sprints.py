numList=[]
def my_function(numList):
    
    intList=[]
    floatList=[]
    strList=[]

    for i in numList:
        if type(i)==int:
            intList.append(i)
        elif type(i)==float:
            floatList.append(i)
        elif type(i)==str:
            strList.append(i)
            print (0)
    
    Total = 0
    Count = 0
    for numb in intList:
        if numb%2==0:
            Total=Total+numb
            Count=Count+1
            
        EvenAvg=Total/Count
    
    print("The Average of the Even Integers is",EvenAvg)
    print("The Maximum Float Number is",max((floatList))) 

nList=[10,21.1910,8,45.382,66,95.77,8]
my_function(nList)
