import math
class Lead:
    def __init__(self , name , staff_size , estimated_revenue , effort_factor):
        self.name = name
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

    def __get_digit(self , op):
        return len(str(math.floor(op)))
    
    def lead_score(self):
        return (1/ 
            (self.staff_size 
            / self.estimated_revenue 
            * (
                10 
                ** 
                (
                    self.__get_digit(self.estimated_revenue) 
                    - 
                    self.__get_digit(self.staff_size)
                    
                ) 
            ) 
            * self.effort_factor))

    def __eq__(self , other):
        return self.lead_score() == other.lead_score()
    def __ne__(self,other):
        return self.lead_score() != other.lead_score()
    def __lt__(self,other):

        return self.lead_score() < other.lead_score()
    def __le__(self,other):

        return self.lead_score() <= other.lead_score()
    def __gt__(self,other):

        return self.lead_score() > other.lead_score()
    def __ge__(self,other):

        return self.lead_score() >= other.lead_score()

    def __str__(self):
        return f"you estimated factore {str(self.effort_factor)} and youe staff size are {self.staff_size}"

    
l1 = Lead('pavi' , 12 , 1000 , 10.0)
l2 = Lead('pavi' , 12 , 1000 , 10.0)
print(l1.lead_score())
print(l1==l2)
print(str(l1))


"""
example of using thes function

$ python -i vars.py
>>> user1 = User("KeVin", "kbacon@EXAMPLE.com")
>>> user2 = User("kevIN", "KBACON@example.com")
>>> user3 = User("Keith", "keith@example.com")
>>> user1 == user2
True
>>> user1 != user2
False
>>> user1 == user3
False
>>> user1 != user3
True
>>> user1 > user3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'User' and 'User'

"""