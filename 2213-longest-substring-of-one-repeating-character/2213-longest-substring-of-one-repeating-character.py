class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # len, pref, suff, best, leftChar, rightChar
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            length1, pref1, suff1, best1, left1, right1 = a
            length2, pref2, suff2, best2, left2, right2 = b

            length = length1 + length2
            pref = pref1
            suff = suff2
            best = max(best1, best2)

            if right1 == left2:
                best = max(best, suff1 + pref2)

                if pref1 == length1:
                    pref = length1 + pref2

                if suff2 == length2:
                    suff = length2 + suff1

            return (length, pref, suff, best, left1, right2)

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = (1, 1, 1, 1, c, c)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, c):
            if l == r:
                tree[node] = (1, 1, 1, 1, c, c)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, c)
            else:
                update(node * 2 + 1, mid + 1, r, idx, c)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, c)
            ans.append(tree[1][3])  # best

        return ans