import click

from app import init_app

app = init_app()


@app.cli.command(with_appcontext=True)
def initdb():
    from app.models.models import db, ItemType
    db.create_all()
    db.session.commit()
    item_types = ItemType.query.with_entities(ItemType.item_type).all()
    expected_types = ['Book', 'Comic', 'Movie', 'Music', 'Video_Game']
    if sorted([item_type.item_type for item_type in item_types]) != sorted(expected_types):
        for item_type in expected_types:
            item_type_entry = ItemType(item_type=item_type)
            db.session.add(item_type_entry)
    db.session.commit()
    click.echo("Databases created")
