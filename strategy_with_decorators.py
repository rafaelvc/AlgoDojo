# Luciano Ramalho implemented the strategy pattern for
# an e-commerce where any type of discount given is a strategy.

# 1 - Using an abstract class as an inteface for different strategies
# 2 - Using multiple functions as strategies
# 3 - Using a @promo decorator where each strategy function is decorated
from abc import ABC, abstractclassmethod
from typing import NamedTuple 
from decimal import Decimal
from typing import Sequence
from functools import cached_property

from dataclasses import dataclass, field


class Promo(ABC):

    @abstractclassmethod
    def promo(self, order : 'Order') -> Decimal:
        pass 

class Promo_10(Promo):

    def promo(self, order: 'Order') -> Decimal:
        discount = Decimal(0)
        for item in order.itens:
            discount += Decimal(item.unit_price * item.quantity * 0.1)
        return discount
 
class Promo_5_for_10_Itens(Promo):

    def promo(self, order: 'Order') -> Decimal:
        more_than_10 = (Decimal(item.unit_price * item.quantity * 0.05) for item in order.itens if item.quantity >= 10)
        return sum(more_than_10, Decimal(0))
 

# Named tupled as classes emulate data records 
# withoud need for __inits__ constructors
# is enough to define an item Item('aaa', '1.1', '')
#class Item(NamedTuple):
@dataclass
class Item():
    product: str   
    unit_price: Decimal 
    quantity: int
    
@dataclass
class Order():

    itens: Sequence[Item]
    # promo: 'Promo' = field(default=Promo_5_for_10_Itens(), repr=False) #'Review: not working when default is not Used
    promo: 'Promo'

    @property
    #@cached_property
    def total(self) -> Decimal:
        return sum((Decimal(item.quantity * item.unit_price) for item in self.itens), Decimal(0))

#    @cached_property
    @property
    def discount(self) -> Decimal:
        return self.promo.promo(self)    
    
    def __repr__(self):
        return f' Partial total: {self.total:.2f}\n Discount: {self.discount:.2f} \n Total: {(self.total - self.discount):.2f}'

   

order = Order( [Item('Tennis', 50.0, 2), Item('Tshirt', 25.0, 1)], Promo_10() )
print (order)
print (order)