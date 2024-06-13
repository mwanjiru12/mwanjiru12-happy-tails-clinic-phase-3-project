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
* Add, update, and delete appointment sessions.
* Add, update, and delete owners.
* View a list of all owners.
* Add, update, and delete veterinarians.
* View a list of all veterinarians.

## Model Structure for SQLite Database

### Class Definitions

#### \`class Pet(Base)\`
This class represents a table in the database named 'pets'.

#### \`class Veterinarian(Base)\`
This class represents a table in the database named 'veterinarians'.

#### \`class Owner(Base)\`
This class represents a table in the database named 'owners'.

#### \`class Appointment(Base)\`
This class represents a table in the database named 'appointments'.

### Tables for Database

#### Pets Table
| Column | Description |
| --- | --- |
| ID | A unique identifier for each pet. |
| Name | The name of the pet. |
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

### \`cli.py\`
This Python script defines a command-line interface (CLI) for the application. It uses the click library, a Python package that simplifies the creation of command line interfaces.

- The script starts by importing the \`click\` module.
- It then imports commands from several modules: \`pets\`, \`owners\`, \`veterinarians\`, and \`appointments\`.
- The \`@click.group()\` decorator creates a new \`click.Group\` instance as the main command of the CLI.
- The docstring inside \`cli()\` provides a welcome message.
- Commands are added to the main \`cli\` command group using the \`add_command\` method.
- The script includes the idiom \`if __name__ == '__main__':\` to launch \`cli()\` when run directly.

### \`pets.py\`
This file defines CLI commands for managing pets using \`click\` and SQLAlchemy.<br>
The functions include:
- `add_pet(name, color, properties)`: Adds a new pet to the database with the given name, color, and properties, setting availability to `True`.
- `remove_pet(id)`: Removes a pet identified by the provided `id`.
- `update_pet(id, name, color, properties)`: Updates the details (name, color, properties) of a pet identified by `id`.
- `view_pet(id)`: Retrieves and displays the details of a pet identified by `id`.
- `search_pet(query)`: Searches for pets by `id`, name, color, or properties.
- `list_pets()`: Lists all pets in the database. <br>
These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.<br>
![Pets Menu](screenshots/petsmenu.png)

### \`owners.py\`
This file defines CLI commands for managing owners using \`click\` and SQLAlchemy.<br>
The functions include:
- `add_owner(name)`: Adds a new owner to the database with the given name.
- `update_owner(id, name)`: Updates the name of an existing owner identified by `id`.
- `remove_owner(id)`: Removes an owner identified by `id`.
- `list_owners()`: Lists all owners in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.
<br>

![Owners Menu](screenshots/ownermenu.png)

### \`veterinarians.py\`
This file defines CLI commands for managing veterinarians using \`click\` and SQLAlchemy.<br>
The functions include:

- `add_veterinarian(name, specialization)`: Adds a new veterinarian with the given name and specialization.
- `update_veterinarian(id, name, specialization)`: Updates the name and specialization of a veterinarian identified by `id`.
- `remove_veterinarian(id)`: Removes a veterinarian identified by `id`.
- `list_veterinarians()`: Lists all veterinarians in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.
<br>
![Veterinarians Menu](screenshots/veterinarian.png)

### \`appointments.py\`
This file defines CLI commands for managing appointments using \`click\` and SQLAlchemy.<br>
The functions include:

- `add_appointment(pet_id, veterinarian_id, owner_id)`: Adds a new appointment record with the given pet ID, veterinarian ID, and owner ID, setting the current date as the start date.
- `update_appointment(id, pet_id, veterinarian_id, owner_id, end_date)`: Updates an existing appointment record identified by `id`.
- `remove_appointment(id)`: Removes an appointment record identified by `id`.
- `list_appointments()`: Lists all appointment records in the database.

These functions are added to a list named `commands`, which is imported by the CLI script to include these commands in the main CLI command group.
<br>

![Appointments Menu](screenshots/appointments.png)

## Author
Created by Maria Wanjiru

## License
MIT License
