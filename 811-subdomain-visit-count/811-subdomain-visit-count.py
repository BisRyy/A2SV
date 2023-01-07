class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        '''
        cpdomains = [
                        "900 google.mail.com", 
                        "50 yahoo.com", 
                        "1 intel.mail.com", 
                        "5 wiki.org"
                    ]
        
                    [
                        "901 mail.com",
                        "50 yahoo.com",
                        "900 google.mail.com",
                        "5 wiki.org",
                        "5 org",
                        "1 intel.mail.com",
                        "951 com"
                    ]
        '''
        pairs = defaultdict(int)
        for domains in cpdomains:
            count, domain = map(str, domains.split())
            for i in range(len(domain.split('.'))):
                pairs[domain.split('.',i)[-1]] += int(count)
                
        answer = []
        for pair in pairs:
            answer.append(str(pairs[pair]) + " " + str(pair))
        
        return answer
            
            
            
            
            