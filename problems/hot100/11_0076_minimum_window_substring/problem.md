# LeetCode Hot 100 11 - 最小覆盖子串

> 状态：未实现。建题日期：2026-10-26。

- 来源：[LeetCode 76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
- 难度：困难
- 标签：字符串、滑动窗口、哈希表
- 本地模式：ACM 标准输入输出

## 题目摘要

在 s 中找最短的连续子串，包含 t 的全部字符及其重复次数。区分大小写。无解输出空行；本地约定：并列最短答案取起点最小者。

## 输入描述

第一行输入 s，第二行输入 t。两个字符串均非空，只含英文字母，不含空格。

## 输出描述

输出最短覆盖子串；无解输出一个空行。

## 数据范围

1 <= len(s), len(t) <= 10^5；目标时间 O(len(s)+len(t))。

## 样例

输入：

```text
ADOBECODEBANC
ABC
```

输出：

```text
BANC
```

## 本地测试

- `tests/01.in` / `tests/01.out`：普通覆盖。
- `tests/02.in` / `tests/02.out`：最小长度。
- `tests/03.in` / `tests/03.out`：模式串更长、无解。
- `tests/04.in` / `tests/04.out`：重复字符次数。
- `tests/05.in` / `tests/05.out`：区分大小写。
- `tests/06.in` / `tests/06.out`：并列最短取最左。
- `tests/07.in` / `tests/07.out`：字符不存在。
- `tests/08.in` / `tests/08.out`：文本最大长度。
