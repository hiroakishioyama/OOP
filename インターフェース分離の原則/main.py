from abc import ABC, abstractmethod

class Printer(ABC):
    """
    印刷関連のタスクのためのインターフェース。
    """
    @abstractmethod
    def print_document(self, document):
        """
        文書を印刷する。
        """
        pass

class Scanner(ABC):
    """
    スキャナー関連のタスクのためのインターフェース。
    """
    @abstractmethod
    def scan_document(self, document):
        """
        文書をスキャンする。
        """
        pass

class Fax(ABC):
    """
    FAX関連のタスクのためのインターフェース。
    """
    @abstractmethod
    def fax_document(self, document):
        """
        文書をFAX送信する。
        """
        pass

class MultiFunctionPrinter(Printer, Scanner, Fax):
    """
    複合機クラス。印刷、スキャン、FAXの全機能を提供。
    """
    def print_document(self, document):
        print("Document printed.")

    def scan_document(self, document):
        print("Document scanned.")

    def fax_document(self, document):
        print("Document faxed.")

class SimplePrinter(Printer):
    """
    基本的な印刷機能のみを提供するプリンタクラス。
    """
    def print_document(self, document):
        print("Document printed.")

# 使用例
printer = SimplePrinter()
printer.print_document("Sample Document")  # 文書を印刷

mf_printer = MultiFunctionPrinter()
mf_printer.print_document("Sample Document")
mf_printer.scan_document("Sample Document")
mf_printer.fax_document("Sample Document")
