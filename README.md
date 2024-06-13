# Happy Tails Clinic - Phase 3 CLI Project

## Introduction
This is a CLI application that manages a pet care center's collection of pets, for use by veterinarians with the pet's owners.

## Installation
pipenv install

## Functionality/User Stories
As a user I am able to:

* Add new pets to the collection.
* Remove pets from the collection.
* Update details about a particular pet in the collection.
* Search for a pet based on various attributes (name, breed, illness, etc.)
* Display information about a particular pet.
* View a list of all pets.
* Track which veterinarian is using which pet, and with which owner.
* Add, update and delete appointment sessions.
* Add, update, and delete owners.
* View a list of all owners.
* Add, update, and delete veterinarians.
* View a list of all veterinarians.

## Model Structure for SQLite Database
The `models.py` file defines the model structure for the SQLite database using the SQLAlchemy ORM (Object Relational Mapping) in Python.

### Tables for Database

#### Pets Table
| Column | Description |
| --- | --- |
| ID | A unique identifier for each pet. |
| Name | The name of the pet. |
| Breed | The breed of the pet. |
| Illness | The illness or health condition of the pet. |
| Availability | Whether the pet is currently available for appointment. |

#### Veterinarians Table
| Column | Description |
| --- | --- |
| ID | A unique identifier for each veterinarian. |
| Name | The name of the veterinarian. |
| Specialization | The veterinarian's area of specialization or expertise. |

#### Owners Table
| Column | Description |
| --- | --- |
| ID | A unique identifier for each owner. |
| Name | The name of the owner. |

#### Appointments Table
| Column | Description |
| --- | --- |
| ID | A unique identifier for each appointment record. |
| Pet ID | The ID of the pet being used. |
| Veterinarian ID | The ID of the veterinarian using the pet. |
| Owner ID | The ID of the owner with whom the pet is being used. |
| Start Date | The date and time when the appointment started. |
| End Date | The date and time when the appointment ended. |

## File Descriptions

### cli.py
This Python script defines a command-line interface (CLI) for the application. It uses the click library, a Python package that simplifies the creation of command line interfaces. <br>
![Pets Menu](screenshots/mainmenu.png)

### pets.py
This file defines a series of command-line interface (CLI) commands for managing pets. <br>
![Pets Menu](screenshots/petsmenu.png)<br>
This file defines a series of CLI commands using the `click` library and SQLAlchemy for database interactions. The functions include:

- `add_pet(name, color, properties)`: Adds a new pet to the database with the given name, color, and properties, setting availability to `True`.
- `remove_pet(id)`: Removes a pet identified by the provided `id`.
- `update_pet(id, name, color, properties)`: Updates the details (name, color, properties) of a pet identified by `id`.
- `view_pet(id)`: Retrieves and displays the details of a pet identified by `id`.
- `search_pet(query)`: Searches for pets by `id`, name, color, or properties.
- `list_pets()`: Lists all pets in the database. <br>
These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.


### owners.py
This file defines a series of command-line interface (CLI) commands for managing owners.<br>
![Pets Menu](screenshots/ownermenu.png)<br>
This file also defines a set of CLI commands using `click` and SQLAlchemy. The functions include:

- `add_owner(name)`: Adds a new owner to the database with the given name.
- `update_owner(id, name)`: Updates the name of an existing owner identified by `id`.
- `remove_owner(id)`: Removes an owner identified by `id`.
- `list_owners()`: Lists all owners in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.


### veterinarians.py
This file defines a series of command-line interface (CLI) commands for managing veterinarians.<br>
![Pets Menu](screenshots/veterinarian.png)<br>
This file defines CLI commands for managing veterinarians using `click` and SQLAlchemy. The functions include:

- `add_veterinarian(name, specialization)`: Adds a new veterinarian with the given name and specialization.
- `update_veterinarian(id, name, specialization)`: Updates the name and specialization of a veterinarian identified by `id`.
- `remove_veterinarian(id)`: Removes a veterinarian identified by `id`.
- `list_veterinarians()`: Lists all veterinarians in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.

### appointments.py
This file defines a series of command-line interface (CLI) commands for managing appointments.<br>
 ![Pets Menu](screenshots/appointments.png)<br>
 This file defines CLI commands for managing appointment records using `click` and SQLAlchemy. An appointment record represents the instance of a pet being seen by a veterinarian under an owner's care<br> The functions include:

- `add_appointment(pet_id, veterinarian_id, owner_id)`: Adds a new appointment record with the given pet ID, veterinarian ID, and owner ID, setting the current date as the start date.
- `update_appointment(id, pet_id, veterinarian_id, owner_id, end_date)`: Updates an existing appointment record identified by `id`.
- `remove_appointment(id)`: Removes an appointment record identified by `id`.
- `list_appointments()`: Lists all appointment records in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.

## Author
Created by Maria Wanjiru

## License
MIT License

Copyright (c) [2024] Maria Wanjiru 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.