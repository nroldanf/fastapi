# FastAPI

Python backend framework. One of the fastest frameworks, directly compete with Node.js according to benchmarks. Widely used by multiple companies like Netflix and Microsoft.

Uses uvicorn as server (software that distributes an application), Starlette (low-level backend framework) and Pydantic to define models.

## Path Operations

### Operations

- GET - Client brings information from the server and send info in the path or query params.
- POST - Client sends JSON information (request) and receives a JSON response from the server.
- PUT - Updates information
- DELETE - Deletes information
- OPTIONS
- HEAD
- PATCH
- TRACE

### Path parameters

Inside a path, a variable can be defined using the following notaiton:  `/route-name/{variable-name}`. 

In general terms, these variables are used to point a resource within a collection. For example, a user_id.

Path parameters are `mandatory`.

### Query parameters

If information want to be send within the route, but don't want them to be mandatory, we can use query parameters. Query parameters looks like this:

`/route-name?username=myname&age=20&height=184`

## Request Body

When using HTTP we send the following:

- Body
- Headers

When a client send information to a server: `Request`
When a server sends information back to the client: `Response`

Both are send in JSON format and both can have headers values.

## Models

Descriptive representation of an real world entity e.g. an user. Models in FastAPI are created using Pydantic and this is done using Pydantic `BaseModel`

## Validations

For query params we can use `Query` class.

- For `str`
    - min_lenght
    - max_lenght
    - regex
- For `int`
    - ge (greater or equal to)
    - le (less or equal to)
    - gt (greater than)
    - lt (less than)

## Order matter when defining path operations

https://fastapi.tiangolo.com/tutorial/path-params/#order-matters

## Some commands

### Start a server
Use uvicorn to start a server that serves requests and reload when code is modified (hot reloader).
```
uvicorn <name-of-file>:<name-of-fast-api-instance> --reload
```

### Access the documentation
OpenAPI is a set of rules that describes how to defined an API. OpenAPI specification can be visualized using `Swagger UI` or `Redoc`. To access the automatic generated docs using OpenAPI specification go to `/docs` path for swagger UI and `/redoc` for Redoc.

For example, openAPI specification:
```JSON
{
	"openapi": "3.0.2",
	"info": {
		"title": "FastAPI",
		"version": "0.1.0"
	},
	"paths": {
		"/": {
			"get": {
				"summary": "Home",
				"operationId": "home__get",
				"responses": {
					"200": {
						"description": "Successful Response",
						"content": {
							"application/json": {
								"schema": {}
							}
						}
					}
				}
			}
		}
	}
}
```
