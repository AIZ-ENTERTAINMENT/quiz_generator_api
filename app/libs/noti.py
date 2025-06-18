import ssl

from app.libs.async_http_client import AsyncHTTPClient

LINETOKEN = "3n95ane3hGi3neFnFrKI08ExyVC8yx74fIMKfF3nkkO"

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

noti_client = AsyncHTTPClient(
    host="https://hooks.slack.com",
    port=443,
    suffix="/services",
    header={
        "Content-Type": "application/json",
    },
)


async def slack_noti(txt):
    """
    curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
    """
    response = await noti_client.post(
        suffix="/T05RWBW4VUK/B0885365M0E/kmZYuYFEjkVRrXPlxw6yH4Qw",
        json={"text": txt},
        ssl=ssl_context,
    )
    return response


async def line_noti(txt, token=LINETOKEN):
    client = AsyncHTTPClient(
        host="https://notify-api.line.me",
        port=443,
        suffix="/api",
        header={"Authorization": f"Bearer {token}"},
    )
    await client.post(
        suffix="/notify",
        data={"message": txt},
    )
