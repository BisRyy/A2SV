class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for list_index in range(len(words)-1):
            index = 0
            current = words[list_index]
            next = words[list_index + 1]
            min_length = min(len(current), len(next))
            while(index  < min_length):
                if order.find(current[index]) > order.find(next[index]):
                    print(1)
                    return False
                elif order.find(current[index]) == order.find(next[index]):
                    if index == min_length -1 and (len(current) > len(next)):
                        return False
                    index +=1
                else:
                    print(3)
                    break
        return True
