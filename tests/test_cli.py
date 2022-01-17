import unittest
from unittest import mock

from swrlcli.src.cli import reason
from click.testing import CliRunner


def mock_save(res):
    """
    Mocks a file save by returning True
    :return:
    """
    return True


class TestCli:

    @mock.patch('owlready2.namespace.Ontology.save', side_effect=mock_save)
    def test_reason(self, mock):
        """
        Test that 'reason' handles input correctly

        :param mock: The file write mock
        :return: None
        """
        runner = CliRunner()
        result = runner.invoke(reason, ['tests/data/swrl_1.txt', 'tests/data/ontology_1.owl'])
        assert result.exit_code == 0
        result = runner.invoke(reason, ['tests/data/swrl_1.txt', 'tests/data/ontology_1.owl', '--separate'])
        assert result.exit_code == 0


if __name__ == '__main__':
    unittest.main()
