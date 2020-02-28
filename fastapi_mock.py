import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"name": "hello world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    """
    - item id
    - query string

    """
    return {"item_id": item_id, "q": q}


def main():
    # for local
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()
