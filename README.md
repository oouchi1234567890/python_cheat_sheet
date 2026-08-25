# python_cheat_sheet
# Python チートシート

Pythonでよく使う構文や操作を、用途別にすぐ確認できるようにまとめたチートシートです。
vscodeで作成したものをchatGPTで整理しています。
> [!NOTE]
> コードブロックには `python` を指定しています。VS CodeのMarkdownプレビューでは、使用中のテーマに合わせて構文が色分けされます。

## 目次

- [文字列](#文字列)
  - [検索・分割・置換](#検索分割置換)
  - [f-stringの書式指定](#f-stringの書式指定)
  - [raw文字列と文字コード](#raw文字列と文字コード)
  - [内包表記と展開](#内包表記と展開)
- [データ構造](#データ構造)
  - [リスト](#リスト-list)
  - [タプル](#タプル-tuple)
  - [集合](#集合-set)
  - [辞書](#辞書-dict)
- [組み込み関数](#組み込み関数)
- [関数](#関数)
  - [引数の種類](#引数の種類)
  - [デフォルト引数の注意点](#デフォルト引数の注意点)
  - [lambda・高階関数・スコープ](#lambda高階関数スコープ)
- [クラスとインスタンス](#クラスとインスタンス)
  - [継承・super・property](#継承superproperty)
- [デコレータ](#デコレータ)

---

## 文字列

### 検索・分割・置換

```python
s = " Python,チートシート,検索・分割・置換 "
text = s.strip()                     # 前後の空白を削除

text.startswith("Python")           # 接頭辞を判定: True
text.endswith("置換")                # 接尾辞を判定: True
"Python" in text                    # 部分文字列を判定: True

parts = text.split(",")             # 区切ってリスト化
joined = " / ".join(parts)          # 要素を文字列で連結
replaced = text.replace(
    "チートシート", "作成"
)                                    # 文字列を置換

found_index = text.find("Py")       # 最初の位置。なければ -1
without_prefix = text.removeprefix(
    "Python,"
)                                    # 接頭辞があれば削除

head, sep, tail = text.partition(",")
# 最初の区切り文字を境に、前・区切り文字・後の3要素に分割
```

文字列は変更不可（イミュータブル）です。文字列メソッドは原則として新しい文字列を返します。

大文字・小文字を区別せず比較するときは `casefold()` が便利です。

```python
"Python".casefold() == "PYTHON".casefold()  # True
```

### f-stringの書式指定

```python
name, price, rate = "本", 123456, 0.075

f"{name}: {price:,}円"   # '本: 123,456円'
f"{rate:.1%}"            # '7.5%'
f"{price:>10}"           # 幅10で右寄せ
f"{price:0>10}"          # 幅10で左側を0埋め
f"{name!r}"              # repr()形式: "'本'"
f"{price=}"              # 'price=123456'（デバッグ向け）
```

### raw文字列と文字コード

raw文字列では、バックスラッシュによるエスケープを原則そのまま扱います。

```python
path = r"C:\new\test"

data = "Python".encode("utf-8")  # 文字列からバイト列へ
text = data.decode("utf-8")       # バイト列から文字列へ
```

### 内包表記と展開

```python
# リスト内包表記: 偶数だけを抽出して2乗
squares = [x * x for x in range(6) if x % 2 == 0]
# [0, 4, 16]

# 辞書内包表記
lookup = {x: x * x for x in range(3)}
# {0: 0, 1: 1, 2: 4}

# 集合内包表記: 重複なし・順序の保証なし
names = ["Alice", "Bob", "Charlie", "alice"]
unique = {name.lower() for name in names}
# {'alice', 'bob', 'charlie'} ※表示順は一定ではない

names_list = [name + "さん" for name in names]
print(*names_list, sep=", ")
# Aliceさん, Bobさん, Charlieさん, aliceさん
```

`*` はイテラブルを、`**` は辞書を展開します。

```python
nums = [1, 2]
more_nums = [0, *nums, 3]           # [0, 1, 2, 3]

options = {"flag": True}
config = {"mode": "fast", **options}
# {'mode': 'fast', 'flag': True}

print(*nums)                         # print(1, 2) と同じ
```

---

## データ構造

| 型 | 順序 | 変更 | 重複 | 主な用途 |
|---|---|---|---|---|
| `list` | あり | 可 | 可 | 順序付きの要素一覧 |
| `tuple` | あり | 不可 | 可 | 変更しない値の組 |
| `set` | 保証なし | 可 | 不可 | 重複除去・集合演算 |
| `dict` | あり | 可 | キーは不可 | キーと値の対応 |

### リスト `list`

順序があり、要素を変更できます。

```python
names = ["Alice", "Bob", "Charlie", "alice"]

first = names[0]                    # 先頭
last = names[-1]                    # 末尾
part = names[1:3]                   # [開始:終了:間隔]

names.append("David")              # 末尾に1要素追加
names.extend(["Eve", "Frank"])     # 末尾に複数要素追加
names.insert(1, "Grace")           # 指定位置に追加

names.remove("Charlie")            # 最初に一致した値を削除
popped = names.pop()                # 末尾を取得して削除
del names[0]                        # 指定位置を削除

names.sort(reverse=True)            # 元のリストを降順に並べ替え
names.reverse()                     # 元のリストを反転

"David" in names                   # 含まれているか
len(names)                          # 要素数
names.count("Alice")               # 値の個数
names.index("David")               # 最初に現れる位置
```

> [!TIP]
> `list.sort()` は元のリストを変更して `None` を返します。元のリストを残す場合は `sorted(names)` を使います。

### タプル `tuple`

順序があり、作成後は要素を変更できません。

```python
point = (10, 20)
single = (10,)                      # 1要素では末尾のカンマが必要

x, y = point                       # アンパック
x, y = y, x                        # 値を入れ替え
```

### 集合 `set`

重複する要素を持たず、集合演算に向いています。

```python
a = {1, 2, 3}
b = {3, 4}
empty = set()                       # {} は空の辞書になるため注意

a | b                              # 和集合: {1, 2, 3, 4}
a & b                              # 積集合: {3}
a - b                              # 差集合: {1, 2}
a ^ b                              # 対称差: {1, 2, 4}

a.add(5)                           # 要素を追加
a.discard(9)                       # 要素を削除。なくてもエラーにならない
a.clear()                          # 全要素を削除
```

### 辞書 `dict`

キーと値の組を保持します。

```python
user = {"name": "Mika", "age": 20}

name = user["name"]                # キーがなければ KeyError
city = user.get("city", "Tokyo")  # なければ既定値

user["age"] = 21                  # 追加または上書き
user["active"] = True
user.update(city="Osaka", active=False)
user.update({"city": "Kyoto"})

keys = user.keys()                  # キーのビュー
values = user.values()              # 値のビュー
items = user.items()                # (キー, 値) のビュー

for key, value in user.items():
    print(key, value)

age = user.pop("age")              # 削除した値を返す
"name" in user                     # キーの存在判定
```

---

## 組み込み関数

| 分類 | 主な関数 |
|---|---|
| 型・判定 | `type(x)`, `isinstance(x, T)`, `issubclass(A, B)`, `callable(x)` |
| 型変換 | `str(x)`, `int(x)`, `float(x)`, `bool(x)`, `list(it)`, `tuple(it)`, `dict(it)`, `set(it)` |
| 集計 | `len(x)`, `min(it)`, `max(it)`, `sum(it)`, `abs(x)` |
| 並べ替え | `sorted(it, key=..., reverse=True)`, `reversed(seq)` |
| 反復 | `range(start, stop, step)`, `enumerate(it, start=0)`, `zip(a, b)` |
| 変換・抽出 | `map(fn, it)`, `filter(fn, it)` |
| 条件判定 | `any(it)`, `all(it)` |
| 属性操作 | `getattr(obj, "name", default)`, `setattr(obj, "name", value)` |
| 入出力 | `print(*values, sep=" ", end="\n")`, `input(prompt)` |

定番の使い分けは次のとおりです。

```python
names = ["Aoi", "Mika"]
scores = [90, 80]

for index, name in enumerate(names, start=1):
    print(index, name)              # 番号付きで反復

for name, score in zip(names, scores):
    print(name, score)              # 複数の列を同時に反復

has_passed = any(score >= 60 for score in scores)
all_passed = all(score >= 60 for score in scores)
```

---

## 関数

```python
def greeting(name: str, prefix: str = "Hi") -> str:
    """挨拶文を返す。"""
    return f"{prefix}, {name}!"


greeting("Aoi")                         # 位置引数
greeting(name="Aoi", prefix="Hello")  # キーワード引数
```

### 引数の種類

```python
def func(pos_only, /, normal=0, *args, flag=False, **kwargs):
    return pos_only, normal, args, flag, kwargs
```

| 記述 | 意味 |
|---|---|
| `pos_only` | 位置で渡す引数 |
| `/` | これより前は位置専用引数 |
| `normal=0` | 位置でもキーワードでも渡せる引数。既定値は `0` |
| `*args` | 追加の位置引数をタプルで受け取る |
| `flag=False` | キーワード専用引数。既定値は `False` |
| `**kwargs` | 追加のキーワード引数を辞書で受け取る |

```python
result = func(1, 2, 3, 4, flag=True, mode="fast")
# (1, 2, (3, 4), True, {'mode': 'fast'})
```

### デフォルト引数の注意点

リストや辞書などの変更可能な値をデフォルト引数にすると、その値が呼び出し間で共有されます。

```python
# 非推奨
def bad_default(items=[]):
    items.append(1)
    return items
```

共有したくない場合は `None` を使います。

```python
def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

### lambda・高階関数・スコープ

`lambda` は、名前を持たない短い関数を作る式です。

```python
double = lambda x: x * 2
double(5)                           # 10

# 上記は次の関数と同じ動作
def double(x):
    return x * 2
```

関数を引数に取る、または関数を返す関数を高階関数と呼びます。

```python
rows = [
    {"score": 80},
    {"score": 90},
    {"score": 70},
]

result = sorted(
    rows,
    key=lambda row: row["score"],
    reverse=True,
)
# [{'score': 90}, {'score': 80}, {'score': 70}]
```

内側の関数から外側の関数の変数を書き換えるには `nonlocal` を使います。

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()
c()                                 # 1
c()                                 # 2
```

---

## クラスとインスタンス

```python
class User:
    species = "human"               # クラス属性

    def __init__(self, name: str):
        self.name = name             # インスタンス属性

    def greet(self) -> str:
        return f"Hi, {self.name}"


user = User("Aoi")                 # インスタンスを生成
user.name                           # 'Aoi'
user.greet()                        # 'Hi, Aoi'
isinstance(user, User)              # True
```

### 継承・`super()`・`property`

```python
class Admin(User):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name)       # 親クラスの初期化処理を呼ぶ
        self._level = level

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        if value < 1:
            raise ValueError("level must be at least 1")
        self._level = value

    @level.deleter
    def level(self) -> None:
        del self._level


admin = Admin("Aoi", level=2)
admin.level                         # getterを呼ぶ
admin.level = 3                     # setterを呼ぶ
del admin.level                     # deleterを呼ぶ
```

Pythonでは `_name` は「外部から直接触らない」という慣例を表します。Javaなどの `private` のような強制的なアクセス制限ではありません。

---

## デコレータ

デコレータは、既存の関数などを受け取り、機能を加えたオブジェクトを返します。`@デコレータ名` の形式で適用します。

```python
from functools import wraps


def repeat(count):
    def decorator(func):
        @wraps(func)                 # 元の関数名やdocstringを保持
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(count):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"こんにちは、{name}さん")


greet("Alice")                      # 挨拶を3回表示
```

`@repeat(3)` は、おおむね次の代入と同じ意味です。

```python
greet = repeat(3)(greet)
```

---

## 関連ファイル

- 元のPythonファイル: [`cheat_sheet.py`](./cheat_sheet.py)
