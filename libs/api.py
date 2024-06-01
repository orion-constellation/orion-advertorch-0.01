from fastapi import FastAPI, BackgroundTasks
from contextlib import asynccontextmanager
import httpx
import asyncio

app = FastAPI()
data_stream = asyncio.create_task(post_data(data))
def main(data) -> json:
    
    @asynccontextmanager
    async def lifespan(app: FastAPI, data_stream):
        for data in data_stream():
            
            yield data_stream
            
        #data_stream.clear()

    async def post_data(data):
        return await print(data)
        
    @app.get("/")
    def read_root():
        return {"Live": "Data Stream"}

    @app.post("/report")
    def report_threat(data):
        return data

    @app.get("/health")
    def health_check():
        return "OK"
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main(data_stream), host="0.0.0.0", port=8080)