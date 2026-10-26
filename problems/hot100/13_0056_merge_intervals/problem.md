# LeetCode Hot 100 13 - 合并区间

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 56. 合并区间](https://leetcode.cn/problems/merge-intervals/)
- 难度：中等
- 标签：数组、排序、区间
- 本地模式：ACM 标准输入输出

## 题目摘要

合并所有有交集的闭区间，使输出两两不相交且覆盖原区间。端点相等也视为相交。输出按左端点递增排列。

## 输入描述

第一行输入区间数量 n；接下来 n 行每行输入 left 和 right。

## 输出描述

第一行输出合并后的区间数 m；接下来 m 行每行输出一个区间的左右端点。

## 数据范围

1 <= n <= 10^4；0 <= left <= right <= 10^4。

## 样例

输入：

```text
4
1 3
2 6
8 10
15 18
```

输出：

```text
3
1 6
8 10
15 18
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通重叠。
- `tests/02.in` / `tests/02.out`：单点区间。
- `tests/03.in` / `tests/03.out`：端点相接。
- `tests/04.in` / `tests/04.out`：包含关系。
- `tests/05.in` / `tests/05.out`：无序且互不相交。
- `tests/06.in` / `tests/06.out`：重复区间。
- `tests/07.in` / `tests/07.out`：链式重叠及最大端点。
- `tests/08.in` / `tests/08.out`：最大区间数量。
