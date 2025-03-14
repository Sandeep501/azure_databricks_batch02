from abc import ABC, abstractmethod


class ReadFile(ABC):
    @abstractmethod
    def extract(self):
        pass
    
class ReadCSV(ReadFile):
    def extract(self):
        return "extarct csv"
    
class ReadParquet(ReadFile):
    def extract(self):
        return "extract parquet"
    
    
read_csv = ReadCSV()
read_csv.extract()

read_par = ReadParquet()
read_par.extract()