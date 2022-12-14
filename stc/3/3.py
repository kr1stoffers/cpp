class Node:
    def __init__(self, number = None):
        self.number = number
        self.next = None
        self.pref = None
        
    def add(self, number):
        if self.number is None:
            self.number = number
            return self
        
        newNode = Node(number)
        newNode.next = self
        self.pref = newNode
        return newNode
        
        
    def remove(self):
        if self.next is None:
            self.number = None
            return self
        
        self = self.next
        self.pref = None
        return self
        
myList = Node()

while True:
    print("1. Add node")
    print("2. Remove node")
    print("3. List view")
    print("4. Does list contain?")
    print("0. Exit")
    
    swt = input("Your choose: ")
    
    if swt == '1':        #Add node 
        number = input("Number: ")
        
        myList = myList.add(number)
        
    elif swt == '2':    #Remove node
        myList = myList.remove()
    
    elif swt == '3':    #List view
        chain = myList
        if chain.number == None:
            print("A hde? A net\n")
        else:
            print(chain.number)
            while chain.next:
                chain = chain.next
                print(chain.number)
            
    elif swt == '4':    #Does list contain
        search = input("Enter a node name: ")
        chain = myList
        while chain:
            if chain.number == search:
                print("Yea")
                break
            if chain.next == None:
                print("Nea")
                break
            chain = chain.next     
    else:
        break
