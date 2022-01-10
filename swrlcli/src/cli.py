import click


@click.group()
def cli():
    """
    SWRLEdit CLI
    """


@click.command()
@click.argument('rules', type=click.Path(exists=True))
@click.argument('onto', type=click.Path(exists=True))
def reason(rules: str, onto: str) -> None:
    """
    Command that takes a rule and ontology and runs the parser

    :param rules: Path to the file containing the rule
    :param onto: The path where the input ontology file is
    :return:
    """
    click.echo(click.format_filename(rules))
    click.echo(click.format_filename(onto))


if __name__ == '__main__':
    reason()
