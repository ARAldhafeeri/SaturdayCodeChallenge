import os

from fastapi import FastAPI

from models import Document, SearchResults, SearchQuery

from whoosh.index import create_in # simple fs to create index

from whoosh.fields import *

from whoosh.qparser import QueryParser


app = FastAPI()

schema = Schema(
 # TODO: Add schema fields
)

# TODO: add full-text index directory if not exists
if not os.path.exists("index"):
    os.mkdir("index")

ix = create_in("index", schema)

# index endpoint
@app.post("/index/")
async def index(doc : Document):
    # TODO: write document to index
    return { "message": "Document indexed successfully"}

# search endpoint
@app.post("/search/")
async def search(query: SearchQuery):
    res = []
    # TODO : search index and return results
    return res