import numpy as np

def generate_random_list(size: int, max_value: int) -> list:
    return [np.random.randint(1, max_value) for _ in range(size)]
import os

def generate_flowchart():
    """
    Returns the path to the flowchart image in the assets directory.
    Ensures the file exists before returning.
    """
    flowchart_path = os.path.join("assets", "flowchart.png")
    if not os.path.exists(flowchart_path):
        raise FileNotFoundError(f"Flowchart image not found at {flowchart_path}")
    return flowchart_path