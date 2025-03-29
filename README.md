# Hyperion
This project is a collection of various apps that was created for my HyperionDev Software Engineer Bootcamp course. The apps
showcase some of my work in the course. There are various apps such as a 'blog', 'polls', 'webapp', 'user_auth' and 'accounts' that provide various
functionality.
* blog - allows an django admin user to post blog posts on a website.
* polls - allows a django admin user to start a poll.
* webapp - display a fictious hardware store with a catologue of tools.
* user_auth and accounts - used for authentication purposes in polls app.
  
## Table of Contents
[Hyperion](#hyperion) 

[Description](#description)

[Table of Contents](#table-of-contents)

[Installation](#installation)

[Usage](#usage)

[URL To GitHub Repository](#url-to-github-repository)

## Description
This project is a collection of various apps that was created for my HyperionDev Software Engineer Bootcamp course. The apps
showcase some of my work in the course. There are various apps such as a 'blog', 'polls', 'webapp', 'user_auth' and 'accounts' that provide various
functionality.
Below are the apps and short description of it functionality.
* blog - allows an django admin user to post blog posts on a website.
* polls - allows a django admin user to start a poll.
* webapp - display a fictious hardware store with a catologue of tools.
* user_auth and accounts - used for authentication purposes in polls app.

## Installation
Here are are the step to setup and run this project locally:

**Prerequisites**

Ensure you have the following installed:

  * Python 3.12.9 or later

  * Git

  * SQLite3

  * Pip

  * Django 5.1.6 or later

  * Bootsrap

**Step 1: Clone the Repository**

1. Open your terminal or command prompt.
2. Use the following command clone the repository to your local machine: git clone https://github.com/DarrylA09/Darryl-s-First-Projects.git
3. Navigate into the project directory: cd Darryl-s-First-Projects

**Step 2: Setup the Virtual Environment**

1. Use the following command to install and use built-in pip module:
   
   python -m pip install pip
   
2. To enable the virtual environment, use the following command:

   pip install virtualenv
   
3. There is also a wrapper available that provides some handy commands, use the following command:

   For Windows: pip install virtualenvwrapper-win
   For Linux or MacOS: pip install virtualenvwrapper
   
**Step 4: Apply Database Migrations**

1. Run the following command to apply migrations:

   python manage.py migrate

**Step 5: Start the Django development server**

1. Run the following command:
  
   python manage.py runserver

## Usage

**Step 1: Access the Application**

1. Navigate to the file directory where django environment is setup and run the following the command:

   my_django\Scripts\activate

**Step 2: Here are the key features of the project:**

**Blog App**
1. Ability to add posts for the blog via Django admin. http://127.0.0.1:8000/admin/ 
   
   ![Blog Admin](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Blog%20Admin.png)
 
2. Ability to add a post for the blog page.

   ![Add Post](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Add%20Post.png)

4. Ability to change a post for the blog page.

   ![Change Post](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Change%20Post.png)

6. View a list of blog posts. http://127.0.0.1:8000/blog/

   ![View Posts](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/View%20Blog%20Posts.png)

7.  Open a blog posts.

    ![Open Posts](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Open%20Blog%20Posts.png)

**Polls App**
1. Ability to create poll questions and choices. http://127.0.0.1:8000/admin/ 

   ![Manage Polls](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Admin.png)
   
2. Ability to add poll questions.

   ![Add Poll Questions](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Add%20Questions.png)

4. Ability to change poll questions.

   ![Change Poll Questions](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Change%20Questions.png)

6. Ability to add poll choices.

   ![Add Choices](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Add%20Choice.png)

8. Ability to change poll choices.

   ![Change Choices](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Change%20Choice.png)
   
10. Polls Login Page. http://127.0.0.1:8000/polls/auth/login/

    ![Login Page](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Login.png)
  
12. Polls Signup page.

    ![Signup Page](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Signup.png)

14. Polls Homepage. http://127.0.0.1:8000/polls/

    ![Polls homepage](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Homepage.png)

16. Polls Voting.

    ![Polls Voting](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Choice.png)

18. Polls Results. http://127.0.0.1:8000/polls/3/results/ 

    ![Polls Results](https://github.com/DarrylA09/Darryl-s-First-Projects/blob/master/Screenshots/Polls%20Results.png)

## URL To GitHub Repository

Here is a link to access the GitHub repository

[GitHub Repository Darryls First Projects](https://github.com/DarrylA09/Darryl-s-First-Projects)
