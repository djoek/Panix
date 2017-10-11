import json
import requests


class NXAPIException(Exception):
    def __init__(self, message, code, data):
        super(NXAPIException, self).__init__(message)

        self.code = code
        self.data = data
        self.message = message

    def __str__(self):
        return "<NXAPIException ({code}: {mesg!s}) {data!r}>".format(
            code=self.code,
            mesg=self.message,
            data=self.data,
        )


class NXAPI(object):

    def __init__(self, hostname, username, password, *, scheme='https', port=8080):
        self.url = '{scheme}://{hostname}:{port!s}/ins'.format(
            scheme=scheme, hostname=hostname, port=port)

        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers['Content-Type'] = 'application/json-rpc'

        self._ids = (r for r in range(1, 100000))

    def _execute(self, cmd, method="cli_ascii"):

        payload = {
            "params": {
                "cmd": cmd,
                "version": 1.2
            },
            "jsonrpc": "2.0",
            "method": method,
            "id": next(self._ids)
        }

        response = self.session.post(
            self.url,
            data=json.dumps(payload),
        )
        jsonrpc_response = response.json()
        error = jsonrpc_response.get('error')
        if error is not None:
            raise NXAPIException(
                message=error['message'],
                code=error['code'],
                data=error['data'].get('msg', error['data'])
            )
        return jsonrpc_response['result']

    def __call__(self, command, *, parsed=False):
        method = 'cli' if parsed else 'cli_ascii'
        key = 'body' if parsed else 'msg'

        result = self._execute(command, method=method)
        if result is not None:
            if key in result:
                return result.get(key)
        else:
            if parsed:
                raise NXAPIException("No parsed data available for this command", code=-1, data=None)
        return result
