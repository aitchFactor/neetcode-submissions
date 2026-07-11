class Solution:
    def decodeString(self, s: str) -> str:
        dfs = [0]
        ks = [1]
        res = ""
        frag = ""
        while dfs:
            i = dfs.pop()
            v = s[i]
            if v == "]":
                k, frag2 = ks.pop()
                frag = frag2 + k*frag
                if i < len(s)-1:
                    dfs.append(i+1)
                continue
            elif v.isdigit():
                for i2 in range(i+1, i+4):
                    if not s[i2].isdigit():
                        break
                    else:
                        v += s[i2]
                dfs.append(i2+1)
                ks.append((int(v), frag))
                frag = ""
                continue
            else:
                frag += v
                for i2 in range(i+1, min(len(s), i+31)):
                    if (s[i2].isdigit() or s[i2] == "]"):
                        dfs.append(i2)
                        break
                    else:
                        frag += s[i2]
        return frag

                

