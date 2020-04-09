import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--punc', default="!", help="Set the punctuation at the end")
@click.option('-u', '--upper', default=False,
                is_flag=True, help="Change the message to all uppercase")
@click.option('-l', '--lower', default=False,
                is_flag=True, help="Change the message to all lowercase")
@click.option('-w', '--word', required=False, default="Hello",
                help="Set the greeting word, e.g.: Hi")
@click.argument('name', required=False, default="World")
def greet(punc, name, upper, lower, word):
    string = f"{word.capitalize()}, {name.capitalize()}{punc}"
    if upper:
        print(string.upper())
    elif lower:
        print(string.lower())
    else:
        print(string)

@cli.command()
@click.option('--punc', default="!", help="Set the punctuation at the end")
@click.argument('name', required=False, default="User")
def morning(name, punc):
    print("Good morning, ", name.capitalize(), punc, sep="")

if __name__ == '__main__':
    cli()

