import unittest
from stack_and_queue import Queue, Node
from abc import ABCMeta


# Implement an animal shelter that can adopt dogs and cats.
# When you take an animal, you take the oldest animal from the registration date.
# You can choose the species of animals, but you can't adopt the specific animal.
class AnimalNode(Node):

    def __str__(self):
        return self.item.name
    
    @property
    def order(self):
        return self.item.order
    
    @property
    def name(self):
        return self.item.name


class AnimalQueue(Queue):

    def __init__(self, animal=None):
        super().__init__(animal)
        if not animal:
            self._first = None
            self._last = None
            self._size = 0
        else:
            self._first = AnimalNode(animal)
            self._last = AnimalNode(animal)
            self._size = 1

    def push(self, item):
        new_node = AnimalNode(item)
        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node 
        self.size += 1


class AnimalShelter:

    def __init__(self):
        self._dog_list = AnimalQueue()
        self._cat_list = AnimalQueue()
        self._order = 0
    
    def __len__(self):
        return len(self.dog_list) + len(self.cat_list)
    
    def __str__(self):
        return_str = "Dog: " + str(self.dog_list) + "\n"
        return_str += "Cat: " + str(self.cat_list) + "\n"
        return_str += "Any: "

        dog = self.dog_list.first
        cat = self.cat_list.first
        animal_list = []

        while dog and cat:
            if cat.order <= dog.order:
                animal_list.append(str(cat))
                cat = cat.next
            else:
                animal_list.append(str(dog))
                dog = dog.next
        
        remain = dog or cat
        while remain:
            animal_list.append(str(remain))
            remain = remain.next

        return_str += " -> ".join(animal_list)
        return return_str
        
    @property
    def dog_list(self):
        return self._dog_list
    
    @property
    def cat_list(self):
        return self._cat_list
    
    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, new_order):
        self._order = new_order

    def register(self, animal):
        animal.order = self.order
        new_node = AnimalNode(animal)
        if animal.kind == 'Dog':
            self.dog_list.push(new_node)
        else:
            self.cat_list.push(new_node)
        self.increase_order()
        
    def increase_order(self):
        self.order += 1
    
    def adopt(self):
        oldest_dog = self.dog_list.peek()
        oldest_cat = self.cat_list.peek()

        if len(self) == 0:
            return None

        if not oldest_dog:
            return self.adopt_cat()
        if not oldest_cat:
            return self.adopt_dog()
        
        if oldest_cat.order <= oldest_dog.order:
            return self.adopt_cat()
        else:
            return self.adopt_dog()
    
    def adopt_cat(self):
        return self.cat_list.pop_front()
    
    def adopt_dog(self):
        return self.dog_list.pop_front()


class Animal(metaclass=ABCMeta):
    
    def __init__(self, name, kind=None):
        if kind:
            self._kind = kind
        else:
            self._kind = None
        self._name = name
        self._order = 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def kind(self):
        return self._kind
    
    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, new_order):
        self._order = new_order


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name, 'Dog')


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name, 'Cat')


class Test(unittest.TestCase):

    def test(self):
        shelter = AnimalShelter()
        d1 = Dog("C")
        d2 = Dog("Cpp")
        d3 = Dog("CSharp")
        c1 = Cat("Python")
        c2 = Cat("JavaScript")
        c3 = Cat("Rust")
        shelter.register(c1)
        shelter.register(d1)
        shelter.register(d2)
        shelter.register(c2)
        shelter.register(d3)
        shelter.register(c3)
        self.assertEqual(str(shelter.adopt()), "Python")
        self.assertEqual(str(shelter.adopt_cat()), "JavaScript")
        self.assertEqual(str(shelter.adopt_dog()), "C")
        self.assertEqual(str(shelter.adopt()), "Cpp")
        self.assertEqual(str(shelter.adopt()), "CSharp")
        self.assertEqual(str(shelter.adopt()), "Rust")


if __name__ == '__main__':
    unittest.main()
