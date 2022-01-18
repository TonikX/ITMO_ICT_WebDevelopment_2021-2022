## Overview
The **library** api presents information on the contents of the **library** database. 
It includes information on **books**, **readers** who attend the library and the library **halls**. The api allows to request more and less specific information from the corresponding tables. 
The api also provides tools for registering readers as users, allows to edit their profiles and do authorization by token.  


## Quick Start
To start using the library api, follow these steps.

1. Install Django and Django Rest Framework:  
`pip install django`  
`pip install djangorestframework`

2. Clone the repository to your local computer. 
In order to do that, press the button `Git clone` in the upper left corner and run the command in your local cmd.

3. Go to the `library_app` folder and run the command  
`python manage.py runserver`

4. Go to `localhost:8000/library/` and start using the api. 
For the list of available endpoints, consult the library docs.