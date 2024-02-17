from pydantic  import BaseModel

class Document(BaseModel):
    content: str
    title: str
    url: str

class SearchQuery(BaseModel):
    query: str

class SearchResults(BaseModel):
    score: float
    url: str