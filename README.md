# FastAPI

Python backend framework. One of the fastest frameworks, directly compete with Node.js according to benchmarks. Widely used by multiple companies like Netflix and Microsoft.

Uses uvicorn as server (software that distributes an application), Starlette (low-level backend framework) and Pydantic to define models.

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