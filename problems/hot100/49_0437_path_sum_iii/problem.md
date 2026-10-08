# LeetCode Hot 100 49 - 路径总和 III

> 状态：本地用例通过。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)
- Difficulty: 中等
- Tags: 二叉树、深度优先搜索、前缀和
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 n 和 targetSum；第二行输入 n 个按层序排列的节点值，空节点写为 null。

## Local output contract

输出路径节点值之和等于 targetSum 的路径数量。路径必须向下，但不要求从根节点开始。

## Constraints

- 1 <= n <= 10^4；节点值和 targetSum 为整数。

## Example

Input:
```text
11 8
10 5 -3 3 2 null 11 3 -2 null 1
```

Output:
```text
3
```

The local format is a concise practice contract; consult the source link for the original statement.
