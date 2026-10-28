class Solution(object):
    def distanceK(self, root, target, k):
        parent={}
        def dfs(node,par):
            if not node:
                return 
            parent[node]=par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        queue=[target]
        visited={target}
        distance=0
        while queue:
            if distance==k:
                return[node.val for node in queue]
            for _ in range(len(queue)):
                node=queue.pop(0)
                for nei in (node.left,node.right,parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            distance+=1
        return []


        