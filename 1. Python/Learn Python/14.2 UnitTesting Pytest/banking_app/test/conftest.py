import os
import sys

# to get absolute path of the project root directory

project_root=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print("Project root: ",project_root)

sys.path.insert(0,project_root)