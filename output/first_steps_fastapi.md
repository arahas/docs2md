---
title: First Steps - FastAPI
source: https://fastapi.tiangolo.com/tutorial/first-steps/
captured: 2025-03-31 20:24:34
---

[ ![logo](../../img/icon-white.svg) ](../.. "FastAPI") FastAPI 

[ fastapi/fastapi  ](https://github.com/fastapi/fastapi "Go to repository")

  * [ FastAPI  ](../..)
  * [ Features  ](../../features/)
  * [ Learn  ](../../learn/)

Learn 
    * [ Python Types Intro  ](../../python-types/)
    * [ Concurrency and async / await  ](../../async/)
    * [ Environment Variables  ](../../environment-variables/)
    * [ Virtual Environments  ](../../virtual-environments/)
    * [ Tutorial - User Guide  ](../)

Tutorial - User Guide 
      * First Steps  [ First Steps  ](./) Table of contents 
        * Check it 
        * Interactive API docs 
        * Alternative API docs 
        * OpenAPI 
          * "Schema" 
          * API "schema" 
          * Data "schema" 
          * OpenAPI and JSON Schema 
          * Check the `openapi.json`
          * What is OpenAPI for 
        * Recap, step by step 
          * Step 1: import `FastAPI`
          * Step 2: create a `FastAPI` "instance" 
          * Step 3: create a _path operation_
            * Path 
            * Operation 
            * Define a _path operation decorator_
          * Step 4: define the **path operation function**
          * Step 5: return the content 
        * Recap 
      * [ Path Parameters  ](../path-params/)
      * [ Query Parameters  ](../query-params/)
      * [ Request Body  ](../body/)
      * [ Query Parameters and String Validations  ](../query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](../path-params-numeric-validations/)
      * [ Query Parameter Models  ](../query-param-models/)
      * [ Body - Multiple Parameters  ](../body-multiple-params/)
      * [ Body - Fields  ](../body-fields/)
      * [ Body - Nested Models  ](../body-nested-models/)
      * [ Declare Request Example Data  ](../schema-extra-example/)
      * [ Extra Data Types  ](../extra-data-types/)
      * [ Cookie Parameters  ](../cookie-params/)
      * [ Header Parameters  ](../header-params/)
      * [ Cookie Parameter Models  ](../cookie-param-models/)
      * [ Header Parameter Models  ](../header-param-models/)
      * [ Response Model - Return Type  ](../response-model/)
      * [ Extra Models  ](../extra-models/)
      * [ Response Status Code  ](../response-status-code/)
      * [ Form Data  ](../request-forms/)
      * [ Form Models  ](../request-form-models/)
      * [ Request Files  ](../request-files/)
      * [ Request Forms and Files  ](../request-forms-and-files/)
      * [ Handling Errors  ](../handling-errors/)
      * [ Path Operation Configuration  ](../path-operation-configuration/)
      * [ JSON Compatible Encoder  ](../encoder/)
      * [ Body - Updates  ](../body-updates/)
      * [ Dependencies  ](../dependencies/)

Dependencies 
        * [ Classes as Dependencies  ](../dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](../dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](../dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](../dependencies/global-dependencies/)
        * [ Dependencies with yield  ](../dependencies/dependencies-with-yield/)
      * [ Security  ](../security/)

Security 
        * [ Security - First Steps  ](../security/first-steps/)
        * [ Get Current User  ](../security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](../security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](../security/oauth2-jwt/)
      * [ Middleware  ](../middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](../cors/)
      * [ SQL (Relational) Databases  ](../sql-databases/)
      * [ Bigger Applications - Multiple Files  ](../bigger-applications/)
      * [ Background Tasks  ](../background-tasks/)
      * [ Metadata and Docs URLs  ](../metadata/)
      * [ Static Files  ](../static-files/)
      * [ Testing  ](../testing/)
      * [ Debugging  ](../debugging/)
    * [ Advanced User Guide  ](../../advanced/)

Advanced User Guide 
      * [ Path Operation Advanced Configuration  ](../../advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](../../advanced/additional-status-codes/)
      * [ Return a Response Directly  ](../../advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](../../advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](../../advanced/additional-responses/)
      * [ Response Cookies  ](../../advanced/response-cookies/)
      * [ Response Headers  ](../../advanced/response-headers/)
      * [ Response - Change Status Code  ](../../advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](../../advanced/advanced-dependencies/)
      * [ Advanced Security  ](../../advanced/security/)

Advanced Security 
        * [ OAuth2 scopes  ](../../advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](../../advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](../../advanced/using-request-directly/)
      * [ Using Dataclasses  ](../../advanced/dataclasses/)
      * [ Advanced Middleware  ](../../advanced/middleware/)
      * [ Sub Applications - Mounts  ](../../advanced/sub-applications/)
      * [ Behind a Proxy  ](../../advanced/behind-a-proxy/)
      * [ Templates  ](../../advanced/templates/)
      * [ WebSockets  ](../../advanced/websockets/)
      * [ Lifespan Events  ](../../advanced/events/)
      * [ Testing WebSockets  ](../../advanced/testing-websockets/)
      * [ Testing Events: startup - shutdown  ](../../advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](../../advanced/testing-dependencies/)
      * [ Async Tests  ](../../advanced/async-tests/)
      * [ Settings and Environment Variables  ](../../advanced/settings/)
      * [ OpenAPI Callbacks  ](../../advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](../../advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](../../advanced/wsgi/)
      * [ Generate Clients  ](../../advanced/generate-clients/)
    * [ FastAPI CLI  ](../../fastapi-cli/)
    * [ Deployment  ](../../deployment/)

Deployment 
      * [ About FastAPI versions  ](../../deployment/versions/)
      * [ About HTTPS  ](../../deployment/https/)
      * [ Run a Server Manually  ](../../deployment/manually/)
      * [ Deployments Concepts  ](../../deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](../../deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](../../deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](../../deployment/docker/)
    * [ How To - Recipes  ](../../how-to/)

How To - Recipes 
      * [ General - How To - Recipes  ](../../how-to/general/)
      * [ GraphQL  ](../../how-to/graphql/)
      * [ Custom Request and APIRoute class  ](../../how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](../../how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](../../how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](../../how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](../../how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](../../how-to/configure-swagger-ui/)
      * [ Testing a Database  ](../../how-to/testing-database/)
  * [ Reference  ](../../reference/)

Reference 
    * [ `FastAPI` class  ](../../reference/fastapi/)
    * [ Request Parameters  ](../../reference/parameters/)
    * [ Status Codes  ](../../reference/status/)
    * [ `UploadFile` class  ](../../reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](../../reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](../../reference/dependencies/)
    * [ `APIRouter` class  ](../../reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](../../reference/background/)
    * [ `Request` class  ](../../reference/request/)
    * [ WebSockets  ](../../reference/websockets/)
    * [ `HTTPConnection` class  ](../../reference/httpconnection/)
    * [ `Response` class  ](../../reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](../../reference/responses/)
    * [ Middleware  ](../../reference/middleware/)
    * [ OpenAPI  ](../../reference/openapi/)

OpenAPI 
      * [ OpenAPI `docs` ](../../reference/openapi/docs/)
      * [ OpenAPI `models` ](../../reference/openapi/models/)
    * [ Security Tools  ](../../reference/security/)
    * [ Encoders - `jsonable_encoder` ](../../reference/encoders/)
    * [ Static Files - `StaticFiles` ](../../reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](../../reference/templating/)
    * [ Test Client - `TestClient` ](../../reference/testclient/)
  * [ FastAPI People  ](../../fastapi-people/)
  * [ Resources  ](../../resources/)

Resources 
    * [ Help FastAPI - Get Help  ](../../help-fastapi/)
    * [ Development - Contributing  ](../../contributing/)
    * [ Full Stack FastAPI Template  ](../../project-generation/)
    * [ External Links and Articles  ](../../external-links/)
    * [ FastAPI and friends newsletter  ](../../newsletter/)
    * [ Repository Management Tasks  ](../../management-tasks/)
  * [ About  ](../../about/)

About 
    * [ Alternatives, Inspiration and Comparisons  ](../../alternatives/)
    * [ History, Design and Future  ](../../history-design-future/)
    * [ Benchmarks  ](../../benchmarks/)
    * [ Repository Management  ](../../management/)
  * [ Release Notes  ](../../release-notes/)



Table of contents 

  * Check it 
  * Interactive API docs 
  * Alternative API docs 
  * OpenAPI 
    * "Schema" 
    * API "schema" 
    * Data "schema" 
    * OpenAPI and JSON Schema 
    * Check the `openapi.json`
    * What is OpenAPI for 
  * Recap, step by step 
    * Step 1: import `FastAPI`
    * Step 2: create a `FastAPI` "instance" 
    * Step 3: create a _path operation_
      * Path 
      * Operation 
      * Define a _path operation decorator_
    * Step 4: define the **path operation function**
    * Step 5: return the content 
  * Recap 



  1. [ FastAPI  ](../..)
  2. [ Learn  ](../../learn/)
  3. [ Tutorial - User Guide  ](../)



# First Steps¶

The simplest FastAPI file could look like this:

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

Copy that to a file `main.py`.

Run the live server:
    
    
    $ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>
    
      <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀
    
                 Searching for package file structure from directories
                 with <font color="#3465A4">__init__.py</font> files
                 Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>
    
       <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py
    
         <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
                 the following code:
    
                 <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>
    
          <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>
    
       <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
       <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>
    
          <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
                 <b>fastapi run</b>
    
                 Logs:
    
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
                 <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
                 to quit<b>)</b>
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
         <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
    

In the output, there's a line with something like:
    
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    

That line shows the URL where your app is being served, in your local machine.

### Check it¶

Open your browser at <http://127.0.0.1:8000>.

You will see the JSON response as:
    
    
    {"message": "Hello World"}
    

### Interactive API docs¶

Now go to <http://127.0.0.1:8000/docs>.

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs¶

And now, go to <http://127.0.0.1:8000/redoc>.

You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI¶

**FastAPI** generates a "schema" with all your API using the **OpenAPI** standard for defining APIs.

#### "Schema"¶

A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

#### API "schema"¶

In this case, [OpenAPI](https://github.com/OAI/OpenAPI-Specification) is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc.

#### Data "schema"¶

The term "schema" might also refer to the shape of some data, like a JSON content.

In that case, it would mean the JSON attributes, and data types they have, etc.

#### OpenAPI and JSON Schema¶

OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using **JSON Schema** , the standard for JSON data schemas.

#### Check the `openapi.json`¶

If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

You can see it directly at: <http://127.0.0.1:8000/openapi.json>.

It will show a JSON starting with something like:
    
    
    {
        "openapi": "3.1.0",
        "info": {
            "title": "FastAPI",
            "version": "0.1.0"
        },
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
    
    
    
    ...
    

#### What is OpenAPI for¶

The OpenAPI schema is what powers the two interactive documentation systems included.

And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with **FastAPI**.

You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.

## Recap, step by step¶

### Step 1: import `FastAPI`¶

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

`FastAPI` is a Python class that provides all the functionality for your API.

Technical Details

`FastAPI` is a class that inherits directly from `Starlette`.

You can use all the [Starlette](https://www.starlette.io/) functionality with `FastAPI` too.

### Step 2: create a `FastAPI` "instance"¶

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

Here the `app` variable will be an "instance" of the class `FastAPI`.

This will be the main point of interaction to create all your API.

### Step 3: create a _path operation_¶

#### Path¶

"Path" here refers to the last part of the URL starting from the first `/`.

So, in a URL like:
    
    
    https://example.com/items/foo
    

...the path would be:
    
    
    /items/foo
    

Info

A "path" is also commonly called an "endpoint" or a "route".

While building an API, the "path" is the main way to separate "concerns" and "resources".

#### Operation¶

"Operation" here refers to one of the HTTP "methods".

One of:

  * `POST`
  * `GET`
  * `PUT`
  * `DELETE`



...and the more exotic ones:

  * `OPTIONS`
  * `HEAD`
  * `PATCH`
  * `TRACE`



In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

* * *

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

  * `POST`: to create data.
  * `GET`: to read data.
  * `PUT`: to update data.
  * `DELETE`: to delete data.



So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "**operations** " too.

#### Define a _path operation decorator_¶

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

The `@app.get("/")` tells **FastAPI** that the function right below is in charge of handling requests that go to:

  * the path `/`
  * using a `get` operation



`@decorator` Info

That `@something` syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells **FastAPI** that the function below corresponds to the **path** `/` with an **operation** `get`.

It is the "**path operation decorator** ".

You can also use the other operations:

  * `@app.post()`
  * `@app.put()`
  * `@app.delete()`



And the more exotic ones:

  * `@app.options()`
  * `@app.head()`
  * `@app.patch()`
  * `@app.trace()`



Tip

You are free to use each operation (HTTP method) as you wish.

**FastAPI** doesn't enforce any specific meaning.

The information here is presented as a guideline, not a requirement.

For example, when using GraphQL you normally perform all the actions using only `POST` operations.

### Step 4: define the **path operation function**¶

This is our "**path operation function** ":

  * **path** : is `/`.
  * **operation** : is `get`.
  * **function** : is the function below the "decorator" (below `@app.get("/")`).



Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

This is a Python function.

It will be called by **FastAPI** whenever it receives a request to the URL "`/`" using a `GET` operation.

In this case, it is an `async` function.

* * *

You could also define it as a normal function instead of `async def`:

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def root():
        return {"message": "Hello World"}
    

Note

If you don't know the difference, check the [Async: _"In a hurry?"_](../../async/#in-a-hurry).

### Step 5: return the content¶

Python 3.8+
    
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    

You can return a `dict`, `list`, singular values as `str`, `int`, etc.

You can also return Pydantic models (you'll see more about that later).

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.

## Recap¶

  * Import `FastAPI`.
  * Create an `app` instance.
  * Write a **path operation decorator** using decorators like `@app.get("/")`.
  * Define a **path operation function** ; for example, `def root(): ...`.
  * Run the development server using the command `fastapi dev`.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! 

Back to top 
  *[`get` operation]: an HTTP GET method
