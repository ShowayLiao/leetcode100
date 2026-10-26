# LeetCode Hot 100 16 - 轮转数组

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 189. 轮转数组](https://leetcode.cn/problems/rotate-array/)
- 难度：中等
- 标签：数组、双指针
- 本地模式：ACM 标准输入输出

## 题目摘要

将数组向右轮转 k 个位置；每次轮转将末尾元素移到最前。练习目标是在原数组上完成。

## 输入描述

第一行输入 n 和非负整数 k；第二行输入 n 个整数。

## 输出描述

输出轮转后的 n 个整数，用单个空格分隔。

## 数据范围

1 <= n <= 10^5；0 <= k <= 10^5；-2^31 <= nums[i] <= 2^31-1；进阶目标 O(n) 时间、O(1) 算法额外空间。

## 样例

输入：

```text
7 3
1 2 3 4 5 6 7
```

输出：

```text
5 6 7 1 2 3 4
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通右轮转。
- `tests/02.in` / `tests/02.out`：负数混合。
- `tests/03.in` / `tests/03.out`：单元素及最大 k。
- `tests/04.in` / `tests/04.out`：零次轮转。
- `tests/05.in` / `tests/05.out`：整圈轮转。
- `tests/06.in` / `tests/06.out`：k 大于长度。
- `tests/07.in` / `tests/07.out`：重复零及整数边界。
- `tests/08.in` / `tests/08.out`：最大长度。
