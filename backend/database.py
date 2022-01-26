
# from lib2to3.pgen2 import driver

# ##mongodb driver
# import motor.motor_asyncio

# PORT = 27017


# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:' + str(PORT))

# database = client.brog
# collection = database.file_list


# async def fetch_one_pdf_file(filename):
#     document = await collection.find_one({"filename": filename})
#     return document

# async def fetch_all_pdf_file():
#     documents = []
#     cursor  = collection.find({})
#     async for document in cursor:
#         # documents.append(Pdf_File(**document))
#         pass
#     return documents

# async def create_pdf(filename, file):
#     document = {"filename":filename, "file":file}
#     result = await collection.insert_one(document)
#     # result = await collection.insert_one({"filename":"aaa"})
#     return result

# async def update_pdf(filename):
#     pass

# async def remove_pdf(filename):
#     try:
#         ##是否改为软删除
#         await collection.delete_one({"filename": filename})
#     except Exception as error:
#         print("删除失败 --- 错误如下\n %s" %(error))


from settings import SQLALCHEMY_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = SQLALCHEMY_CONFIG['url']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding = 'utf8',
    echo = True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


