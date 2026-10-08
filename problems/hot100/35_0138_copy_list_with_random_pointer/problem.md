# LeetCode Hot 100 35 - 随机链表的复制

> 状态：未实现。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/)
- Difficulty: 中等
- Tags: 链表、哈希表、深拷贝
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 n；随后 n 行，每行输入节点值 val 和 random 指向的 0 起始下标；-1 表示 random 为空。next 按输入行顺序连接。

## Local output contract

先输出 n，再逐行输出复制链表的 val 和 random 的 0 起始下标；-1 表示空。复制节点须与原节点身份不同，本地文本输出只能核对值和指针关系。

## Constraints

- 0 <= n <= 10000；-1 <= random 下标 < n；n 为 0 时无节点行；节点值为整数。

## Example

Input:
```text
5
7 -1
13 0
11 4
10 2
1 0
```

Output:
```text
5
7 -1
13 0
11 4
10 2
1 0
```

The local format is a concise practice contract; consult the source link for the original statement.
