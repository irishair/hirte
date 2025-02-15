# SPDX-License-Identifier: GPL-2.0-or-later

import pytest
from typing import Dict

from bluechi_test.test import BluechiTest
from bluechi_test.container import BluechiControllerContainer, BluechiNodeContainer
from bluechi_test.config import BluechiControllerConfig, BluechiNodeConfig

NODE_GOOD = "node-good"
NODE_WITH_LONG_LOGISQUIET = "node-long-logisquiet"
NODE_WITH_NOT_VALID_VALUE = "node-with-not-valid-value"
NODE_WITH_NUMBERS_ONLY_IN_LOGISQUIET = "node-numbers-only"


def start_with_invalid_port(ctrl: BluechiControllerContainer, nodes: Dict[str, BluechiNodeContainer]):
    _, output = nodes[NODE_GOOD].exec_run('systemctl status bluechi-agent')
    output_systemd = str(output)
    if "fail" in output_systemd.lower():
        raise Exception(f"{NODE_GOOD} bluechi-agent should NOT failed during the start of the service")

    _, output = nodes[NODE_WITH_LONG_LOGISQUIET].exec_run('systemctl status bluechi-agent')
    output_systemd = str(output)
    if "fail" not in output_systemd.lower():
        raise Exception(
                f"{NODE_WITH_LONG_LOGISQUIET} bluechi-agent should FAIL "
                "during the start of the service"
        )

    _, output = nodes[NODE_WITH_NOT_VALID_VALUE].exec_run('systemctl status bluechi-agent')
    output_systemd = str(output)
    if "fail" in output_systemd.lower():
        raise Exception(
                f"{NODE_WITH_NOT_VALID_VALUE} bluechi-agent should "
                "NOT failed during the start of the service")

    _, output = nodes[NODE_WITH_NUMBERS_ONLY_IN_LOGISQUIET].exec_run('systemctl status bluechi-agent')
    output_systemd = str(output)
    if "fail" in output_systemd.lower():
        raise Exception(
                f"{NODE_WITH_NUMBERS_ONLY_IN_LOGISQUIET} bluechi-agent should "
                "NOT failed during the start of the service")


@pytest.mark.timeout(15)
def test_agent_invalid_port_configuration(
        bluechi_test: BluechiTest,
        bluechi_node_default_config: BluechiNodeConfig, bluechi_ctrl_default_config: BluechiControllerConfig):

    node_good_cfg = bluechi_node_default_config.deep_copy()
    node_good_cfg.node_name = NODE_GOOD
    node_good_cfg.log_is_quiet = "false"

    node_with_long_logisquiet_cfg = bluechi_node_default_config.deep_copy()
    node_with_long_logisquiet_cfg.node_name = NODE_WITH_LONG_LOGISQUIET
    node_with_long_logisquiet_cfg.log_is_quiet = "NO_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION_NOT_REALLY_A_VALID_OPTION" # noqa: E501, E261

    node_with_invalid_value_cfg = bluechi_node_default_config.deep_copy()
    node_with_invalid_value_cfg.node_name = NODE_WITH_NOT_VALID_VALUE
    node_with_invalid_value_cfg.log_is_quiet = "NOT_TRUE_OR_FALSE_VALUE"

    node_with_numbersonly_in_logisquiet_cfg = bluechi_node_default_config.deep_copy()
    node_with_numbersonly_in_logisquiet_cfg.node_name = NODE_WITH_NUMBERS_ONLY_IN_LOGISQUIET
    node_with_numbersonly_in_logisquiet_cfg.log_is_quiet = 10000000

    bluechi_ctrl_default_config.allowed_node_names = [
            NODE_GOOD,
            NODE_WITH_LONG_LOGISQUIET,
            NODE_WITH_NOT_VALID_VALUE,
            NODE_WITH_NUMBERS_ONLY_IN_LOGISQUIET
    ]

    bluechi_test.set_bluechi_controller_config(bluechi_ctrl_default_config)

    bluechi_test.add_bluechi_node_config(node_good_cfg)
    bluechi_test.add_bluechi_node_config(node_with_long_logisquiet_cfg)
    bluechi_test.add_bluechi_node_config(node_with_invalid_value_cfg)
    bluechi_test.add_bluechi_node_config(node_with_numbersonly_in_logisquiet_cfg)

    bluechi_test.run(start_with_invalid_port)
