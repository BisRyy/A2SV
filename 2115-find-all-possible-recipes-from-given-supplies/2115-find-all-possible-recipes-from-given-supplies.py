class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        menu = list(zip(recipes, ingredients))
        graph = defaultdict(list)
        indegrees = {r: 0 for r in recipes}
        for r, ing in menu:
            for i in ing:
                graph[i].append(r)
                if i not in supplies:
                    indegrees[r] += 1 
        
        q = deque()
        possibleRecipe = []
        for r, v in indegrees.items():
            if v == 0:
                q.append(r)
                possibleRecipe.append(r)
        
        while q:
            currRecipe = q.popleft()
            for neiRecipe in graph[currRecipe]:
                indegrees[neiRecipe] -= 1
                if indegrees[neiRecipe] == 0:
                    possibleRecipe.append(neiRecipe)
                    q.append(neiRecipe)
        return(possibleRecipe)