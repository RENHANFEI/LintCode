from collections import defaultdict

class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        counts = defaultdict(lambda: 0)
        for cpdomain in cpdomains:
            time, domain = cpdomain.split(' ')
            time = int(time)
            sub_domains = domain.split('.')
            now_domain = sub_domains[-1]
            counts[now_domain] += time
            for sub_domain in sub_domains[::-1][1:]:
                now_domain = sub_domain + '.' + now_domain
                counts[now_domain] += time
                
        ans = []
        for domain, count in counts.items():
            ans.append(str(count) + ' ' + domain)
            
        return ans
