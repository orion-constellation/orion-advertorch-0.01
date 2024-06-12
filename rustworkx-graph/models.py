from pydantic import BaseModel
import rustworkx as rx
from typing import Dict, List, Tuple, Optional, Union, Enum

class IGraphInit(BaseModel):
    graph: rx.PyGraph #@TODO Confirm PyGraph Member
    nodes: Dict(str) #TODO IS DICT OR LIST?
    relationships: List[Tuple: str | int ] #TODO Again is string or int?
    properties: Optional #TODO Is Optional?
    
class INodeInit(BaseModel):
    graph: GraphInit
    nodes: Enum[List[str]] #TODO Is List, string etc

class IRelInit(BaseModel):
    graph: GraphInit
    nodes: NodeInit
    rels: Enum[List[str]] #TODO Is List, string etc
    
class IGraphGen(BaseModel):
    #TODO Read Rustworkx Documentation to determine the appropriateness
    
    