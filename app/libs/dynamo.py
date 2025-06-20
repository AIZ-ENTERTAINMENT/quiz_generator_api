import os
from functools import wraps

import aioboto3
import boto3
from botocore.config import Config
from fastapi import HTTPException


class DynamoDBClient:
    access_key = os.environ["AWS_ACCESS_KEY"]
    secret_key = os.environ["AWS_SECRET_KEY"]
    region = "ap-northeast-2"

    _dynamodb = boto3.client(
        "dynamodb",
        endpoint_url="http://localhost:8001",
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )

    def table(cls, table_name):
        return cls._dynamodb.Table(table_name)

    @classmethod
    def create_table(
        cls,
        table_name: str,
        key_schema: list,
        attribute_definitions: list,
        provisioned_throughput: dict,
    ):
        table = cls._dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput,
        )
        table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
        return table

    @classmethod
    def write_to_dynamodb(cls, table_name: str, item: dict):
        table = cls.table(table_name)
        response = table.put_item(Item=item)
        return response

    @classmethod
    def read_from_dynamodb(cls, table_name: str, key: dict):
        table = cls.table(table_name)
        response = table.get_item(Key=key)
        if "Item" in response:
            return response["Item"]
        else:
            return None


    @classmethod
    def delete_item(cls, table_name: str, key: dict):
        table = cls.table(table_name)
        response = table.delete_item(Key=key)
        return response

    @classmethod
    def drop_table(cls, table_name: str):
        table = cls.table(table_name)
        response = table.delete()
        return response

    @classmethod
    def show_all_tables(cls):
        response = cls.table(table_name)
        return [table.name for table in response]


class AsyncDynamoDBClient:
    access_key = os.environ["AWS_ACCESS_KEY"]
    secret_key = os.environ["AWS_SECRET_KEY"]
    endpoint_url = os.environ.get("AWS_ENDPOINT_URL_DYNAMO")
    deploy_phase = os.environ.get("DEPLOY_PHASE")
    suffix = "" if deploy_phase == "local" else f"_{deploy_phase}"
    config = Config(
        connect_timeout=2.0,
        read_timeout=2.0,
        retries={
            "total_max_attempts": 3,
        },
    )
    region = "ap-northeast-2"
    _session = aioboto3.Session(
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )

    @classmethod
    def session(cls):
        return cls._session

    @classmethod
    async def create_table(
        cls,
        table_name: str,
        key_schema: list,
        attribute_definitions: list,
        provisioned_throughput: dict,
    ):
        async with cls._session.resource(
            "dynamodb", endpoint_url=cls.endpoint_url
        ) as dynamodb:
            table = await dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                ProvisionedThroughput=provisioned_throughput,
            )
            waiter = table.meta.client.get_waiter("table_exists")
            await waiter.wait(TableName=table_name)  # 테이블 생성완료까지 대기.
            return table

    @classmethod
    def with_dynamo_table(cls, table_name: str):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                if "table_session" in kwargs:
                    return await func(*args, **kwargs)
                else:
                    async with cls._session.resource(
                        "dynamodb", endpoint_url=cls.endpoint_url, config=cls.config
                    ) as dynamodb:
                        table = await dynamodb.Table(table_name + cls.suffix)
                        return await func(*args, table_session=table, **kwargs)

            return wrapper

        return decorator

    @classmethod
    def with_dynamo_session(cls, func):
        # deploy phase에 따른 suffix 의 변화를 각자의 환경에 맞게 설정해주세요.
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if "dynamodb" in kwargs:
                return await func(*args, **kwargs)
            else:
                async with cls._session.resource(
                    "dynamodb", endpoint_url=cls.endpoint_url, config=cls.config
                ) as dynamodb:
                    return await func(*args, dynamodb=dynamodb, **kwargs)

        return wrapper

    @classmethod
    def get_dynamo_table(cls, table_name: str, dynamodb):
        deploy_phase = os.environ.get("DEPLOY_PHASE")
        if not deploy_phase:
            raise HTTPException(400, detail="Deploy phase is not set")
        if deploy_phase == "local":
            suffix = ""
        else:
            suffix = f"_{deploy_phase}"
        return dynamodb.Table(table_name + suffix)
