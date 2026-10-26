# LeetCode Hot 100 19 - 旋转图像

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 48. 旋转图像](https://leetcode.cn/problems/rotate-image/)
- 难度：中等
- 标签：矩阵、模拟
- 本地模式：ACM 标准输入输出

## 题目摘要

将方阵顺时针旋转 90 度。要求在原矩阵上修改，不创建另一份同等大小的矩阵。

## 输入描述

第一行输入阶数 n；接下来 n 行每行 n 个整数。

## 输出描述

输出旋转后的 n 行矩阵，同行元素用单个空格分隔。

## 数据范围

1 <= n <= 20；-1000 <= matrix[i][j] <= 1000；目标算法额外空间 O(1)。

## 样例

输入：

```text
3
1 2 3
4 5 6
7 8 9
```

输出：

```text
7 4 1
8 5 2
9 6 3
```

## 本地测试

- `tests/01.in` / `tests/01.out`：奇数阶方阵。
- `tests/02.in` / `tests/02.out`：单元素及最小值。
- `tests/03.in` / `tests/03.out`：偶数阶方阵。
- `tests/04.in` / `tests/04.out`：负数及零。
- `tests/05.in` / `tests/05.out`：重复值。
- `tests/06.in` / `tests/06.out`：对角矩阵。
- `tests/07.in` / `tests/07.out`：数值上下界。
- `tests/08.in` / `tests/08.out`：最大阶数。
