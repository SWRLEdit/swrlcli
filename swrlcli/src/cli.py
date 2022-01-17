import os.path
from os import path

import click
import csv
import owlready2 as owl


@click.group()
def cli():
    """
    SWRLEdit CLI
    """
    pass


@click.command()
@click.argument('rules', type=click.Path(exists=True))
@click.argument('onto', type=click.Path(exists=True))
@click.option('--separate', is_flag=True, help="Path to a file containing the reasoned facts.")
def reason(rules: str, onto: str, separate: bool = False) -> None:
    """
    Command for reasoning over the provided ontology with the provided rules.

    :param rules: Path to the file containing the rule
    :param onto: The path where the input ontology file is
    :param separate: Set when the reasoned facts should be written to a separate file
    :return:
    """
    # Get a list of all the swrl rules
    swrl_rules = []
    with open(rules, 'r') as f:
        csvreader = csv.reader(f, delimiter=';')
        for swrl_rule in csvreader:
            swrl_rules.append(swrl_rule[0])

    ontology = owl.get_ontology(onto)
    with ontology.load():
        swrl_rule = owl.Imp()
        print(swrl_rules[0])
        swrl_rule.set_as_rule(swrl_rules[0])
        if separate:
            # Create a new ontology context that only contains the reasoned facts
            onto2 = owl.get_ontology('')
            with onto2:
                owl.sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
                onto2.save(f'{os.path.splitext(onto)[0]}_reasoned_facts.owl')
        else:
            # Run the reasoner in the same namespace as the input file
            owl.sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
            ontology.save(f'{os.path.splitext(onto)[0]}_reasoned.owl')


if __name__ == '__main__':
    reason()
