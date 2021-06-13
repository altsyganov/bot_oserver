from .utils import get_request, post_request, patch_request


class API:

    def __init__(self, session):
        self.base_url = 'http://localhost:8000/api/{}'
        self.session = session

    def _make_url(self, path):
        return self.base_url.format(path)

    async def list_clients(self):
        url = self._make_url('clients/')
        return await get_request(self.session, url)

    async def create_client(self, payload):
        url = self._make_url('clients/')
        return await post_request(session=self.session, url=url, json=payload)

    async def create_request(self, payload):
        url = self._make_url('requests/')
        return await post_request(session=self.session, url=url, json=payload)

    async def update_request(self, task_id, payload):
        url = self._make_url('requests/{}/').format(task_id)
        return await patch_request(session=self.session, url=url, json=payload)

    async def retrieve_bot(self, ping_name):
        url = self._make_url('bots/')
        query_params = {'ping_name': ping_name}
        return await get_request(session=self.session, query_params=query_params, url=url)
