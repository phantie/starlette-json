from typing import Any
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class ORJsonMiddleware(BaseHTTPMiddleware):
	async def dispatch(self, request, call_next):
		async def orjson_loads(self) -> Any:
			from orjson import loads

			if not hasattr(self, '_json'):
				body = await self.body()
				self._json = loads(body)
			return self._json

		response = await call_next(request)
		response.json = orjson_loads
		return response

class ORJsonResponse(Response):

	media_type = "application/json"

	def __init__(self, *args, **kwargs):
		valid_args = {'default','option'}
		self.render_args = {k:v for k,v in kwargs.items() if k in valid_args}
		super().__init__(*args, **{k:v for k,v in kwargs.items() if k not in valid_args})

	def render(self, content) -> bytes:
		from orjson import dumps
		return dumps(content, **self.render_args)
