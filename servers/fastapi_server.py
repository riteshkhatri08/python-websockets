from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.get("/hello")
def sayHello():
    return "Hi There!"


def main():
    print("Starting FastAPI server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
