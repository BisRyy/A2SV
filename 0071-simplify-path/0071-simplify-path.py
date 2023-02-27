class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        
        folders = path.split('/')
        
        for folder in folders:
            if folder == '.' or folder == '':
                pass
            elif folder == '..':
                if paths: paths.pop()
            else:
                paths.append(folder)
        print(folders)
        return '/' + '/'.join(paths)