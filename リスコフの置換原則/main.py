class Bird:
    """
    鳥類を表す基底クラス。すべての鳥は飛ぶことが期待されます。
    """

    def fly(self):
        """
        鳥が飛ぶ動作をシミュレートします。
        """
        print("This bird is flying.")

class Sparrow(Bird):
    """
    スズメクラス。鳥類の一種で、飛ぶことができます。
    """

    def fly(self):
        """
        スズメが飛ぶ動作をシミュレートします。
        """
        print("Sparrow flying high.")

class Ostrich(Bird):
    """
    ダチョウクラス。実際には飛べないため、この原則に反する例です。
    """

    def fly(self):
        """
        ダチョウは飛べないため、例外を投げます。
        """
        raise Exception("Ostriches cannot fly.")

def let_bird_fly(bird):
    """
    鳥が飛ぶことを試みる関数。リスコフ置換原則に従って、
    この関数に渡されるどの鳥も飛ぶことができることが期待されます。
    """
    bird.fly()

# 使用例
sparrow = Sparrow()
let_bird_fly(sparrow)  # 正常に動作します。

ostrich = Ostrich()
let_bird_fly(ostrich)  # 例外が発生し、LSPに反する。
