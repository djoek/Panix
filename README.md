# Panix, an NXAPI library

Panix is a python3 NXAPI convenience library.  It internally uses json and returns the user python native data structures. It leverages requests for the json-rpc handling. 

NXAPI is a Cisco Systems Inc. feature on recent NX-OS devices that opens a http(s) API interface using JSON-RPC to execute commands on the device. 

Panix offers some helper classes to make the structured output more workable. 


## Quickstart

```python

from panix import NXAPI

nxos = NXAPI('nxos_switch', username='admin', password='secret', scheme='https', port=8080)


# Text output of the command
sh_ver_text = nxos('show version')

# Some commands have structured output
sh_ver_data = nxos('show version', parsed=True)

# The structure isn't that great, Panix has helpers
from panix.helpers.version import version_helper

sh_ver_data = version_helper(sh_ver_data)


print(sh_ver_data['system_version'])
# '8.1(1)'


```


