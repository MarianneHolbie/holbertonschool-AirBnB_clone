<h1 align="center">holbertonschool-AirBnB_clone</h1>

![hbnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)
<h1 align="center">------------------ AirBnB clone - The console ------------------</h1>

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

The console will be a tool to validate this storage engine.

![image](https://user-images.githubusercontent.com/113857342/220392841-0292dfc2-8bf7-4355-8e21-48f1afc1fdc0.png)

*****



### ***file tree***

- AUTHORS https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/AUTHORS
- README.md https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/README.md
- console.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/console.py
- init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/__init__.py

- ***models*** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models
    - init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/__init__.py
    - **base_model.py** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/base_model.py
    - amenety.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/amenity.py
    - city.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/city.py
    - place.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/place.py
    - review.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/review.py
    - state.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/state.py
    - user.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/user.py
    - ***engine*** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/engine
        - init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/engine/__init__.py
        - **file_storage.py** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/models/engine/file_storage.py

- ***tests*** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests
    - init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/__init__.py
    - ***test_models*** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models
        - init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/__init__.py
        - test_base_model.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_base_model.py
        - test_amenity.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_amenity.py
        - test_city.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_city.py
        - test_place.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_place.py
        - test_review.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_review.py
        - test_state.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_state.py
        - test_user.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_user.py
        - ***test_engine*** https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_engine
            - init.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_engine/__init__.py
            - test_file_storage.py https://github.com/Amandine4731/holbertonschool-AirBnB_clone/tree/master/tests/test_models/test_engine/test_file_storage.py

*****


### ***files***

- **console.py** : command interpreteur.
    
| ***Commands*** | Description |
|----------|-----------------------------------------------|
| **create** | Creates a new instance of a class, saves it (to the JSON file) and prints the id. |
| **show** | Prints the string representation of an instance based on the class name and id. |
|  **destroy** | Deletes an instance based on the class name and id (save the change into the JSON file). |
| **all** | Prints all string representation of all instances based or not on the class name |
| **update** | Updates an instance based on the class name and id by adding or updating attribute, saves it to the JSON file |
| **EOF** (ctrl+d) | Exits the console |
| **quit** | Exits the console |
| emptyline | Does nothing |
- **base_model.py** : Class Base Model.
- **file_storage.py** Serialization - deserialization tool.
- **tests** : Unit testing. ***To check the tests with a verbose output :***

```bash
$ python3 -m unittest discover tests -v
```
*****
$\color[rgb]{0,1,0} OUR \ PROGRAM$

### The repository :
```bash  
$ git clone https://github.com/Amandine4731/holbertonschool-AirBnB_clone.git  
```  


### To run the program :

```bash
$ ./console.py
```


*By Marianne Arrué and Amandine Assenat*
