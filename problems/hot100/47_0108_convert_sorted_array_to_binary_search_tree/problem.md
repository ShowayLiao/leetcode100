# LeetCode Hot 100 47 - 将有序数组转换为二叉搜索树

> 状态：本地用例通过。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)
- Difficulty: 简单
- Tags: 二叉树、二叉搜索树、分治
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入 n；第二行输入 n 个严格递增的整数。

## Local output contract

为使本地文本判定具有唯一答案，输出按以下规则构造的高度平衡二叉搜索树的层序序列：

- 每个子数组使用半开区间 `[l, r)`，根下标为 `(l + r) // 2`；偶数长度时选择右侧中点。
- 左子树对应 `[l, mid)`，右子树对应 `[mid + 1, r)`。
- 空节点写为 `null`，删除层序序列末尾连续的 `null`，元素用单个空格分隔。

原题允许多解；以上是本仓库为了严格比较输出而增加的本地约定。

## Constraints

- 1 <= n <= 10^4。

## Example

Input:
```text
5
-10 -3 0 5 9
```

Output:
```text
0 -3 9 -10 null 5
```

The local format is a concise practice contract; consult the source link for the original statement.
