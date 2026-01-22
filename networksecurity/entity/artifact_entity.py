from dataclasses import dataclass

#@dataclass used to create classes with variables , without writing init method and functions
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

