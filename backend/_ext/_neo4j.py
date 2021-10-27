__all__ = ["CypherEngine"]


from neo4j import *
from .ext_settings import NEO4J_CONFIG as CONFIG
from typing import Callable, Tuple
from functools import wraps


class CypherEngine:
    def __init__(self, uri: str, auth: Tuple[str, str]):
        self.driver: Driver = GraphDatabase.driver(uri, auth)

    @staticmethod
    def _wrapQuery(queryStr) -> Callable:
        async def inner(tx, *args, **kwargs):
            return list(tx.run(queryStr, *args, **kwargs))
        return inner

    async def query(self, queryStr, *args, **kwargs):
        wrappedQuery = self._wrapQuery(queryStr)
        with self.driver.session() as session:
            result = await session.read_transaction(wrappedQuery, *args, **kwargs)
            if not result:
                return None
            return result

    async def write(self, queryStr, *args, **kwargs):
        wrappedQuery = self._wrapQuery(queryStr)
        with self.driver.session() as session:
            result = await session.write_transaction(wrappedQuery, *args, **kwargs)
            if not result:
                return None
            return result
