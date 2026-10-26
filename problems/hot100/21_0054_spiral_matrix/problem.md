# LeetCode Hot 100 21 - 螺旋矩阵

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)
- 难度：中等
- 标签：矩阵、模拟
- 本地模式：ACM 标准输入输出

## 题目摘要

从左上角开始，按向右、向下、向左、向上的方向沿边界顺时针遍历，逐层向内，每个元素恰好访问一次。

## 输入描述

第一行输入 m 和 n；接下来 m 行每行 n 个整数。

## 输出描述

在一行中输出顺时针螺旋顺序的全部 m*n 个元素，用单个空格分隔。

## 数据范围

1 <= m, n <= 10；-100 <= matrix[i][j] <= 100。

## 样例

输入：

```text
3 3
1 2 3
4 5 6
7 8 9
```

输出：

```text
1 2 3 6 9 8 7 4 5
```

## 本地测试

- `tests/01.in` / `tests/01.out`：奇数方阵及中心。
- `tests/02.in` / `tests/02.out`：非方阵。
- `tests/03.in` / `tests/03.out`：单元素及最小值。
- `tests/04.in` / `tests/04.out`：单行及最大值。
- `tests/05.in` / `tests/05.out`：单列。
- `tests/06.in` / `tests/06.out`：偶数方阵。
- `tests/07.in` / `tests/07.out`：重复值、窄矩阵。
- `tests/08.in` / `tests/08.out`：最大矩阵、多层边界。
