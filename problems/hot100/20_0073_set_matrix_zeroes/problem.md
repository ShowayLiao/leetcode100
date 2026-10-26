# LeetCode Hot 100 20 - 矩阵置零

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/)
- 难度：中等
- 标签：矩阵、标记
- 本地模式：ACM 标准输入输出

## 题目摘要

将原矩阵中零所在的整行和整列置零。本次修改产生的零不继续触发置零。要求原地修改，进阶目标 O(1) 算法额外空间。

## 输入描述

第一行输入 m 和 n；接下来 m 行每行 n 个整数。

## 输出描述

输出修改后的 m 行矩阵，同行元素用单个空格分隔。

## 数据范围

1 <= m, n <= 200；-2^31 <= matrix[i][j] <= 2^31-1。

## 样例

输入：

```text
3 3
1 1 1
1 0 1
1 1 1
```

输出：

```text
1 0 1
0 0 0
1 0 1
```

## 本地测试

- `tests/01.in` / `tests/01.out`：中间零、不连锁置零。
- `tests/02.in` / `tests/02.out`：单个零。
- `tests/03.in` / `tests/03.out`：单个非零。
- `tests/04.in` / `tests/04.out`：单行。
- `tests/05.in` / `tests/05.out`：单列。
- `tests/06.in` / `tests/06.out`：首行首列零。
- `tests/07.in` / `tests/07.out`：多个零、非方阵、整数边界。
- `tests/08.in` / `tests/08.out`：最大矩阵、全部零。
