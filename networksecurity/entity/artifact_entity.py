from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str