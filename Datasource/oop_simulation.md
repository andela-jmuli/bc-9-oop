

### A real life simulation of Object Oriented programming explaining the attributes  

####1. Inheritance  
Imagine a car dealership and you're the manager. You have a variety of vahicles ranging from trucks, salloon cars and motorcycles. What really makes you unique from other businesses is the pricing of the vehicle lot. Trucks hold a rate of $15,000 by the number of wheels, cars a rate of $8000 by the number of wheels and motorcycles $5000 by the number of wheels.  
An improved sales system would involve object-oriented design whereby the vehicles in sale would be classified under the same category (vehicle). This is because they all display vehicle-like attributes e.g precense of wheels, movement, engines and fuel consumption. In this case, the main or super class would be Vehicle, where child classes including car, truck and motorcycle would extend or inherit from Vehicle.  

####2. Abstraction and Encapsulation  
The child classes would definitely have to be initialized in order to define different types of each and in our case, we'd result to having a super **Vehicle** class which would in turn result to vehicle objects. But vehicle objects wouldn't be specific to any kind of vehicle and we have quite a variety. Our source code so far would also be so repetitive as we'd have to declare a vehicle class, each child class with the same attributes which is against the rule of **DRY** and also not a really good practice. Abstraction comes in play where the Vehicle class is made abstract by adding an abstract method which would define a vehicle category on instantiation. This also implies that all Vehicle class can't be instantiated anymore thus the child classes would also have to define the method vehicle_category() to specify instances only when they inherit from Vehicle.  
With that change, the class attributes would only be defined in the super class thus code efficiency.  
Encapsulation and Abstraction are synonymous in a number of ways. They both define data hiding. Generally, encapsulation restricts access of some of an object's components. This means that the object's internal representation cannot be seen from outside the object's definition.

####3. Polymorphism  
Polymorphism defines a situation where two instances of a class display of demonstrate different behaviours under the same context or given the same method. In the dealership case, We'd say each car or vehicle would display a totally different behaviour if we were to have a honk method. Well, some would be almost similar but the majority would have a totally different honk type.
