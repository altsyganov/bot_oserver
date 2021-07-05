import aiohttp
import logging

reject_text = {
    'nei': 'Слишком плохо описан запрос',
    'cbr': 'Такого больше не может повторится',
    'aiw': 'Уже в работе'
}


# Вспомогательные функции для обращений в апи
async def get_request(session: aiohttp.ClientSession, url: str, query_params: dict = None) -> aiohttp.ClientResponse.json:
    async with session.get(url, params=query_params) as response:
        logging.info(response.status)
        return await response.json()


async def post_request(session: aiohttp.ClientSession, url: str, json: dict, query_params: dict = None) -> aiohttp.ClientResponse.json:
    async with session.post(url, json=json, params=query_params) as response:
        logging.info(response.status)
        if await response.text():
            return await response.json()


async def patch_request(session: aiohttp.ClientSession, url: str, json: dict, query_params: dict = None) -> aiohttp.ClientResponse.json:
    async with session.patch(url, json=json, params=query_params) as response:
        logging.info(response.status)

        return await response.json()


async def delete_request(session: aiohttp.ClientSession, url: str, query_params: dict = None) -> aiohttp.ClientResponse.json:
    async with session.delete(url, params=query_params) as response:
        logging.info(response.status)
        return await response.json()

