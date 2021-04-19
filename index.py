# Budget app 

#Creating of Budget class
class Budget:
      #Initializing Budget class
      def __init__(self, name):
          self.name = name
          self.balance = 0
          
      #Creating a deposit method   
      def deposit(self, amount):
         self.balance = amount
         outcome = '******************************************************\n'
         outcome += 'Your deposit request was successful\n'
         outcome += f'Your current account balance is ${self.balance} in {self.name} Budget \n'
         outcome += '******************************************************'
         return outcome
      
     # Creating a withdrawal method
      def withdrawal(self, amount):
          if (self.balance < amount):
              return 'Insufficient Funds, Kindly deposit funds.'
          else:
              self.balance -= amount
              outcome = '******************************************************\n'
              outcome += f'Your withdrawal request of ${amount} was successful\n'
              outcome += f'Your Updated account balance is ${self.balance} in {self.name} Budget \n'
              outcome += '******************************************************'
              return outcome
    
      #Creating a Transfer method
      def transfer(self, amount, secondary_category):
          if (self.balance < amount):
              return 'Insufficient Funds, Kindly deposit funds.'
          else:
              self.balance -= amount
              secondary_category.balance += amount
              outcome = '******************************************************\n'
              outcome += 'Your Transfer Transaction was successful\n'
              outcome += f'Your updated account balance is ${self.balance} in {self.name} Budget \n'
              outcome += f'Your updated account balance is ${secondary_category.balance} in {secondary_category.name} Budget \n'
              outcome += '******************************************************'
              return outcome
         
# Creating and Assignment of objects to class of Budget       
food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('music')

# Testing of budget classes and method through assigning inputs.
print (food.deposit(2000));
print(entertainment.deposit(220000))
print(entertainment.withdrawal(15000))
print(entertainment.transfer(60000, clothing))
