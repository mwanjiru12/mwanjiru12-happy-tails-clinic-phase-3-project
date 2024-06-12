import click
from gemstones import commands as gemstone_commands
from members import commands as member_commands
from practitioners import commands as practitioner_commands
from usages import commands as usage_commands

def gemstone_submenu():
    click.echo('Pets commands:')
    click.echo('1. Add pets')
    click.echo('2. Remove pets')
    click.echo('3. Update pets')
    click.echo('4. View pets')
    click.echo('5. Search pets')
    click.echo('6. List pets')
    click.echo('7. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option!.')
        return
    
    if choice == 7:
        return
    elif 1 <= choice <= 6:
        gemstone_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def practitioner_submenu():
    click.echo('Veternarian commands:')
    click.echo('1. Add veterinarian')
    click.echo('2. Remove veterinarian')
    click.echo('3. Update veterinarian')
    click.echo('4. List veterinarians')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        practitioner_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def member_submenu():
    click.echo('Owner commands:')
    click.echo('1. Add Owner')
    click.echo('2. Remove Owner')
    click.echo('3. Update Owner')
    click.echo('4. List Owners')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        member_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def usage_submenu():
    click.echo('Treatment-Appointment commands:')
    click.echo('1. Add Appointment')
    click.echo('2. Remove Appointment')
    click.echo('3. Update Appointment')
    click.echo('4. List Appointments')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        usage_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

@click.group()
def cli():
    """Welcome to Happy Tails Clinic, the Veterinary's Management Application!"""

if __name__ == '__main__':
    while True:
        click.echo("""Welcome to Happy Tails Clinic, the Veterinary Clinic's Management Application!""")
        click.echo('Main menu:')
        click.echo('1. Pets commands')
        click.echo('2. Owner commands')
        click.echo('3. Veterinarian commands')
        click.echo('4. Treatment-Appointments commands')
        click.echo('q. Quit')

        choice = click.prompt('Please enter your choice', type=str)

        if choice == '1':
            gemstone_submenu()
        elif choice == '2':
            member_submenu()
        elif choice == '3':
            practitioner_submenu()
        elif choice == '4':
            usage_submenu()
        elif choice.lower() == 'q':
            break
        else:
            click.echo('Invalid choice. Please choose a valid option.')

for command in gemstone_commands + member_commands + practitioner_commands + usage_commands:
    cli.add_command(command)
#cli menu will have 4 options