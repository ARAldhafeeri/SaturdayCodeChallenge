# Full-Text Search Service Design Document

## 1. Introduction
The Full-Text Search Service is designed to provide users with efficient search capabilities across a collection of documents or data sources. The service utilizes Whoosh library which is fast, featurefull full-text indexing and searching library for powerful full-text search functionality and is accessible via a FastAPI-based RESTful API.

## 2. Goals and Objectives
- Enable users to perform fast and accurate full-text searches.
- Provide a scalable and reliable search service for various applications and use cases.
- Offer an intuitive API for integrating search functionality into client applications.

## 3. Scope
The Full-Text Search Service includes features for indexing documents, performing search queries, and retrieving search results. It does not include advanced features such as faceted search or search result ranking algorithms.

## 4. Architecture Overview
The service follows a client-server architecture. The backend is built using FastAPI, while the search functionality is powered by whoosh library.

## 5. Components and Modules
- **Backend**: FastAPI application handles HTTP requests and interacts with whoosh library for indexing and searching documents.


## 6. Technologies Used
- FastAPI for backend development.
- whoosh library for full-text search capabilities.
- Python for scripting and application logic.

## 7. Data Model
The data model includes documents that are indexed for full-text search. Each document consists of one or more fields, which can be searched individually or collectively.
- Document:
    - Title: The title of the document.
    - Content: The main text content of the document.
    - URL: The URL or identifier of the document.
- SearchResult:
    - Score: The relevance score of the search result.
    - URL: The URL of the document matching the search query.
- SearchQuery:
    - Query: The full-text search query submitted by the user.

## 8. User Interface (UI) Design
The service does not have a user interface. It is accessed programmatically through the FastAPI-based API endpoints.

## 9. Functional Requirements
- Indexing documents: Users can submit documents to be indexed.
- Searching documents: Users can perform full-text search queries.
- Retrieving search results: Users receive relevant search results based on their queries.

## 10. Non-Functional Requirements
- Performance: Searches should return results within milliseconds for optimal user experience.
- Scalability: The service should handle a large volume of documents and search queries.
- Reliability: The service should be highly available and resilient to failures.

## 11. Use Cases
- User submits documents for indexing.
- User performs a full-text search query.
- User receives search results matching the query.

## end points 
- POST /index: Index a new document.
    + request :
        ```
        {
            "title": "document_title",
            "content": "document_content"
            "document_url" : "document_url"
        }
        ```
    + response :
        ```
        {
            "message": "Document indexed successfully",
        }
        ```
- POST /search: Perform a full-text search query.
    + request :
        ```
        {
            "query": "search_query"
        }
        ```
    + response :
        ```
        {
            "results": [
                {
                    "score": 0.75
                    "url": "document_url",
                },
                {
                    "score": 0.75
                    "url": "document_url",
                }
            ]
        }
        ```

