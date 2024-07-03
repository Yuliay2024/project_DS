class Node:  

   
	def __init__(self, data):         
		self.data = data        
		self.prevNode = None         
		self.nextNode = None 

		
class Listnew:

     
	def __init__(self):         
		self.head = None         
		self.tail = None                
	
	def addNode(self, data): 
		newNode = Node(data)            
		if(self.head == None):                
			self.head = self.tail = newNode               
			self.head.prevNode = None               
			self.tail.nextNode = None           
		else:                
			self.tail.nextNode = newNode               
			newNode.prevNode = self.tail                 
			self.tail = newNode               
			self.tail.nextNode = None     
			
			
class Item:     


	def __init__(self, item):         
		self.item = item          
		

elements = Listnew()    

item_one = Item(15) 
item_two = Item(15)   
elements.push(item_one) 
elements.pop()  
elements.shift()  
elements.unshift(item_two)