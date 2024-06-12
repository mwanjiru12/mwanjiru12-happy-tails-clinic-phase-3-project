import click
from db.models import Session, Gemstone
from sqlalchemy import or_

@click.command()
@click.option('--name', prompt='Name of the pet', help='The name of the pet.')
@click.option('--color', prompt='Color of the pets fur', help='The color of the pets fur.')
@click.option('--properties', prompt='Properties of the pet', help='The properties of the pets.')
def add_gemstone(name, color, properties):
    """Add a new pet to the system."""
    session = Session()
    
    new_gemstone = Gemstone(name=name, color=color, properties=properties, availability=True)
    session.add(new_gemstone)
    
    session.commit()
    click.echo(f"Pet added with ID {new_gemstone.id}.")


@click.command()
@click.option('--id', prompt='ID of the pet to remove', help='The ID of the pet to remove.')
def remove_gemstone(id):
    """Remove a pet from the collection."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        session.delete(gemstone)
        session.commit()
        click.echo(f"Removed pet with ID {id}.")
    else:
        click.echo(f"No pet found with ID {id}.")


@click.command()
@click.option('--id', prompt='ID of the pet to update', help='The ID of the pet to update.')
@click.option('--name', prompt='Updated name of the pet', help='The new name of the pet.')
@click.option('--color', prompt='Updated color of the pet', help='The new color of the pet.')
@click.option('--properties', prompt='Updated properties of the pet', help='The new properties of the pet.')
def update_gemstone(id, name, color, properties):
    """Update a pet in the system."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        gemstone.name = name
        gemstone.color = color
        gemstone.properties = properties
        session.commit()
        click.echo(f"Updated pet with ID {id}.")
    else:
        click.echo(f"No pet found with ID {id}.")


@click.command()
@click.option('--id', prompt='ID of the pet to view', help='The ID of the pet to view.')
def view_gemstone(id):
    """View a pet in the collection."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
    else:
        click.echo(f"No gemstone found with ID {id}.")


@click.command()
@click.option('--query', prompt='Search for a pet by ID name, color, or properties', help='The search query.')
def search_gemstone(query):
    """Search for a pet in the collection."""
    session = Session()
    
    gemstones = session.query(Gemstone).filter(
        or_(Gemstone.name.contains(query), Gemstone.properties.contains(query), 
            Gemstone.color.contains(query), Gemstone.id.contains(query))
    ).all()
    
    for gemstone in gemstones:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
        click.echo("-------")


@click.command()
def list_gemstones():
    """List all pets in the system."""
    session = Session()
    
    gemstones = session.query(Gemstone).all()
    
    for gemstone in gemstones:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
        click.echo("-------")


commands = [add_gemstone, remove_gemstone, update_gemstone, view_gemstone, search_gemstone, list_gemstones]
