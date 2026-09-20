"""■　■　■　文字列　■　■　■"""

"""検索・分割・置換"""
s = " Python,チートシート,検索・分割・置換"

# 前後のブランクの削除
text = s.strip()

# 接頭辞を判定
starts_with_python = text.startswith("Python")

# 接尾辞を判定
ends_with_intro = text.endswith("チートシート")

# 部分文字列を判定
contains_python = "Python" in text

# 区切ってリスト化
parts = text.split(",")

# 文字列を連結
joined = " / ".join(parts)

# 文字の置換　前が置換前、後が置換後
replaced = text.replace("チートシート", "作成")

# 無ければ -1
found_index = text.find("Py")

# 接頭辞があれば除去
without_prefix = text.removeprefix("Python,")

head, sep, tail = text.partition(",")

# 文字列は変更不可（immutable）。各メソッドは原則として 新しい文字列
# を返す。大文字小文字を無視した比較には casefold()


"""f-string 書式指定"""

name, price, rate = "本", 123456, 0.075

# 本: 123,456円
f"{name}: {price:,}円"

# 7.5%
f"{rate:.1%}"

# 右寄せ
f"{price:>10}"

# 0埋め
f"{price:0>10}"

# repr() 表現　シングルクォートで囲まれる
f"{name!r}"

# 変数名付き（デバッグ向け）
f"{price=}"

raw = r"C:\new\test"
"""等を展開しないraw文字列"""

# 文字列からバイト列へ
data = text.encode("utf-8")

# バイト列から文字列へ
back = data.decode("utf-8")


"""内包表記｜短く変換・抽出"""
squares = [x * x for x in range(6) if x % 2 == 0]
lookup = {x: x * x for x in range(3)}
names = ["Alice", "Bob", "Charlie", "alice", "alice"]
unique = {s.lower() for s in names}

# 小文字に変換しての集合なので重複なし、順番は担保されない
names_list = [s + "さん" for s in names]

# 各名前の後に "さん" を付けてリスト化
# Aliceさん, Bobさん, Charlieさん, aliceさん
# print(*names_list, sep=", ")
nums = [1, 2]

opts = {"flag": True}

# 　イテラブル（リスト・タプルなど）を展開
num_list = [*nums]

# 辞書をキーワード引数として展開
num_dict = {**opts}

"""展開して、list とdict をキーワード引数として渡る"""


"""■　■　■　データ構造　■　■　■"""

"""list|リスト順序あり・変更可能"""
names = ["Alice", "Bob", "Charlie", "alice"]

# "Alice" / first_names[-1] は末尾
first_names = names[0]

# スライス ["Bob", "Charlie"] [開始:終了:間隔]
names[1:3]

names.append("David")

# 末尾に追加
names.extend(["Eve", "Frank"])

names.insert(1, "Grace")

# 値を指定して削除
names.remove("Charlie")

# 末尾を取得して削除
last = names.pop()

# 指定のインデックスを削除
del names[0]

# 降順にソート
names.sort(reverse=True)

"""sort() は元のリストを変更して None を返す"""

# リストを反転
names.reverse()

# リストに "David" が含まれるか
judge_name = "David" in names

# リストの長さ
len(names)

# リストに "Alice" がいくつ含まれるか
names_count = names.count("Alice")

# リストで "David" が最初に現れるindex
names_index = names.index("David")

"""tuple タプル｜順序あり・変更不可イミュータブル"""

# 1要素なら (10,)
point = (10, 20)

# アンパック
x, y = point

# 変数の入れ替え
x, y = y, x

"""set 集合｜重複なし・集合演算"""

# 空集合は set()
a, b = {1, 2, 3}, {3, 4}

# 和集合 a & b # 積集合
judge = a | b

# 差集合
judge = a - b

# 対称差
judge = a ^ b

# 要素の追加
a.add(5)

# 要素の削除（存在しなくてもエラーにならない）
a.discard(9)

# 全要素の削除
a.clear()

"""dict 辞書｜キー → 値"""
user = {"name": "Mika", "age": 20}

# 無いキーは KeyError
judge = user["name"]

# 無ければ既定値
judge = user.get("city", "Tokyo")

# 追加、"age" が存在していれば、値を上書き
user["age"] = 21

# 複数のキーと値をまとめて追加・更新
user.update(active=True)

# 上と同じ、辞書に新しいキーと値をまとめて追加
user.update({"active": True})

# 上と同じ、辞書に新しいキーと値をまとめて追加
user["active"] = True

# コロンの左側のキーを取得
keys = user.keys()

# コロンの右側の値を取得
values = user.values()

# キーと値のペアを取得、ほぼタプルで取得（dict_items）
items = user.items()

# キーと値を同時に取得する場合は items() を使う
for k, v in user.items():

    # 処理なし
    pass

    # print(k, v)
# 指定のキーと値を削除して値を返す、無ければ KeyError
age = user.pop("age")

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

"""■　■　■　数値の計算と丸め　■　■　■"""

"""最大値・最小値"""
numbers = [2, 4, 4, 4, 5, 5, 7, 9]

# 9: 最大値
max(numbers)

# 2: 最小値
min(numbers)

# 8: 複数の引数でも指定できる
max(3, 8, 1)

# None: 空の場合の既定値
min([], default=None)

"""roundによる銀行家の丸め"""

# 2
round(2.5)

# 4
round(3.5)

# -2
round(-2.5)

# 0.12: 小数第2位まで残す
round(0.125, 2)

# 0.38
round(0.375, 2)

# 1200: 百の位に丸める
round(1234, -2)

# 2.67: floatの表現誤差に注意
round(2.675, 2)

"""decimalによる四捨五入日本で一般的な方式"""
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

# Decimal('3')
Decimal("2.5").quantize(Decimal(1), rounding=ROUND_HALF_UP)

# Decimal('-3')
Decimal("-2.5").quantize(Decimal(1), rounding=ROUND_HALF_UP)

# Decimal('2.68')
Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# Decimal('1.3E+3')
Decimal(1250).quantize(Decimal("1E2"), rounding=ROUND_HALF_UP)

# Decimal('2')
Decimal("2.5").quantize(Decimal(1), rounding=ROUND_HALF_EVEN)

"""平均・標準偏差"""
import statistics

numbers = [2, 4, 4, 4, 5, 5, 7, 9]

# 5: 算術平均
statistics.mean(numbers)

# 5.0: floatで返す算術平均
statistics.fmean(numbers)

# 2.0: 母標準偏差（分母はn）
statistics.pstdev(numbers)

# 2.138089935299395: 標本標準偏差（分母はn - 1）
statistics.stdev(numbers)

# Decimalは文字列から作る。百の位への丸めはDecimal("1E2")を指定する。
# mean/fmean/pstdevは1個以上、stdevは2個以上必要。不足時はStatisticsError。


"""■　■　■　　関数　　■　■　■"""


def greeting(name: str, prefix: str = "Hi") -> str:
    """挨拶文を返す。strの初期値として prefix を指定"""
    return f"{prefix}, {name}!"


# 位置引数
greeting("Aoi")

# キーワード引数
greeting(name="Aoi", prefix="Hello")

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

# 10が出力される
# print(double(5))

"""以下と同じ"""


# lambdaとdefの等価な書き方を比較するため、ここでは同じ名前を再定義します。
# pylint: disable-next=function-redefined
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
        # inc() の外側にある n を使う
        nonlocal n

        n += 1
        return n

    return inc


c = counter()

# 1
# print(c())
# 2
# print(c())

"""コンストラクタ / インスタンス"""


class User:

    # クラス属性
    species = "human"

    def __init__(self, name: str):

        # __init__ はコンストラクタ、インスタンス生成時に呼ばれる
        # インスタンス属性
        self.name = name

    def greet(self) -> str:
        return f"Hi, {self.name}"


u = User("Aoi")
user_name = u.name
u.greet()
user_instance = isinstance(u, User)

"""継承・super・property"""


class Admin(User):

    # User クラスを継承java の extends と同じ

    # コンストラクタと同じ
    def __init__(self, name, level=1):

        # 親クラスのコンストラクタを呼ぶsuper().
        super().__init__(name)

        # 隠蔽は_で名前を変える
        self._level = level

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

        # @wraps(func)は、元の関数名や説明文などの情報を保持
        @wraps(func)

        def wrapper(*args, **kwargs):
            result = None

            # _は、ループ変数を使わない場合の名前
            for _ in range(count):

                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


# repeatに渡される引数は count で、3回繰り返す
@repeat(3)

def greet(name):

    # print(f"こんにちは、{name}さん")
    # 上のコメントを解除すると3回prinitされる
    pass


greet("Alice")


"""■　■　■モジュール / パッケージ / 名前空間 / スコープ"""
import math

# asで別名を付けることもできる。
import pathlib as pl
from collections import Counter

# from の後はモジュール名、モジュール名はファイル名から.pyを除いたもの。
# collections.Counter は、要素の出現回数を数えるためのクラス。
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = Counter(fruits)

# print(counts)
math.sqrt(9)

pl.Path("data.txt")

"""モジュールと実行"""


# 特定のファイル名を実行する tool.pyだとmain()が実行されるが、
# 他のファイルからimportされた場合は実行されない。
def main():

    # print("run")
    pass


if __name__ == "__main__":

    # python tool.py のときだけ実行
    main()

"""パッケージはモジュールをまとめるディレクトリ。通常は __init__.py
を置く（名前空間パッケージでは省略可能）。相対import例: from
.utils import helper。"""


"""■　■　■　　ファイル操作　　■　■　■"""
from pathlib import Path

"""ファイルの読み書き"""
path = Path("sample.txt")

# ファイルの書き込み
with path.open("w", encoding="utf-8") as f:

    f.write("Hello, World!\n")
    f.write("Python チートシート\n")

# もしくは
path.write_text("Hello, World!\nPython チートシート\n", encoding="utf-8")

# ファイルのクローズ処理は自動で実施

# ファイルの読み込み
with path.open("r", encoding="utf-8") as f:

    content = f.read()

    # print(content)
path.read_text(encoding="utf-8")

# こちらもファイルのクローズ処理は自動で実施

"""json ファイルの読み書き"""

import json

json_path = Path("sample.json")

# JSON の書き込み
data = {"name": "Alice", "age": 30}

with json_path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

    # 引数の説明　ensure_ascii=False: 非ASCII文字をそのまま出力
    # indent=4　 インデントを4スペースにして整形

# JSON の読み込み
with json_path.open("r", encoding="utf-8") as f:

    loaded_data = json.load(f)

    # print(loaded_data)


"""csv ファイルの読み書き"""

import csv
from pathlib import Path

path = Path("rows.csv")

# ファイルがなければ新規作成する
if not path.exists():

    print(f"{path} がないので新規作成")
    path.touch()

with open("rows.csv", "a+", newline="", encoding="utf-8-sig") as f:

    # "a+",を追記しないと、"r"と同じでファイルがない場合はFileNotFoundError:
    # withステートメントを使うことで、ファイルのクローズ処理を自動で実施
    rows = list(csv.DictReader(f))

path = Path("rows.csv")

# CSV の書き込み
with path.open("w", newline="", encoding="utf-8-sig") as f:

    # newline="" 改行コードを変換せず、ファイル内の改行をそのまま書き込む
    writer = csv.DictWriter(f, fieldnames=["name", "age"])

    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
    writer.writerow({"name": "Bob", "age": 25})

"""CSV の読み込み"""
content = path.read_text(encoding="utf-8-sig")
text = content.splitlines()


# CSV ファイルにデータを書き込む
data = [
    ["ID", "Name", "Age", "Height", "Weight"],
    [1, "Taro Yamada", 16, 170, 65],
    [2, "Hanako Sato", 16, 160, 55],
    [3, "Ichiro Suzuki", 17, 175, 68],
    [4, "Misaki Tanaka", 16, 162, 54],
    [5, "Kenta Takahashi", 17, 178, 70],
    [6, "Mao Ito", 16, 165, 57],
    [7, "Yuko Watanabe", 16, 168, 60],
    [8, "Ryo Nakamura", 17, 172, 66],
    [9, "Ai Kobayashi", 16, 158, 52],
    [10, "Daisuke Kato", 16, 176, 69],
]

# 'w'モードで開く
with open("base.csv", "w") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(data)


# 'sample.csv'ファイルにデータを追記
with open(
    "sample.csv",
    "a",
    newline="",
    encoding="utf-8-sig",

    # BOM付のUTF-8で書き込む　先頭にEF BB BF
# 'a'モードで開くappend 追記モード
) as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(
        [
            [11, "Shota Yamaguchi", 17, 180, 75],
            [12, "Emi Kondo", 16, 158, 50],
        ]

    # 新しいデータを追加
    )


"""■　■　■例外処理■　■　■"""

# 独自例外にする場合は、クラスとして定義
# class InputError(ValueError):
# pass


def save(value):

    print(f"保存しました: {value}")


def cleanup():
    print("後始末をしました")


input_text = "123"

try:

    # 例外が発生する可能性がある処理
    value = int(input_text)

except (ValueError, TypeError):

    # 上で指定したエラーが発生した場合の処理
    print(ValueError("整数ではありません"))

    # raise raiseはエラーを投げるjavaのthrow
else:

    # 例外が発生しない場合のみ実施される
    save(value)

finally:

    # 必ず実行される。ファイルのクローズ処理などの共通で行う後始末に使用
    cleanup()

# よく使う例外:
# TypeError 型が不適切
# ValueError 値が不適切
# KeyError# キーなし
# IndexError 範囲外
# FileNotFoundError ファイルなし
# except: は原則避ける。


"""■　■　■正規表現■　■　■"""

import re

# 以下、メールアドレスのサンプル
pattern = re.compile(r"(?P<name>[A-Za-z]+)@([\w.-]+)")

# rはraw文字列を表します。エスケープ文字を処理しにくくしています。
# (?P<name>...) は名前付きグループを定義します。
# name という名前付きグループ
"""以下、正規表現"""

# [A-Za-z]	半角英字の大文字または小文字
# +	直前のパターンが1回以上続く
# @	@ という文字そのもの
# (...)	マッチした部分をグループとして記録
# \w	英数字やアンダースコアなど
# .	[] の中ではピリオドそのもの
# -	[] の末尾ではハイフンそのもの
# [\w.-]	単語文字、ピリオド、ハイフンのいずれか
# [\w.-]+	これらの文字が1回以上続く

m = pattern.search("連絡先: user@example.com")

if m:

    # マッチ全体
    m.group(0)

    # 名前付きグループ
    m.group("name")

# ['12', '34']　一致する文字列をすべて抽出
re.findall(r"\d+", "A12 B34")

# 出力結果は必ず型が文字列となります

# 'a b'
re.sub(r"\s+", " ", "a b")

# 一致した部分を置換え　r"\s+"  は検索する部分　" "半角空白1個に置換
# re.sub() は元の文字列を変更せず、置換後の新しい文字列を返します

# ['a','b','c']
re.split(r"[,;]", "a,b;c")

# 主な記号: . 任意1文字／^ $ 先頭・末尾／* + ? 反復／[abc]
# 文字集合／\d \w \s 数字・単語・空白。パターンはraw文字列推奨。
