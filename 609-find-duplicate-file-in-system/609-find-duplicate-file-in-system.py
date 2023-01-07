class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        '''
        paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)"]
        [
            ["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
            ["root/a/1.txt","root/c/3.txt"]
                                                            ]
                                                            
        {
            abcd: [
                   root/a 1.txt,
                   root/c 3.txt
            ],
            efgh: [
                   root/a 2.txt,
                   root/c/d 4.txt,
                   root 4.txt
            ]
        }
                                                            
        '''
        store = defaultdict(list)
        
        for path in paths:
            files = path.split()
            # print (files)
            for index, file in enumerate(files):
                if index > 0:
                    file = file.split('(')
                    store[file[1]].append(files[0] + "/" + file[0])
                # print(file)
        # print (store)
        x = store.values()
        answer = []
        for i in x:
            if len(i) > 1:
                answer.append(i)
        return answer
        
        
        