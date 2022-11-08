from unittest.mock import patch, Mock
from opnsense_cli.commands.core.syslog.destination import destination
from opnsense_cli.tests.commands.base import CommandTestCase


class TestSyslogDestinationCommands(CommandTestCase):
    def setUp(self):
        self._api_data_fixtures_reconfigure_OK = {
            "status": "ok"
        }
        self._api_data_fixtures_reconfigure_FAILED = {
            "status": "failed"
        }
        self._api_data_fixtures_configtest_OK = {
            "result": "Configuration file is valid\n\n\n"
        }
        self._api_data_fixtures_configtest_FAILED = {
            "result": "Configuration file is invalid\n\n\n"
        }
        self._api_data_fixtures_create_OK = {
            "result": "saved",
            "uuid": "85282721-934c-42be-ba4d-a93cbfda26af"
        }
        self._api_data_fixtures_create_ERROR = {
            "result": "failed",
            "validations": {'<TODO>': ['Please specify a value between 1 and 100.']}
        }
        self._api_data_fixtures_update_OK = {
            "result": "saved"
        }
        self._api_data_fixtures_update_NOT_EXISTS = {
            "result": "failed"
        }
        self._api_data_fixtures_delete_NOT_FOUND = {
            "result": "not found"
        }
        self._api_data_fixtures_delete_OK = {
            "result": "deleted"
        }
        self._api_data_fixtures_list_EMPTY = {
            "syslog": {
                "destinations": {
                    "destination": []
                }
            }
        }
        self._api_data_fixtures_list = self._read_json_fixture('core/syslog/model_data.json')
        self._api_client_args_fixtures = [
            'api_key',
            'api_secret',
            'https://127.0.0.1/api',
            True,
            '~/.opn-cli/ca.pem',
            60
        ]

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_list(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            destination,
            [
                'list', '-o', 'plain', '-c',
                'uuid,TODO_specifiy_columns'
            ]
        )

        self.assertIn(
            (
                "<TODO match to command output>\n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_list_EMPTY(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list_EMPTY,
            ],
            destination,
            ['list', '-o', 'plain']
        )

        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_show_NOT_FOUND(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            destination,
            ['show', 'b468c719-89db-45a8-bd02-b081246dc002']
        )
        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_show_EMPTY_STRING(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            destination,
            ['show', '']
        )
        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_show(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            destination,
            [
                'show', '2c57ff97-10df-41a1-8a02-ab2fd1a4a651', '-o', 'plain', '-c',
                'uuid,name,Servers,Resolver,Healthcheck,Mailer,Users,Groups,Actions,Errorfiles'
            ]
        )

        self.assertIn(
            (
                "2c57ff97-10df-41a1-8a02-ab2fd1a4a651 pool2 server2,server4  http_head     \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_create_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_create_OK,
                #self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "create", "my_test_destination",
                "--TODO", "<customize with create options>"
            ]
        )

        self.assertIn(
            (
                "saved \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_create_ERROR(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_create_ERROR,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "create",
                "--hostname", "10.0.0.1"
                "--program", "doesnotexists"
            ]
        )

        self.assertIn(
            (
                "Error: {'result': 'failed', 'validations': "
                "{'todo.click_option': ['Please specify a value between 1 and 100.']}}\n"
            ),
            result.output
        )
        self.assertEqual(1, result.exit_code)

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_update_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_update_OK,
                #self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "update", "<TODO customize uuid>",
                "--TODO", "<customize with create options>"
            ]
        )

        self.assertIn(
            (
                "saved \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_update_NOT_EXISTS(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_update_NOT_EXISTS,
                #self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "update", "99282721-934c-42be-ba4d-a93cbfda2644",
                "--no-enabled",
            ]
        )

        self.assertIn(
            (
                "Error: {'result': 'failed'}\n"
            ),
            result.output
        )
        self.assertEqual(1, result.exit_code)

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_delete_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_delete_OK,
                #self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "delete", "85282721-934c-42be-ba4d-a93cbfda26af",
            ]
        )

        self.assertIn(
            (
                "deleted \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.core.syslog.destination.ApiClient.execute')
    def test_delete_NOT_FOUND(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_delete_NOT_FOUND,
                #self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            destination,
            [
                "delete", "99282721-934c-42be-ba4d-a93cbfda2644",
            ]
        )

        self.assertIn("Error: {'result': 'not found'}\n", result.output)
        self.assertEqual(1, result.exit_code)
