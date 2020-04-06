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
@click.option('--punc', default="!", help="Set the punctuation at the end")
@click.argument('name', required=False, default="User")
def morning(name, punc):
    print("Good morning, ", name.capitalize(), punc, sep="")

if __name__ == '__main__':
    cli()

