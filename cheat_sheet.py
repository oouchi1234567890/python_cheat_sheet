"""■　■　■　文字列　■　■　■"""

"""検索・分割・置換"""
s = " Python,チートシート,検索・分割・置換"
text = s.strip()  # 前後のブランクの削除
starts_with_python = text.startswith("Python")  # 接頭辞を判定
ends_with_intro = text.endswith("チートシート")  # 接尾辞を判定
contains_python = "Python" in text  # 部分文字列を判定
parts = text.split(",")  # 区切ってリスト化
joined = " / ".join(parts)  # 文字列を連結
replaced = text.replace("チートシート", "作成")  # 文字の置換　前が置換前、後が置換後
found_index = text.find("Py")  # 無ければ -1
without_prefix = text.removeprefix("Python,")  # 接頭辞があれば除去
head, sep, tail = text.partition(",")
# 文字列は変更不可（immutable）。各メソッドは原則として 新しい文字列
# を返す。大文字小文字を無視した比較には casefold()


"""f-string 書式指定"""
name, price, rate = "本", 123456, 0.075
f"{name}: {price:,}円"  # 本: 123,456円
f"{rate:.1%}"  # 7.5%
f"{price:>10}"  # 右寄せ
f"{price:0>10}"  # 0埋め
f"{name!r}"  # repr() 表現　シングルクォートで囲まれる
f"{price=}"  # 変数名付き（デバッグ向け）
raw = r"C:\new\test"
"""等を展開しないraw文字列"""
data = text.encode("utf-8")  # 文字列からバイト列へ
back = data.decode("utf-8")  # バイト列から文字列へ


"""内包表記｜短く変換・抽出"""
squares = [x * x for x in range(6) if x % 2 == 0]
lookup = {x: x * x for x in range(3)}
names = ["Alice", "Bob", "Charlie", "alice", "alice"]
unique = {s.lower() for s in names}
# 小文字に変換しての集合なので重複なし、順番は担保されない
names_list = [s + "さん" for s in names]
# 各名前の後に "さん" を付けてリスト化
# print(*names_list, sep=", ")  # Aliceさん, Bobさん, Charlieさん, aliceさん
nums = [1, 2]
opts = {"flag": True}
num_list = [*nums]  # 　イテラブル（リスト・タプルなど）を展開
num_dict = {**opts}  # 辞書をキーワード引数として展開
"""展開して、list とdict をキーワード引数として渡る"""


"""■　■　■　データ構造　■　■　■"""

"""list|リスト順序あり・変更可能"""
names = ["Alice", "Bob", "Charlie", "alice"]
first_names = names[0]  # "Alice" / first_names[-1] は末尾
names[1:3]  # スライス ["Bob", "Charlie"] [開始:終了:間隔]
names.append("David")
names.extend(["Eve", "Frank"])  # 末尾に追加
names.insert(1, "Grace")
names.remove("Charlie")  # 値を指定して削除
last = names.pop()  # 末尾を取得して削除
del names[0]  # 指定のインデックスを削除
names.sort(reverse=True)  # 降順にソート
"""sort() は元のリストを変更して None を返す"""
names.reverse()  # リストを反転
judge_name = "David" in names  # リストに "David" が含まれるか
len(names)  # リストの長さ
names_count = names.count("Alice")  # リストに "Alice" がいくつ含まれるか
names_index = names.index("David")  # リストで "David" が最初に現れるindex

"""tuple タプル｜順序あり・変更不可イミュータブル"""
point = (10, 20)  # 1要素なら (10,)
x, y = point  # アンパック
x, y = y, x  # 変数の入れ替え

"""set 集合｜重複なし・集合演算"""
a, b = {1, 2, 3}, {3, 4}  # 空集合は set()
judge = a | b  # 和集合 a & b # 積集合
judge = a - b  # 差集合
judge = a ^ b  # 対称差
a.add(5)  # 要素の追加
a.discard(9)  # 要素の削除（存在しなくてもエラーにならない）
a.clear()  # 全要素の削除

"""dict 辞書｜キー → 値"""
user = {"name": "Mika", "age": 20}
judge = user["name"]  # 無いキーは KeyError
judge = user.get("city", "Tokyo")  # 無ければ既定値
user["age"] = 21  # 追加、"age" が存在していれば、値を上書き
user.update(active=True)  # 複数のキーと値をまとめて追加・更新
user.update({"active": True})  # 上と同じ、辞書に新しいキーと値をまとめて追加
user["active"] = True  # 上と同じ、辞書に新しいキーと値をまとめて追加
keys = user.keys()  # コロンの左側のキーを取得
values = user.values()  # コロンの右側の値を取得
items = user.items()  # キーと値のペアを取得、ほぼタプルで取得（dict_items）
for k, v in user.items():  # キーと値を同時に取得する場合は items() を使う
    pass  # 処理なし
    # print(k, v)
age = user.pop("age")  # 指定のキーと値を削除して値を返す、無ければ KeyError
judge = "name" in user


"""■　■　■　組み込み関数　■　■　■"""
""" 
len(x) type(x) isinstance(x, T) issubclass(A, B)
str(x) int(x) float(x) bool(x) list(it) tuple(it)
dict(it) set(it) min(it) max(it) sum(it) abs(x)
sorted(it, key=..., reverse=True) reversed(seq)
range(start, stop, step) enumerate(it, start=0)
zip(a, b) map(fn, it) filter(fn, it)
any(it) all(it) callable(x) hash(x)
getattr(obj, "name", default) setattr(obj, "name", v)
print(*values, sep=" ", end="\n") input(prompt)
定番: インデックス付き反復は enumerate、複数列は zip、
存在判定はany、全件判定は all。
"""

"""■　■　■　　関数　　■　■　■"""


def greeting(name: str, prefix: str = "Hi") -> str:
    """挨拶文を返す。strの初期値として prefix を指定"""
    return f"{prefix}, {name}!"


greeting("Aoi")  # 位置引数
greeting(name="Aoi", prefix="Hello")  # キーワード引数

"""引数の並びと展開"""


def f(pos_only, /, normal=0, *args, flag=False, **kwargs):
    return pos_only, normal, args, flag, kwargs


"""
# pos_only
# → 位置で渡す引数
# /
# → ここより前は「位置引数のみ」
# normal=0
# → 通常の引数、デフォルト値0
# *args
# → 複数の位置引数をタプルで受け取る
# flag=False
# → キーワード専用引数のデフォルト値
# **kwargs
# → 複数のキーワード引数を辞書で受け取る
"""

"""変更可能な値をデフォルト値にすると、呼び出し間で共有される。"""


def bad_default(x=[]):
    x.append(1)
    return x


"""安全な変更可能な値を共有しない書き方:"""


def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


"""lambda・高階関数・スコープ"""
"""lambda 引数: 式 名前を持たない短い関数を定義するための式。"""

double = lambda x: x * 2
print(double(5))  # 10

"""以下と同じ"""


def double(x):
    return x * 2


"""高階関数とは、関数を引数として受け取ったり、関数を戻り値として返したりする関数"""
rows = [
    {"score": 80},
    {"score": 90},
    {"score": 70},
]
key = lambda row: row["score"]
result = sorted(rows, key=key, reverse=True)
# print(result)


def counter():
    n = 0

    def inc():
        # 外側の関数の変数を参照するには nonlocal 宣言が必要
        nonlocal n  # inc() の外側にある n を使う
        n += 1
        return n

    return inc


c = counter()
# print(c())  # 1
# print(c())  # 2

"""■　■　■　　クラス / インスタンス　　■　■　■"""


class User:
    species = "human"  # クラス属性

    def __init__(self, name: str):
        # __init__ はコンストラクタ、インスタンス生成時に呼ばれる
        self.name = name  # インスタンス属性

    def greet(self) -> str:
        return f"Hi, {self.name}"


u = User("Aoi")
user_name = u.name
u.greet()
user_instance = isinstance(u, User)

"""継承・super・property"""


class Admin(User):
    # User クラスを継承java の extends と同じ

    def __init__(self, name, level=1):  # コンストラクタと同じ
        super().__init__(name)  # 親クラスのコンストラクタを呼ぶsuper().
        self._level = level  # 隠蔽は_で名前を変える

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 1:
            raise ValueError("level >= 1")
            # raiseで例外を発生　javaのthrowと同じ
        self._level = value

    @level.deleter
    def level(self):
        del self._level


"""デコレータ・デコレータの引数・クラスデコレーター"""
"""デコレータは関数を引数に取り、機能を追加した関数を返す関数"""
"""@decorator_name と書くことで、関数を装飾"""
from functools import wraps


def repeat(count):
    def decorator(func):
        @wraps(func)  # @wraps(func)は、元の関数名や説明文などの情報を保持
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(count):  # _は、ループ変数を使わない場合の名前
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)  # repeatに渡される引数は count で、3回繰り返す
def greet(name):
    print(f"こんにちは、{name}さん")


greet("Alice")
