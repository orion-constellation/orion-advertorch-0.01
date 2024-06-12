"""
Uses Rustworkx to generate a Graph of different types
- Implements PyDantic DataVerification Models to Ensure Data Integrity
- @TODO IN GENERAL. WORK OUT YOUR NAMING SCHEME AND DATA MODELLING


"""
import os
import random
from typing import List, Dict, Tuple, Optional

import rustworkx as rx
import uuid
from uuid import uuid4
from models import IGraphInit, INodeInit, IRelInit, IGraphGen
from dotenv import load_dotenv
load_dotenv()

from libs.custom_loggers.file_logging import setup_logging

_logger = setup_logging()


class GraphInit(IGraphInit):
    def __init__(self, gr):
        self.rx.graph = gr
        self.id = f"G_{uuid.uuidv4}"

class NodeInit(INodeInit):
    def __init__(self, nodes: Dict, relationships: Dict, id: uuidv4):
        self.name = f"G_{uuidv4()}"
        self.nodes = nodes
        self.relationships = {relationships}


    def __init__(self, gr, nodes)
        for ix, node in self.nodes.enumerate():
            self.gr.add_parent(self.nodes[ix-1])
            self.add_node(self.nodes[node.name])

class RelInit(IRelInit):
    def __init__(gr, nodes, rels):
        pass #@TODO FIX THIS 
    
    def init_relationships(self, node1, node2, relationship):
        relationship = self.name
        self.node1 = node1
        self.node2 = node2
        self.relationship  = relationship
  
      
graph1 = GraphElements(gr)
print(graph1)