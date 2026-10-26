# LeetCode Hot 100 14 - 最大子数组和

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)
- 难度：中等
- 标签：数组、动态规划
- 本地模式：ACM 标准输入输出

## 题目摘要

选取一个非空的连续子数组，输出其元素和的最大值。全负数组也必须选至少一个元素。

## 输入描述

第一行输入数组长度 n；第二行输入 n 个整数。

## 输出描述

输出最大连续子数组和。

## 数据范围

1 <= n <= 10^5；-10^4 <= nums[i] <= 10^4；目标时间 O(n)。

## 样例

输入：

```text
9
-2 1 -3 4 -1 2 1 -5 4
```

输出：

```text
6
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通混合数组。
- `tests/02.in` / `tests/02.out`：单个负数。
- `tests/03.in` / `tests/03.out`：单个零。
- `tests/04.in` / `tests/04.out`：全部为负。
- `tests/05.in` / `tests/05.out`：全部为正。
- `tests/06.in` / `tests/06.out`：最优在开头。
- `tests/07.in` / `tests/07.out`：最优在末尾。
- `tests/08.in` / `tests/08.out`：最大长度及最大元素。
