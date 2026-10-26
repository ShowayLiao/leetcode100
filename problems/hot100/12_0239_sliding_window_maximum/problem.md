# LeetCode Hot 100 12 - 滑动窗口最大值

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)
- 难度：困难
- 标签：数组、滑动窗口、单调队列
- 本地模式：ACM 标准输入输出

## 题目摘要

长度为 k 的窗口从数组左端开始，每次右移一位。依次输出每个完整窗口的最大元素。

## 输入描述

第一行输入 n 和 k；第二行输入 n 个整数。

## 输出描述

输出 n-k+1 个窗口最大值，用单个空格分隔。

## 数据范围

1 <= k <= n <= 10^5；-10^4 <= nums[i] <= 10^4；目标时间 O(n)。

## 样例

输入：

```text
8 3
1 3 -1 -3 5 3 6 7
```

输出：

```text
3 3 5 5 6 7
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通窗口。
- `tests/02.in` / `tests/02.out`：单元素。
- `tests/03.in` / `tests/03.out`：窗口为一。
- `tests/04.in` / `tests/04.out`：窗口等于数组。
- `tests/05.in` / `tests/05.out`：重复最大值。
- `tests/06.in` / `tests/06.out`：全负递增。
- `tests/07.in` / `tests/07.out`：递减及数值边界。
- `tests/08.in` / `tests/08.out`：最大数组长度。
