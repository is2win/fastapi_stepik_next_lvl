from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My first project in FastAPI"}


@app.get("/hello/{user}")
async def welcome_user(user: str) -> dict:
    return {"message": f"Hello {user}!"}


@app.get("/user")
async def login(username: str, age: int | None = None) -> dict:
    return {"user": username, "age": age}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name:str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}


# @app.get("/product/{id}")
# async def detail_view(id:int) -> dict:
#     return {"product": f"Stock number {id}"}
@app.get("/product")
async def detail_view(id:int) -> dict:
    return {"product": f"Stock number {id}"}

# @app.get("/users/{name}/{age}")
# async def users(name: str, age: int) -> dict:
#     return {"user_name": name, "user_age": age}
@app.get("/users")
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {"user_name": name, "user_age": age}

@app.get("/users/admin")
async def admin() -> dict:
    return {"message": "Hello admin"}


@app.get("/users/{name}")
async def users(name: str) -> dict:
    return {"user_name": name}

country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}


@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    return {"country": country, "cities": country_dict.get(country)[:limit]}