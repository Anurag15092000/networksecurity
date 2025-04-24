from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_data_path:str
    test_file_path:str
    