import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--punc', default="!", help="Set the punctuation at the end")
@click.argument('name', required=False, default="World")
def greet(punc, name):
    print("Hello, ", name.capitalize(), punc, sep="")

@cli.command()
def morning():
    click.echo("Good morning, ")

if __name__ == '__main__':
    cli()

