class Solution:
    def accountsMerge(self, accounts):
        father = [i for i in range(10000)]
        email_to_id = dict()
        email_to_name = dict()
        def find_father(idx):
            if father[idx] != idx:
                father[idx] = find_father(father[idx])
            return father[idx]

        def union(idx1, idx2):
            father1 = find_father(idx1)
            father2 = find_father(idx2)
            father[father1] = father2
        idx = 0
        for row in accounts:
            name = row[0]
            for email in row[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = idx
                    idx += 1
                union(email_to_id[row[1]], email_to_id[email])
        from collections import defaultdict
        tmp = defaultdict(list)
        for each in email_to_id:
            tmp[find_father(email_to_id[each])].append(each)
        res = list()
        for key, value in tmp.items():
            value.sort()
            res.append([email_to_name[value[0]]] + value)
        return res


class Solution:
    def accountsMerge(self, accounts):
        from collections import defaultdict
        graph = defaultdict(set)
        email_to_name = dict()
        for account in accounts:
            for i in range(1, len(account)):
                email_to_name[account[i]] = account[0]
                graph[account[1]].add(account[i])
                graph[account[i]].add(account[1])

        visited = set()
        res = list()
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                component = [email]
                while stack:
                    e = stack.pop()
                    for each in graph[e]:
                        if each not in visited:
                            visited.add(each)
                            component.append(each)
                            stack.append(each)
                component.sort()
                res.append([email_to_name[component[0]]] + component)
        return res




