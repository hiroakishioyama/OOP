class Report:
    """
    報告書を生成するための抽象基底クラス。
    このクラスは拡張に対して開かれていますが、変更に対して閉じています。
    """

    def generate(self):
        """
        報告書を生成するメソッド。
        具体的な実装はサブクラスに依存します。
        """
        raise NotImplementedError("Subclass must implement abstract method")

class PDFReport(Report):
    """
    PDF形式で報告書を生成するクラス。
    """

    def generate(self):
        """
        PDF報告書を生成してその内容を返します。
        """
        return "PDF report generated"

class ExcelReport(Report):
    """
    Excel形式で報告書を生成するクラス。
    """

    def generate(self):
        """
        Excel報告書を生成してその内容を返します。
        """
        return "Excel report generated"

# 使用例
reports = [PDFReport(), ExcelReport()]
for report in reports:
    print(report.generate())
