# LeetCode Hot 100 34 - 相交链表

> 状态：未实现。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)
- Difficulty: 简单
- Tags: 链表、双指针
- Local mode: ACM-style standard input and output

## Local input contract

依次输入 A 独有前缀、B 独有前缀和共享尾链表：每段先输入长度，再输入该段节点值。A 和 B 的尾部都实际连接到同一组共享节点；共享段为空表示不相交。

## Local output contract

输出第一个共享节点在 A 中的 0 起始下标；不相交输出 -1。节点值相等不代表节点相同。

## Constraints

- 三段总长度不超过 10000；A、B 均至少有一个节点；节点值为整数。

## Example

Input:
```text
2
4 1
3
5 6 1
3
8 4 5
```

Output:
```text
2
```

The local format is a concise practice contract; consult the source link for the original statement.
