from swrlcli.src.cli import reason
from click.testing import CliRunner


def test_reason():
    """
    Test that the reason function works properly

    :return: None
    """
    runner = CliRunner()
    result = runner.invoke(reason, ['tests/data/swrl_1.txt', 'tests/data/ontology_1.ttl'])
    assert result.exit_code == 0
