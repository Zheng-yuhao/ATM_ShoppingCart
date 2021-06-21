"""
The start entrance
"""


import os
import sys
from core import src


project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)

src.run()