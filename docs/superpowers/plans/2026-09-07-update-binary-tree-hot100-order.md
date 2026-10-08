# Update Binary Tree Hot 100 Order

## Goal

Add the 15 binary-tree Hot 100 entries in their original category position, using internal orders `36` through `50` instead of continuing from the currently created item `11`.

## Changes

1. Create one standard ACM-style problem directory for each binary-tree entry under `problems/hot100/36_...` through `problems/hot100/50_...`.
2. Add each directory's `problem.md`, `main.py`, `notes.md`, and initial `tests/01.in` and `tests/01.out` files.
3. Update `sets/leetcode_hot100.md` with local links while preserving the existing problem order and the current `1 / 100` completed count.
4. Verify the directory names, links, and repository tool tests.

## Verification

- Check that all 15 directory names use orders `36`–`50` and preserve the real LeetCode IDs.
- Check that all 15 checklist entries point to their matching local directories.
- Run `python -m unittest discover -s tests -v`.
