import click
from db.models import Session, Member


@click.command()
@click.option('--name', prompt='Name of the owner', help='The name of the owner.')
def add_member(name):
    """Add a new owner."""
    session = Session()
    
    new_member = Member(name=name)
    session.add(new_member)
    
    session.commit()
    click.echo(f"Owner added with ID {new_member.id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the owner to update', help='The ID of the owner to update.')
@click.option('--name', prompt='New name of the owner', help='The new name of the owner.')
def update_member(id, name):
    """Update an owner."""
    session = Session()
    
    member = session.get(Member, id)
    if member is not None:
        member.name = name
        session.commit()
        click.echo(f"Updated owner with ID {id}.")
    else:
        click.echo(f"No owner found with ID {id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the owner to remove', help='The ID of the owner to remove.')
def remove_member(id):
    """Remove an owner."""
    session = Session()
    
    member = session.get(Member, id)
    if member is not None:
        session.delete(member)
        session.commit()
        click.echo(f"Removed owner with ID {id}.")
    else:
        click.echo(f"No owner found with ID {id}.")


@click.command()
def list_members():
    """List all owners."""
    session = Session()
    
    members = session.query(Member).all()
    
    for member in members:
        click.echo(f"ID: {member.id}")
        click.echo(f"Name: {member.name}")
        click.echo("-------")


commands = [add_member, remove_member, update_member, list_members]