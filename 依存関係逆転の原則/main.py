from abc import ABC, abstractmethod

class DataStore(ABC):
    """
    データの保存と取得のための抽象基底クラス。
    このインターフェースを実装することで、様々な種類のデータストアに対応可能。
    """
    @abstractmethod
    def save_data(self, data):
        """
        データを保存する抽象メソッド。
        """
        pass

    @abstractmethod
    def retrieve_data(self, key):
        """
        データを取得する抽象メソッド。
        """
        pass

class Database(DataStore):
    """
    データベースにデータを保存し、取得する具体的なクラス。
    """
    def save_data(self, data):
        print(f"Data '{data}' saved to the database.")

    def retrieve_data(self, key):
        print(f"Data with key '{key}' retrieved from the database.")
        return "Some data"

class FileManager(DataStore):
    """
    ファイルにデータを保存し、取得する具体的なクラス。
    """
    def save_data(self, data):
        print(f"Data '{data}' saved to a file.")

    def retrieve_data(self, key):
        print(f"Data with key '{key}' retrieved from a file.")
        return "Some data"

class DataProcessor:
    """
    データ処理を行う高レベルのクラス。低レベルのデータストアに直接依存せず、
    DataStoreインターフェースに依存する。
    """
    def __init__(self, storage: DataStore):
        self.storage = storage

    def process_data(self, data):
        """
        データを処理して保存します。
        """
        self.storage.save_data(data)

# 使用例
database = Database()
processor = DataProcessor(database)
processor.process_data("Example data")

file_manager = FileManager()
processor = DataProcessor(file_manager)
processor.process_data("Example data")
