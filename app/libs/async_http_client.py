import aiohttp


class AsyncHTTPClient:
    def __init__(self, host, port, suffix=None, header=None):
        self.host = host
        self.port = port
        self.protocol = "https" if port == 443 else "http"
        self.port_suffix = f":{port}" if port != 80 and port != 443 else ""
        match suffix:
            case None:
                self.suffix = ""
            case suffix if suffix.startswith("/"):
                self.suffix = suffix
            case _:
                self.suffix = f"/{suffix}"
        if host.startswith("http"):
            self.url = f"{host}{self.port_suffix}{self.suffix}"
        else:
            self.url = f"{self.protocol}://{self.host}{self.port_suffix}{self.suffix}"
        self.header = header
        if self.url.endswith("/"):
            self.url = self.url[:-1]

    async def _response_parser(self, response):
        content_type = response.headers.get("Content-Type", "").lower()
        if "application/json" in content_type:
            return await response.json()
        else:
            return await response.text()

    async def get(self, suffix: str = None, **kwargs):
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        current_header = kwargs.get("header", self.header)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.url}{suffix}", headers=current_header, **kwargs
            ) as response:
                return await self._response_parser(response)

    async def post(self, suffix: str = None, **kwargs):
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        current_header = kwargs.get("header", self.header)
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}{suffix}", headers=current_header, **kwargs
            ) as response:
                return await self._response_parser(response)

    async def put(self, suffix: str = None, **kwargs):
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        current_header = kwargs.get("header", self.header)
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{self.url}{suffix}", headers=current_header, **kwargs
            ) as response:
                return await self._response_parser(response)

    async def patch(self, suffix: str = None, **kwargs):
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        current_header = kwargs.get("header", self.header)
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                f"{self.url}{suffix}", headers=current_header, **kwargs
            ) as response:
                return await self._response_parser(response)

    async def delete(self, suffix: str = None, **kwargs):
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        current_header = kwargs.get("header", self.header)
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f"{self.url}{suffix}", headers=current_header, **kwargs
            ) as response:
                return await self._response_parser(response)
