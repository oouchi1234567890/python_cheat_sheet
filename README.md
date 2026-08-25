# Python チートシート

Pythonでよく使う構文や操作を、用途別にすぐ確認できるようにまとめたチートシートです。

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
- [ファイル操作](#ファイル操作)
  - [テキストファイル](#テキストファイル)
  - [JSONファイル](#jsonファイル)
  - [CSVファイル](#csvファイル)
  - [ファイルモード](#ファイルモード)
- [例外処理](#例外処理)
  - [独自例外](#独自例外)
  - [主な例外](#主な例外)
- [正規表現](#正規表現)
  - [検索とグループ](#検索とグループ)
  - [抽出・置換・分割](#抽出置換分割)

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

## ファイル操作

`pathlib.Path` を使うと、ファイルパスの作成、存在確認、読み書きをまとめて扱えます。

```python
from pathlib import Path

path = Path("sample.txt")
```

`"sample.txt"` のような相対パスは、Pythonを実行したときのカレントディレクトリを基準にします。スクリプトと同じフォルダを基準にする場合は、次のようにします。

```python
path = Path(__file__).parent / "sample.txt"
```

### テキストファイル

`with` ブロックを抜けるとファイルは自動的に閉じられます。

```python
from pathlib import Path

path = Path("sample.txt")

# 書き込み。既存の内容は上書きされる
with path.open("w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Python チートシート\n")

# ファイル全体を一度に書く場合
path.write_text(
    "Hello, World!\nPython チートシート\n",
    encoding="utf-8",
)

# 読み込み
with path.open("r", encoding="utf-8") as f:
    content = f.read()

# ファイル全体を一度に読む場合
content = path.read_text(encoding="utf-8")
```

ファイルが存在しない場合だけ空のファイルを作成するには、`touch()` を使います。

```python
path = Path("rows.csv")

if not path.exists():
    print(f"{path} がないので新規作成")
    path.touch()
```

より短く書く場合、`exist_ok=True` を指定すると、既存のファイルがあってもエラーになりません。

```python
path.touch(exist_ok=True)
```

### JSONファイル

`json.dump()` はPythonの辞書などをJSONファイルへ書き込み、`json.load()` はJSONファイルからPythonのデータを読み込みます。

```python
import json
from pathlib import Path

json_path = Path("sample.json")
data = {"name": "Alice", "age": 30}

# JSONの書き込み
with json_path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# JSONの読み込み
with json_path.open("r", encoding="utf-8") as f:
    loaded_data = json.load(f)
```

- `ensure_ascii=False`: 日本語などの非ASCII文字をそのまま保存する
- `indent=4`: 4個の空白でインデントして読みやすく整形する

### CSVファイル

CSVは、カンマや引用符、セル内の改行を正しく扱うために `csv` モジュールで読み書きします。

#### 辞書形式で書き込む

```python
import csv
from pathlib import Path

path = Path("rows.csv")

with path.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
    writer.writerow({"name": "Bob", "age": 25})
```

#### 辞書形式で読み込む

```python
with path.open("r", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    print(row)
```

読み込んだ値は、基本的に文字列になります。

```python
{"name": "Alice", "age": "30"}
{"name": "Bob", "age": "25"}
```

#### 複数行を書き込む

`writerows()` は、リストなどに格納した複数行をまとめて書き込みます。

```python
data = [
    ["ID", "Name", "Age"],
    [1, "Taro Yamada", 16],
    [2, "Hanako Sato", 16],
]

with open("base.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
```

#### ファイルの末尾に追記する

`"a"` はappend（追記）モードです。ファイルがあれば末尾へ追加し、なければ新しく作成します。

```python
new_data = [
    [11, "Shota Yamaguchi", 17],
    [12, "Emi Kondo", 16],
]

with open(
    "sample.csv",
    "a",
    newline="",
    encoding="utf-8-sig",
) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_data)
```

`"a+"` では追記と読み込みの両方ができます。ただし、開いた直後のファイル位置は末尾なので、読み込む前に `seek(0)` で先頭へ戻します。

```python
with open(
    "rows.csv",
    "a+",
    newline="",
    encoding="utf-8-sig",
) as f:
    f.seek(0)
    rows = list(csv.DictReader(f))
```

#### CSVで使うオプション

- `newline=""`: Python側で改行を変換せず、改行の処理を `csv` モジュールに任せる
- `encoding="utf-8-sig"`: UTF-8のBOMを扱う。Windows版Excelで文字コードを判別しやすくなる
- `utf-8-sig` の `sig`: signature（目印）の意味

`read_text()` と `splitlines()` でも行ごとの文字列にはできますが、CSVとして解析しているわけではありません。引用符で囲まれたセル内に改行がある場合などは `csv.reader()` または `csv.DictReader()` を使います。

```python
content = path.read_text(encoding="utf-8-sig")
text = content.splitlines()
```

### ファイルモード

| モード | 操作 | ファイルがある場合 | ファイルがない場合 |
|---|---|---|---|
| `"r"` | 読み込み | 読み込む | `FileNotFoundError` |
| `"w"` | 書き込み | 内容を消して上書き | 新規作成 |
| `"a"` | 追記 | 末尾へ追加 | 新規作成 |
| `"x"` | 新規作成 | `FileExistsError` | 新規作成 |
| `"a+"` | 読み込み・追記 | 末尾から開始 | 新規作成 |

---

## 例外処理

例外処理を使うと、実行中に問題が起きた場合の処理を記述できます。

```python
def save(value):
    print(f"保存しました: {value}")


def cleanup():
    print("後始末をしました")


input_text = "123"

try:
    # 例外が発生する可能性がある処理
    value = int(input_text)
except (ValueError, TypeError):
    # 指定した例外が発生した場合
    print("整数ではありません")
else:
    # 例外が発生しなかった場合だけ実行
    save(value)
finally:
    # 例外の有無に関係なく最後に必ず実行
    cleanup()
```

実行結果：

```text
保存しました: 123
後始末をしました
```

各ブロックの役割は次のとおりです。

| キーワード | 役割 |
|---|---|
| `try` | 例外が発生する可能性がある処理を書く |
| `except` | 指定した例外が発生したときの処理を書く |
| `else` | 例外が発生しなかったときだけ実行する |
| `finally` | 例外の有無に関係なく、最後に必ず実行する |

複数種類の例外を同じ処理で受け取る場合は、例外クラスをタプルで指定します。

```python
except (ValueError, TypeError) as error:
    print(f"エラー: {error}")
```

例外名を省略した `except:` は、プログラム終了などに関係する例外まで捕捉するため、原則として避けます。

### 独自例外

用途に合わせた独自例外は、既存の例外クラスを継承して定義します。

```python
class InputError(ValueError):
    """入力値が不正な場合の例外。"""


input_text = "abc"

try:
    value = int(input_text)
except ValueError as error:
    raise InputError("整数が必要です") from error
```

`raise` は例外を発生させます。`from error` を付けると、原因となった元の例外を残せます。

### 主な例外

| 例外 | 主な発生原因 |
|---|---|
| `TypeError` | 型が不適切 |
| `ValueError` | 型は正しいが値が不適切 |
| `KeyError` | 辞書に指定したキーがない |
| `IndexError` | リストなどの範囲外を指定した |
| `FileNotFoundError` | 指定したファイルがない |

---

## 正規表現

`re` モジュールを使うと、文字列の検索、抽出、置換、分割をパターンで指定できます。正規表現ではバックスラッシュを多用するため、通常はraw文字列 `r"..."` を使います。

```python
import re
```

### 検索とグループ

```python
pattern = re.compile(r"(?P<name>[A-Za-z]+)@([\w.-]+)")
m = pattern.search("連絡先: user@example.com")

if m:
    print(m.group(0))       # user@example.com
    print(m.group("name"))  # user
    print(m.group(2))       # example.com
```

`re.compile()` は正規表現を再利用できるパターンオブジェクトに変換します。`search()` は対象文字列から最初に一致する場所を探し、見つからなければ `None` を返します。

パターンの構成：

| パターン | 意味 |
|---|---|
| `(?P<name>...)` | `name` という名前付きグループ |
| `[A-Za-z]` | 半角英字の大文字または小文字 |
| `+` | 直前のパターンが1回以上続く |
| `@` | `@` そのもの |
| `(...)` | 一致した部分をグループとして記録 |
| `\w` | 英数字やアンダースコアなど |
| `[\w.-]+` | 単語文字、ピリオド、ハイフンが1回以上続く |

`group(0)` は一致した全体、`group(1)` 以降は各グループを返します。名前付きグループは `group("name")` でも取得できます。

> [!NOTE]
> このパターンは学習用の簡易例であり、正式なメールアドレスのすべての形式を検証するものではありません。

### 抽出・置換・分割

#### 一致する文字列をすべて抽出する

```python
numbers = re.findall(r"\d+", "A12 B34")
print(numbers)  # ['12', '34']
```

`\d` は数字、`+` は1回以上の繰り返しです。`findall()` の結果は文字列のリストなので、整数が必要なら変換します。

```python
numbers = [int(value) for value in numbers]
print(numbers)  # [12, 34]
```

#### 一致した部分を置換する

```python
result = re.sub(r"\s+", " ", "a    b")
print(result)  # a b
```

`\s+` は連続する1個以上の空白文字です。`re.sub()` は元の文字列を変更せず、置換後の新しい文字列を返します。

#### 複数種類の区切り文字で分割する

```python
parts = re.split(r"[,;]", "a,b;c")
print(parts)  # ['a', 'b', 'c']
```

`[,;]` は「カンマまたはセミコロン」を表します。

主な正規表現記号：

| 記号 | 意味 |
|---|---|
| `.` | 改行以外の任意の1文字 |
| `^` / `$` | 文字列の先頭／末尾 |
| `*` | 直前のパターンが0回以上 |
| `+` | 直前のパターンが1回以上 |
| `?` | 直前のパターンが0回または1回 |
| `[abc]` | `a`、`b`、`c` のいずれか1文字 |
| `\d` / `\w` / `\s` | 数字／単語文字／空白文字 |

---

## 関連ファイル

- 元のPythonファイル: [`cheat_sheet.py`](./cheat_sheet.py)
