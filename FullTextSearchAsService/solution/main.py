from fastapi import FastAPI, Query
import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from models import Document, SearchResults, SearchQuery

app = FastAPI()

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), url=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)



@app.post("/index/")
async def submit_document(document : Document ):
    writer = ix.writer()
    writer.add_document(title=document.title, content=document.content, url=document.url)
    writer.commit()
    return {"message": "Document submitted successfully"}

@app.post("/search/")
async def search(query : SearchQuery):
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        print(query_parser)
        query = query_parser.parse(query.query)
        results = searcher.search(query)
        search_results = []
        print(results)
        for result in results:
            search_results.append(
                SearchResults(
                    score=result.score, 
                    url=result["url"]
                )
            )
    return search_results

if __name__ == "__main__":
    uvicorn.run(app, port=8000)