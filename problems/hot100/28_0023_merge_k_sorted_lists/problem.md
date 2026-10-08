# LeetCode Hot 100 28 - 合并 K 个升序链表

> 状态：未实现。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
- Difficulty: 困难
- Tags: 链表、堆、归并
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 k；接下来每条链表占两行：长度 n，然后是 n 个升序节点值。空链表的值行可为空。

## Local output contract

输出合并后升序链表的节点值，以空格分隔；空链表输出 empty。

## Constraints

- 0 <= k <= 1000；所有链表总长度不超过 10000；节点值为整数。

## Example

Input:
```text
3
3
1 4 5
3
1 3 4
2
2 6
```

Output:
```text
1 1 2 3 4 4 5 6
```

The local format is a concise practice contract; consult the source link for the original statement.
