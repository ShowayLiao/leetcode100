# LeetCode Hot 100 17 - 除自身以外数组的乘积

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)
- 难度：中等
- 标签：数组、前缀积、后缀积
- 本地模式：ACM 标准输入输出

## 题目摘要

每个位置输出除自身以外所有元素的乘积。禁止使用除法，要求 O(n) 时间；除输出数组外的额外空间目标为 O(1)。

## 输入描述

第一行输入数组长度 n；第二行输入 n 个整数。

## 输出描述

输出 n 个整数，第 i 个数为除第 i 个元素外的乘积，用单个空格分隔。

## 数据范围

2 <= n <= 10^5；-30 <= nums[i] <= 30；保证每个前缀、后缀及每个答案的乘积均在有符号 32 位整数范围内。

## 样例

输入：

```text
4
1 2 3 4
```

输出：

```text
24 12 8 6
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通正数。
- `tests/02.in` / `tests/02.out`：最小长度。
- `tests/03.in` / `tests/03.out`：单个零。
- `tests/04.in` / `tests/04.out`：多个零。
- `tests/05.in` / `tests/05.out`：全部负数。
- `tests/06.in` / `tests/06.out`：重复的一。
- `tests/07.in` / `tests/07.out`：元素上下界。
- `tests/08.in` / `tests/08.out`：最大长度。
