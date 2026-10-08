# Python ACM 输入输出

## 选择方式

- 输入短、格式简单：使用 `input()`，可读性最好。
- 数据量较大或希望一次解析：使用 `sys.stdin.buffer.read().split()`。
- 以行作为独立测试组：遍历 `sys.stdin.buffer`。
- 输出很多行：先收集字符串，最后使用 `"\n".join(...)` 一次输出。

## 一次读取全部整数

```python
import sys

data = sys.stdin.buffer.read().split()
values = list(map(int, data))
```

## 单组数组

输入：

```text
5
1 2 3 4 5
```

解析：

```python
n = int(input())
numbers = list(map(int, input().split()))
assert len(numbers) == n
```

## 首行给出测试组数

```python
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    # 求解当前测试组。
```

## 读取到 EOF

```python
import sys

for line in sys.stdin.buffer:
    if not line.strip():
        continue
    numbers = list(map(int, line.split()))
    # 求解当前行。
```

## 矩阵

```python
rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
```

当每行一定有 `columns` 个元素时可以直接按行读取；输入可能跨行时，改用 token 迭代器。

## 图

```python
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)
```

根据题意确认节点是零基还是一基、图是有向还是无向、边是否带权。

## 输出注意事项

- 标准输出只打印答案，不打印提示语或调试信息。
- 数组通常使用 `print(*answer)`。
- 多行结果可以使用 `print("\n".join(lines))`。
- 本仓库测试工具只忽略文件末尾的换行，不忽略其他空格差异。

