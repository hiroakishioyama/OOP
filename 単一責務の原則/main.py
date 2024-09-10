class User:
    """
    ユーザー情報を管理するクラス。
    単一責務の原則に従い、ユーザー情報の保持と表示のみを行います。
    """

    def __init__(self, name, email):
        """
        初期化メソッド。
        :param name: ユーザーの名前
        :param email: ユーザーのメールアドレス
        """
        self.name = name
        self.email = email

    def print_user(self):
        """
        ユーザー情報を出力します。
        """
        print(f"Name: {self.name}, Email: {self.email}")

# 使用例
user = User("山田太郎", "yamada@example.com")
user.print_user()
