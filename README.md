# Panix, an NXAPI library

Panix is a python3 NXAPI convenience library.  It internally uses json and returns the user python native data structures. It leverages requests for the json-rpc handling. 

NXAPI is a Cisco Systems Inc. feature on recent NX-OS devices that opens a http(s) API interface using JSON-RPC to execute commands on the device. 

## Quickstart

```python

from panix import NXAPI

nxos = NXAPI('nxos_switch', username='admin', password='secret')

show_version = nxos('show version')

```
