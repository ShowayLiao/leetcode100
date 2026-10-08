# LeetCode Hot 100 45 - 从前序与中序遍历序列构造二叉树

> 状态：本地用例通过。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- Difficulty: 中等
- Tags: 二叉树、递归、数组、哈希表
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 n；第二行输入前序遍历序列；第三行输入中序遍历序列。节点值互不相同。

## Local output contract

按层序输出构造出的二叉树，空节点写为 null。

## Constraints

- 1 <= n <= 10^4。

## Example

Input:
```text
5
3 9 20 15 7
9 3 15 20 7
```

Output:
```text
3 9 20 null null 15 7
```

The local format is a concise practice contract; consult the source link for the original statement.
