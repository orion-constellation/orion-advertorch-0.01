    """
    API between RL framework on Ray:
    - FastAPI
    - Endpoint connection using 
    
    
    """
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from typing import List, Dict, Any, Optional
import mypy
from file_logging_utils import setup_logging

logger = setup_logging()# type: ignore

app = FastAPI()

class AgentData(BaseModel) -> None:
    agent_id: int
    observations: List
    actions: List
    rewards: List

@app.post("/agent_data/")
async def receive_data(data: AgentData):
    asyncio.create_task(log_processing(data.agent_id))  # Non-blocking call
    response = await process_agent_data(data)
    if data["status"] == "Failed":
        raise HTTPException(status_code=response.status_code, detail="Data processing failed")
    
    
    return response

async def process_agent_data(data: AgentData):
    print(f"Processing data for agent {data.agent_id}")
    
    act_rew = zip(data.actions, data.rewards)
    
    
    return {
        "status": "Received", 
        "agent_id": data.agent_id,
        
        
        }
    

async def log_processing(agent_id):
    # Example of an asynchronous logging function that could log to a file or a database
    await asyncio.sleep(0.5)  # Simulate some I/O operation
    print(f"Log entry created for agent {agent_id}")
