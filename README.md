# Starlette Json

## Introduction
Starlette json responses for various json serializers available in the python community.

### Why:
- Remove `ujson` dependency from core starlette package
- Add adaptors for other serializers
- Customize serializer rendering settings

## Requirements
- Python 3.6+
- [Starlette](https://github.com/encode/starlette)

## Installation
```console
$ pip install starlette-json
```

## Optional installs
Install at least one of these:
- [orjson](https://github.com/ijl/orjson) `pip install orjson`

## Usage
### Response examples
```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from starlette_json import ORJsonResponse

app = Starlette()
data = {'message': 'Hello World!'}

@app.route('/orjson')
def orjson(request):
	return ORJsonResponse(data)
```