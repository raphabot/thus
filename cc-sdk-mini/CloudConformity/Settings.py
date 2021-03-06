
class Settings:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    def Create(self, data):
        return self._connection.post(url='/settings/communication', payload=data)
    def List(self, channel=None, accountID=None, includeParents=None):
        params = {}
        if channel:
            params['channel'] = channel
        if accountID:
            params['accountId'] = accountID
        if includeParents:
            params['includeParents'] = str(includeParents)
        return self._connection.get(url='/settings/communication', params=params)
    def describe(self, id):
        return self._connection.get(url='/settings/{id}'.format(id))
    def update(self, id, data):
        return self._connection.patch(url='settings/communication/{settingId}'.format(settingId=id), payload=data)
    def delete(self, id):
        return self._connection.delete(url='/settings/{id}'.format(id))
