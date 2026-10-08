# LeetCode Hot 100 32 - 环形链表

> 状态：未实现。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)
- Difficulty: 简单
- Tags: 链表、快慢指针
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 n 和 pos；第二行输入 n 个节点值。pos 是尾节点 next 指向的节点下标（从 0 开始）；-1 表示无环。

## Local output contract

有环输出 true，无环输出 false。pos 仅描述链表结构，不是待输出的答案。

## Constraints

- 0 <= n <= 10000；-1 <= pos < n；n 为 0 时 pos 必须为 -1；节点值为整数。

## Example

Input:
```text
4 1
3 2 0 -4
```

Output:
```text
true
```

The local format is a concise practice contract; consult the source link for the original statement.
