import sys
import os
from fastapi import FastAPI
from data import # @TODO STREAMING
from libs.custom_loggers.file_logging import setup_logging




class OrionServer:
    def __init__(self, app=FastAPI(root_path="orion-threat-intel}/api/v1")):
        _logger = setup_logging()

        @app.get("/")
        def read_root():
            return {"Hello": "World This is Orion Test"}

        @app.post("/encrypt")
        def encrypt_data(data):
            return data

        @app.get("/health")
        def health_check():
            return "OK This shit kinda works do routes"
        
def main():
    try:
        server = OrionServer()
        return server
    except Exception as e:
        _logger.error(e, exec_info=True)
        
    if __name__==__main__:
        main()
