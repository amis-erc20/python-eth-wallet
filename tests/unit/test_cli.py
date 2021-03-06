import pytest
from eth_wallet.cli.eth_wallet_cli import eth_wallet_cli
from eth_wallet.cli.new_wallet import new_wallet
from eth_wallet.cli.get_wallet import get_wallet
from eth_wallet.cli.reveal_seed import reveal_seed
from click.testing import CliRunner


def call_eth_wallet(fnc=None, parameters=None, envs=None):
    fnc = fnc or eth_wallet_cli
    runner = CliRunner()
    envs = envs or {}
    parameters = parameters or []
    # catch exceptions enables debugger
    return runner.invoke(fnc, args=parameters, env=envs, catch_exceptions=False)


def test_base_help():
    result = call_eth_wallet(parameters=["--help"])
    assert result.exit_code == 0
    assert "Usage: eth-wallet-cli [OPTIONS] COMMAND [ARGS]..." in result.output


@pytest.mark.parametrize(
    "subcommand", ["get-wallet", "reveal-seed", "new-wallet"]
)
def test_base_subcommand_help(subcommand):
    result = call_eth_wallet(eth_wallet_cli, parameters=[subcommand, "--help"])
    assert result.exit_code == 0
    assert f"Usage: eth-wallet-cli {subcommand} [OPTIONS]" in result.output


# !!! be careful this test will override keystore file on specific path
# def test_new_account(mocker, tmp_path):
#     conftest.prepare_conf(tmp_path)
#
#     mocker.patch('getpass.getpass',
#                  return_value='my-password')
#     runner = CliRunner()
#     with runner.isolated_filesystem():
#         result = runner.invoke(new_wallet)
#         assert result.exit_code == 0
#
#         result = runner.invoke(get_wallet)
#         assert result.exit_code == 0
#
#         result = runner.invoke(reveal_private_key)
#         assert result.exit_code == 0
