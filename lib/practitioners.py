import click
from db.models import Session, Practitioner

@click.command()
@click.option('--name', prompt='Name of the veterinarian', help='The name of the veterinarian.')
@click.option('--specialization', prompt='Specialization of the veterinarian', help='The specialization of the veterinarian.')
def add_practitioner(name, specialization):
    """Add a new veterinarian."""
    session = Session()
    
    new_practitioner = Practitioner(name=name, specialization=specialization)
    session.add(new_practitioner)
    
    session.commit()
    click.echo(f"Veterinarian added with ID {new_practitioner.id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the Veterinarian to update', help='The ID of the veterinarian to update.')
@click.option('--name', prompt='New name of the veterinarian', help='The new name of the veterinarian.')
@click.option('--specialization', prompt='New specialization of the veterinarian', help='The new specialization of the veterinarian.')
def update_practitioner(id, name, specialization):
    """Update a veterinarian."""
    session = Session()
    
    practitioner = session.get(Practitioner, id)
    if practitioner is not None:
        practitioner.name = name
        practitioner.specialization = specialization
        session.commit()
        click.echo(f"Updated veterinarian with ID {id}.")
    else:
        click.echo(f"No veterinarian found with ID {id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the veterinarian to remove', help='The ID of the veterinarian to remove.')
def remove_practitioner(id):
    """Remove a veterinarian."""
    session = Session()
    
    practitioner = session.get(Practitioner, id)
    if practitioner is not None:
        session.delete(practitioner)
        session.commit()
        click.echo(f"Removed veterinarian with ID {id}.")
    else:
        click.echo(f"No veterinarian found with ID {id}.")


@click.command()
def list_practitioners():
    """List all veterinarians."""
    session = Session()
    
    practitioners = session.query(Practitioner).all()
    
    for practitioner in practitioners:
        click.echo(f"ID: {practitioner.id}")
        click.echo(f"Name: {practitioner.name}")
        click.echo(f"Specialization: {practitioner.specialization}")
        click.echo("-------")


commands = [add_practitioner, remove_practitioner, update_practitioner, list_practitioners]
