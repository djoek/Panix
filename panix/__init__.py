import json
import requests


class NXAPIException(Exception):
    def __init__(self, message, code, data):
        super(NXAPIException, self).__init__(message)

        self.code = code
        self.data = data
        self.message = message

    def __str__(self):
        return "<NXAPIException ({code}) {mesg}. {data}>".format(
            code=self.code,
            mesg=self.message,
            data=' '.join([': '.join(x) for x in self.data.items()])
        )


class NXAPI(object):

    def __init__(self, hostname, username, password, *, scheme='https', port=8080):
        self.url = '{scheme}://{hostname}:{port!s}/ins'.format(
            scheme=scheme, hostname=hostname, port=port
        )

        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers['Content-Type'] = 'application/json-rpc'

        self._ids = (r for r in range(1, 100000))

    def __call__(self, cmd, method="cli_ascii"):

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

        response.raise_for_status()
        jsonrpc_response = response.json()

        error = jsonrpc_response.get('error')
        if error is not None:
            raise NXAPIException(
                message=error['message'],
                code=error['code'],
                data=error['data']
            )
        return jsonrpc_response['result']

    def cli(self, *commands):
        assert len(commands) > 0

        result = self(' ; '.join(commands), method='cli')
        return result.get('body')

    def cli_ascii(self, *commands):
        assert len(commands) > 0

        result = self(' ; '.join(commands), method='cli_ascii')
        return result.get('msg', '')
