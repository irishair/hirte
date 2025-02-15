# Configuration

## Loading order

On startup, bluechi loads configuration files from the following directories:

| Load order | bluechi | bluechi-agent |
|---|---|---|
| 1 | `/usr/share/bluechi/config/bluechi.conf` | `/usr/share/bluechi-agent/config/agent.conf` |
| 2 | `/etc/bluechi/bluechi.conf` | `/etc/bluechi/agent.conf` |
| 3 | `/etc/bluechi/bluechi.conf.d` | `/etc/bluechi/agent.conf.d` |

Based on the load order, settings from a previously read configuration file will be overridden by subsequent files.
For example, the default setting for `AllowedNodeNames` in `/usr/share/bluechi/config/bluechi.conf` is an empty list and
can be overridden by either editing `/etc/bluechi/bluechi.conf` or adding a file in `/etc/bluechi/bluechi.conf.d`. Configuration
files in `/etc/bluechi/bluechi.conf.d` are sorted alphabetically and read in ascending order.

It is also possible to pass the cli option `-c <path_to_file>` to both, bluechi and bluechi-agent. If specified, this
configuration has the highest priority and all defined settings will override previously set options.

For a list of supported options incl. an explanation please refer to the
the MAN pages for [bluechi(5)](./man/bluechi_conf.md) and [bluechi-agent(5)](./man/bluechi_agent_conf.md).

## Maximum line length

The maximum line length supported by BlueChi is 500 characters. If the characters of any key-value pair exceeds this, use
multiple, indented lines. For example, a large number of node names in the `AllowedNodeNames` field can be split like this:

```bash
AllowedNodeNames=node1,
  node2,
  node3
```
