mylist = [1,25,2,26,95,10,85,4]
# sortedlist = []
# largest = 0

# # optimise 1
sortedlist = [i for i in mylist if i % 5 == 0]
        
# example = 5

# def ab():
#     hello = 5


# def find_largest():
#     global largest
#     global secondlargest
#     for index,value in enumerate(sortedlist):
#        if value > largest:
#          largest = value
       
#        if index == len(sortedlist) - 1:
#           sortedlist.remove(largest)
#           for i in sortedlist:
#               if i > secondlargest:
#                   secondlargest = i
          
# find_largest()
# print(secondlargest)

def get_second_and_first_largest(sortedlist):
    largest = secondlargest = 0
    
    for i in sortedlist:
        if i > largest:
            secondlargest = largest
            print("this is before define largest", largest)
            largest = i
            print("this is after largest",largest)
        elif i > secondlargest and i != largest:
            print("this is largest value",i)
            secondlargest = i
    
    return largest,secondlargest


largest,secondlargest= get_second_and_first_largest(sortedlist)
            
# print("this is largest and second largest",largest,secondlargest)

class Private:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
person = Private('shubham',18)
print(person)