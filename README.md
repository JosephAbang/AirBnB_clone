# AirBnB Clone - Command Interpreter

## Description

This project is an AirBnB clone developed as a part of the alx School curriculum. The primary goal of this project is to build a command-line interpreter (console) that allows users to interact with and manage objects within the AirBnB clone project.

## Command Interpreter

The command interpreter, often referred to as the console, is a powerful tool that enables users to perform various operations on objects within the AirBnB clone project. The primary functionalities of the command interpreter include:

- Creating new objects, such as users or places.
- Retrieving objects from various data sources, such as files or databases.
- Performing operations on objects, such as counting or computing statistics.
- Updating attributes of existing objects.
- Destroying objects, effectively removing them from the system.

## How to Start It

To start the AirBnB clone's command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
    git clone https://github.com/Slimake/AirBnB_clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB_clone
   ```

3. Launch the command interpreter by running the `console.py` script:

   ```bash
   ./console.py
   ```

The console will start, and you'll be able to enter commands to interact with the AirBnB clone project.

## How to Use It

Once the command interpreter is running, you can use it to manage objects within the AirBnB clone. Here are some common commands and their usage:

- **Create an Object**:
  ```bash
  (hbnb) create <class_name>
  ```

- **Retrieve an Object**:
  ```bash
  (hbnb) show <class_name> <object_id>
  ```

- **Display All Objects or Objects of a Specific Class**:
  ```bash
  (hbnb) all
  (hbnb) all <class_name>
  ```

- **Update an Object's Attributes**:
  ```bash
  (hbnb) update <class_name> <object_id> <attribute_name> "<new_value>"
  ```

- **Destroy an Object**:
  ```bash
  (hbnb) destroy <class_name> <object_id>
  ```

- **Quit the Console**:
  ```bash
  (hbnb) quit
  ```

## Examples

Here are some examples of using the AirBnB clone command interpreter:

- Creating a new User object:
  ```
  (hbnb) create User
  ```

- Showing details of a Place object with ID `1234-5678`:
  ```
  (hbnb) show Place 1234-5678
  ```

- Listing all User objects:
  ```
  (hbnb) all User
  ```

- Updating the name attribute of a User with ID `user_id`:
  ```
  (hbnb) update User user_id name "New Name"
  ```

- Destroying a Review object with ID `review_id`:
  ```
  (hbnb) destroy Review review_id
  ```

This command interpreter provides a convenient way to manage objects within the AirBnB clone project, facilitating the creation, retrieval, modification, and deletion of objects while abstracting the underlying storage mechanisms.
