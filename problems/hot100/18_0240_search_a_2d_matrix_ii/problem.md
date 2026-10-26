# LeetCode Hot 100 18 - 搜索二维矩阵 II

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)
- 难度：中等
- 标签：矩阵、搜索
- 本地模式：ACM 标准输入输出

## 题目摘要

每行从左到右、每列从上到下均非递减。判断目标是否存在；不保证上一行末尾小于下一行开头。

## 输入描述

第一行输入 m、n 和 target；接下来 m 行每行 n 个整数。

## 输出描述

存在时输出小写 true，否则输出小写 false。

## 数据范围

1 <= m, n <= 300；-10^9 <= matrix[i][j], target <= 10^9；目标搜索时间 O(m+n)，不计读取矩阵。

## 样例

输入：

```text
3 3 5
1 4 7
2 5 8
3 6 9
```

输出：

```text
true
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通命中、行间交错。
- `tests/02.in` / `tests/02.out`：小于最小值。
- `tests/03.in` / `tests/03.out`：单元素命中。
- `tests/04.in` / `tests/04.out`：单元素未命中。
- `tests/05.in` / `tests/05.out`：单行及数值边界。
- `tests/06.in` / `tests/06.out`：单列内部缺失。
- `tests/07.in` / `tests/07.out`：重复值及非方阵。
- `tests/08.in` / `tests/08.out`：最大矩阵、右下角命中。
