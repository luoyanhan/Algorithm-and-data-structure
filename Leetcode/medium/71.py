class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        for each in path.split('/'):
            if '..' == each:
                if stack:
                    stack.pop()
            elif '' == each or '.' == each:
                continue
            else:
                stack.append(each)
        return '/' +  '/'.join(stack)