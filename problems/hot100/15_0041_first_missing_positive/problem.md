# LeetCode Hot 100 15 - 缺失的第一个正数

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/)
- 难度：困难
- 标签：数组、原地哈希
- 本地模式：ACM 标准输入输出

## 题目摘要

找出没有出现在无序整数数组中的最小正整数。要求 O(n) 时间、O(1) 算法额外空间。

## 输入描述

第一行输入数组长度 n；第二行输入 n 个整数。

## 输出描述

输出缺失的最小正整数。

## 数据范围

1 <= n <= 10^5；-2^31 <= nums[i] <= 2^31-1；允许修改原数组，输入读取占用不计入算法额外空间。

## 样例

输入：

```text
4
3 4 -1 1
```

输出：

```text
2
```

## 本地测试

- `tests/01.in` / `tests/01.out`：正负混合。
- `tests/02.in` / `tests/02.out`：单个一。
- `tests/03.in` / `tests/03.out`：单个零。
- `tests/04.in` / `tests/04.out`：连续正数。
- `tests/05.in` / `tests/05.out`：重复正数。
- `tests/06.in` / `tests/06.out`：全部为负。
- `tests/07.in` / `tests/07.out`：整数上下界。
- `tests/08.in` / `tests/08.out`：最大长度、逆序连续。
