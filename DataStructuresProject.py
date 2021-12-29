#login
accounts = {}
def loginMenu():
    while True:
        print("\n*============ LOGIN PAGE ============*\n")
        print("[1]Register  [2]Login  [3]Exit Program")
        choice = input("\nChoose an operation: ")
        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nGoodbye!\n")
            break

        else:
             print("\n!-Invalid input.\n")
       
def login():
    print("\n>> LOGIN")
    while True:
        login = input("Username: ")
        password = input("Password: ")
        hashed_pass = hash(password)

        if login in accounts and accounts[login] == hashed_pass:
            print("\nLogin Succesful!\n")
            main()
            break
            
        elif login in accounts and accounts[login] != hashed_pass:
            print("\n!-Password is incorrect, please try again.\n")
            continue
            
        elif login not in accounts:
            print("\n!-Account does not exist.")
            break

def register():
    print("\n>> REGISTRATION")
    createUser = input("Enter username: ")
    
    if createUser in accounts:
        print("\n!-Username already exists!\n")
        
    else:
        while True:
            createPass = input("Enter password: ")
            if len(createPass) >= 6 and len(createPass) <= 10:
                hashPass = hash(createPass)
                accounts[createUser] = hashPass
                print("\nAccount succesfully created!\n")
                break
            else:
                print("\n!-Please enter a password of 6-10 characters.\n")
                continue

#STACK
stack=[]

for i in range(1,101):
    stack.append(i)
    
#QUEUE
#structure of node for queue
class node:
    def __init__(self,customer=None):
        self.customer=customer
        self.prev=None
        self.next=None
        self.nextval=None
class queue:
    def __init__(self):
        self.head = None
        self.last = None
   
    def enqueue(self, customer):
        
        if self.last is None: 
            self.head =node(customer) 
            self.last =self.head 
        else: 
            self.last.next = node(customer) 
            self.last.next.prev=self.last 
            self.last = self.last.next
        print("\n")
    def dequeue(self): 
        if self.head is None: 
            return None
        else: 
            temp= self.head.customer 
            self.head = self.head.next
            self.head=None
            return temp
        print("\n")
        
    def printQueue(self): 
           
        print("The customer names are:") 
        temp=self.head        
        if self.head is None:
            print("Queue is empty")
        else:
            while temp is not None: 
                print(temp.customer,end=",") 
                temp=temp.next
        print("\n")
            

#LINKEDLIST        
#structure of node for (add,delete,edit products)
class Node:
    def __init__(self,ID=None,name=None,price=None,quantity=None):
        self.ID=ID
        self.name = name
        self.price= price
        self.quantity= quantity
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,ID,name,price,quantity):
        new_node = Node(ID,name,price,quantity)       
        new_node.nextval = self.head
        self.head= new_node
        
    def printList(self):
        count=0
        n = self.head
        
        print("----------------------INVENTORY----------------------\n")
        print("ID\t\t\tPRODUCT NAME\t\tPRICE\t\tQUANTITY")
        print("==================================================================================================")
        while (n!=None): 
            print(n.ID, "\t\t\t",n.name,"\t\t",n.price,"\t\t",n.quantity)
            n = n.nextval
            count=count+1
        print("NUMBER OF PRODUCTS: ",count)
        return count

    def search(self, x):
        count=1
        current = self.head 
        while current != None: 
            if current.ID == x: 
                break
            else:
                count=count+1
                current = current.nextval
        return count
        
    def addItem(self):
        try:
            prodID=input("Enter the product ID: ")
            assert len(prodID)>0
            Name=input("Enter product name: ")
            assert len(Name)>0
            Price=float(input("Enter the product price: "))
            assert Price >0
            quantity=int(input("Enter product quantity: "))
            assert quantity >0
            self.insert(prodID,Name,Price,quantity)    
            print("The product was succesfully added")
        except ValueError :
            print("Incorrect input")
        except AssertionError :
            print("Invalid Input")
        
                         
    def delItem(self):

        count= self.printList() #number of products
        current=self.head
        pre=self.head
        if current==None:
            print("List is empty")
        else:
            deleteItem=input("Enter the ID of the product you want to delete: ")
            pos=int(self.search(deleteItem)) #if item is found, it will return the position

            if current.ID==deleteItem:  
                    self.head = current.nextval
                    current = None
                    print("The product is deleted")
            elif pos <= count :
                while current.ID!=deleteItem:
                    pre=current
                    current=current.nextval
                
                pre.nextval=current.nextval
                      
                print("The product is deleted")
            else:
                print("Item not found")
          
              
    def editItem(self):
        if self.head==None:
            print("List is empty")
        
        else:
            current=self.head
            c=int(self.printList())
            item=input("Enter the ID of the product you want to edit: ")
            
            position=self.search(item)
            if position<=c:
                while current.ID !=item:
                    current=current.nextval
                
                try:
        
                    newID=input("Enter new product ID: ")
                    assert len(newID) >0
                    newName=input("Enter new product name: ")
                    assert len(newName) >0 
                    newPrice=float(input("Enter new product price: "))
                    assert newPrice >0 
                    newQuantity= int(input("Enter new quantity: "))
                    assert newQuantity >0
                    current.ID=newID       
                    current.name=newName         
                    current.price=newPrice 
                    current.quantity=newQuantity
                
                except ValueError:
                    print("Incorrect input")
                except AssertionError:
                    print("Invalid input")
            else:
                print("Item not found")
                            
                            
        
        
llist=LinkedList()
q=queue()


def manage():
    
    print("--------------------MANAGE STORE----------------------")
    while True:
        choice=input("\n\n1-Add Item\n2-Delete Item\n3-Edit Product Information\n4-View Products\n5-View List Costumers\n6-Delete Customers\n7-Delivery Location\n8-Back to main menu\n")
    
        if choice == "1":
            llist.addItem()
        if choice == "2":
            llist.delItem()
        if choice == "3":
            llist.editItem()    
        if choice == "4":
            llist.printList()
        if choice == "5":     
            print("||============================CUSTOMER NAMES========================||")
            q.printQueue()
        if choice == "6":
            print("||============================CUSTOMER NAMES========================||")
            q.dequeue()
            q.printQueue()
        if choice == "7":
            ShippingCost()
        if choice == "8":
            break
#ORDER        
def order(): 
    stack.pop()
    print("-------------------------ORDER------------------------")
    
    products = []
    i = 0
    pay = 0    
    if llist.head == None:
        print("There are no items available. ")
    elif llist.head.nextval == None:
        itemNum=1
    else:
        itemNum = int(input("Input the number of items that you would like to purchase: "))      
    print("\n")
    count=llist.printList()
    while i < itemNum:
        current = llist.head
        pos = 0
        newID = input("Input the item ID of the item you want to purchase: ")
        pos = llist.search(newID)
        if pos <= count:
            while current.ID != newID:
                current = current.nextval
            try:
                quant = int(input("Input desired quantity: "))
                assert quant >0 and quant <= current.quantity
                products.append(current.name)
                pay = int(pay) + (int(current.price)*quant)
                current.quantity = current.quantity - quant
            except AssertionError:
                print("Invalid quantity")
            except ValueError:
                print("Invalid Input")
        
        else:
            print("Item is not available in our store. ")
        i+=1
    if pay <= 0  :
        print("Customer was not added")
    else:
        location=ShippingCost()
        pay = int(pay) + location
        customer = input("Input your name: ")
        q.enqueue(customer)
        print("Items purchased: ")
        for x in products:
            print(x)
        print("══════════════ TOTAL PRICE =",pay,"════════════════")
        
#SHORTESTPATH
def ShortestPath(graph,startingPoint,destination,Vertices=[],distance={},dicPredecessor={}):
        
    if startingPoint == destination:
        path = []
        predecessor = destination
        while predecessor != None:
            path.append(predecessor)
            predecessor=dicPredecessor.get(predecessor,None)
        i=path[0]
        for index in range(1,len(path)):i = path[index]+'--->'+i 
        
        print("Shortest Path: " + i + ", Total Distance: "+str(distance[destination])+" kilometers.")
        cost = int(distance[destination])*2.5
        print("Shipping Cost: P", cost)
        condition = True

    else :     
        if not Vertices: 
            distance[startingPoint]=0
        
        for neighbor in graph[startingPoint] :
            if neighbor not in Vertices:
                new_distance = distance[startingPoint] + graph[startingPoint][neighbor]
                if new_distance < distance.get(neighbor,float('inf')):
                    distance[neighbor] = new_distance
                    dicPredecessor[neighbor] = startingPoint   
        Vertices.append(startingPoint)
        Unvisited={}
        
        for i in graph:
            if i not in Vertices:
                Unvisited[i] = distance.get(i,float('inf'))
                
        x=min(Unvisited, key=Unvisited.get)
        ShortestPath(graph,x,destination,Vertices,distance,dicPredecessor)

    finalCost = int(distance[destination])*2.5
    return finalCost
   


def ShippingCost():    
    graph = {'Cabuyao': {'Calamba':14}, 
            'Calamba': {'Cabuyao':14, 'Alaminos':31, 'Los Banos':23}, 
            'Alaminos': {'Calamba':31, 'San Pablo':7}, 
            'Los Banos': {'Calamba':23, 'Bay':8}, 
            'Bay': {'Los Banos':8, 'Calauan':11,'Victoria':20}, 
            'San Pablo': {'Alaminos':7,'Calauan':11,'Nagcarlan':21,'Majayjay':24}, 
            'Calauan': {'Bay':11,'San Pablo':11,'Victoria':13,'Nagcarlan':15},
             'Victoria':{'Bay':20,'Calauan':13,'Pila':7},
             'Nagcarlan':{'San Pablo':21,'Calauan':15,'Pila':13,'Liliw':9,'Sta Cruz':18},
             'Pila' : {'Victoria':7,'Nagcarlan':13,'Sta Cruz':7},
             'Liliw':{'Nagcarlan':9,'Magdalena':9,'Majayjay':5},
             'Sta Cruz':{'Pila':7,'Nagcarlan':18,'Magdalena':11,'Pagsanjan':6},
             'Magdalena':{'Sta Cruz':11,'Liliw':9},
                'Majayjay':{'Liliw':5,'Pagsanjan':22,'San Pablo':24},
             'Pagsanjan':{'Majayjay':22,'Sta Cruz':6}}
    
    print("List of available shipping destinations: \n")
    for key in graph:
        print(key)
    startLocation="Cabuyao"
    destination=input("\nInput Shipping Destination: ")
    
    if startLocation not in graph or destination not in graph:
        print("Invalid Input.\n")
        cost=0
        return cost
    elif(startLocation==destination):
        print("Shipping Cost: P10")
        cost = 10
        return cost
    else :
        cost = ShortestPath(graph,startLocation,destination)
        return cost
    
#MAIN MENU
def main():
    while True:
        print("\n     ┌───── •••• ─────┐\n          - MENU - \n     └───── •••• ─────┘")
        menu=input("1-MANAGE STORE 2-ORDER 3-BACK TO LOGIN PAGE\n")
        if menu =="1":
            manage()
        if menu=="2":
            if llist.head==None:
                print("No available products")
            else:
                print("\n╔════════════════╗\n|Order Number:",stack[-1],"\n╚════════════════╝")
                order()
        if menu =="3":
            break
        
print("    ──────▄▀▄─────▄▀▄\n    ─────▄█░░▀▀▀▀▀░░█▄\n    ─▄▄──█░░░░░░░░░░░█──▄▄\n    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")

loginMenu()

    
    
