/* SPDX-License-Identifier: GPL-2.0-or-later */
#include <systemd/sd-bus.h>

int method_monitor_units_on_nodes(sd_bus *api_bus, char *nodes, char *units);
int method_monitor_node_connection_state(sd_bus *api_bus);