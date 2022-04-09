# mongodb driver
import asyncio
from xml.dom.minidom import Document
from motor.motor_asyncio import AsyncIOMotorClient
from settings import SQLALCHEMY_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PORT = 27017

client: AsyncIOMotorClient = None

database = None
collection_file = None
collection_profile = None

SQLALCHEMY_DATABASE_URL = SQLALCHEMY_CONFIG['url']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding='utf8',
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def connect_mongo():
    global client
    global database
    global collection_file
    global collection_profile
    client = AsyncIOMotorClient('mongodb://localhost:' + str(PORT))
    database = client.brog
    collection_file = database.file_list
    collection_profile = database.user_profile


async def close_mongo():
    client.close()


async def fetch_one_pdf_file(filename):
    document = await collection_file.find_one({"filename": filename})
    return document


async def fetch_all_pdf_file():
    documents = []
    cursor = collection_file.find({})
    async for document in cursor:
        # documents.append(Pdf_File(**document))
        pass
    return documents


async def create_pdf(filename, file):
    document = {"filename": filename, "file": file}
    result = await collection_file.insert_one(document)
    # result = await collection.insert_one({"filename":"aaa"})
    return result


async def create_document(term, ref_list, bid):
    # doc_tmp = await collection.find({"term":term, "bid":bid})
    document = {"term": term, "ref": ref_list, "bid": bid}
    result = await collection_file.insert_one(document)
    # result = await collection.insert_one({"filename":"aaa"})
    return result


async def create_profile(uid: str, field_list: list):
    document = {"uid": uid, "fields": field_list}
    result = await collection_profile.insert_one(document)
    return result


async def update_pdf(filename):
    pass


async def remove_pdf(filename):
    try:
        ##是否改为软删除
        await collection_file.delete_one({"filename": filename})
    except Exception as error:
        print("删除失败 --- 错误如下\n %s" % (error))
