#made by deviousname
#goal: try and get out of Taco Place without making an error code!
#speedrunable coding game

class Taco_Place(): 
    def __init__(self):
        self.string_input = 0
        self.inventory = {"null":"item0"}
        self.inputs_load()
        self.string1 = ''
        self.cartlist = []
        self.cycles = 0
        self.init_vars(self.cycles)
        self.greet()
        self.customer()

    def inputs_load(self):
        self.dict1 = {
                      "apple":"self.fruit('apple')",
                      "orange":"self.fruit('orange')",
                      "berry":"self.fruit('berry')",
                      "cart":"self.cart()",
                      "empty":"self.cart()",
                      "command":"self.experiment_101()",
                      "dev":"print('made by deviousname')",
                      "custom":'self.custom_command()',
                      "?":"self.print_keys()",
                      "forge":"self.inventory.update({input(self.say):input(self.say)})",
                      "inventory":"print(self.inventory)",
                      "error":"print('Hmm, what could it mean?')",
                      }
        return self.dict1
    
    def print_keys(self):
        self.string1 = ''
        for key in self.dict1.keys():
            self.string1 = self.string1 + ' ' + key
        print (f'[Help Menu]: {self.string1}')
            
    def fruit(self, x1):
        self.cartlist.append(x1)
        print(f'Added {x1} to your [cart].')

    def experiment_101(self):
        for a in range(5):
            print(f'experiment passed x {a+1}')
            
    def custom_command(self):
        x = input("Command name? ")        
        y = int(input("How many lines? "))
        if y == 1:
            n = input("Command: ")
            self.dict1.update({x:eval("n")})
        else:
            print('try 1 line for now')
             
    def cart(self):
        if self.say == "cart":
            print(self.cartlist)
        if self.say == "empty":
            print('Cart emptying...')
            self.cartlist = []
            print('Done.')
        
    def init_vars(self, cycles):
        if cycles == 0:
            print('...initializing variables...')
            print("......press ? for help......")
            self.list0 = []
            self.cycles += 1
            print(self.greet())
        else:
            print('...variables already initialized!')
            print(self.list0)
            self.cycles += 1
            print(f'cycles: {self.cycles}')
            
    def greet(self):
        return "Hello, welcome to Taco Place, how may I assist thee?"

    def customer(self):
        self.say = input('Say: ')
        self.think()
        self.customer()
        
    def think(self):
        if self.say in self.dict1.keys():               
            new_command = self.dict1.get(self.say)
            try:
                eval(new_command)
            except Exception as e:
                print(f'Error Found: {e}')
        else:
            print(f'Did you say {self.say}?')
        self.customer()
        
Taco_Place()
