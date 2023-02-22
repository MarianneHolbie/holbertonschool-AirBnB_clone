
# holbertonschool-binary_trees
## ------ AirBnB clone - The console ------

*****

### ***Introduction to AirBnb clone***
The goal of the project is to deploy on your server a simple copy of the AirBnB website.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-  A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
### ***The console***
- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![image](https://user-images.githubusercontent.com/113857342/220392841-0292dfc2-8bf7-4355-8e21-48f1afc1fdc0.png)

*****

### ***file tree***

- AUTHORS
- README.md
- console.py

- ***models***
    - init.py
    - **base_model.py**
    - amenety.py
    - city.py
    - place.py
    - review.py
    - state.py
    - user.py
    - ***engine***
        - init.py
        - file_storage.py

- ***tests***

*****

### ***files***

- **console.py** : command interpreteur.
- **base_model.py** : Class Base Model.
- **file_storage.py** Serialization - deserialization tool.
- **tests** : Unit testing.
