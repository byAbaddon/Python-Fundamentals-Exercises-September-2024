class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

    def __str__(self):
        if not self.queries:
            return f"https://www.{self.host}.{self.domain}"
        else:
            part_one = f"https://www.{self.host}.{self.domain}/query?="
            part_two = None
            for x in self.queries:
                q = x.split(',')
                part_two = "&".join(['[' + x + ']' for x in q])

            return f"{part_one}{part_two}"


for x in iter(input, 'end'):
    token = x.split(' | ')
    h, d, *q = token
    web = Website(h, d, q)
    print(web)



'''
softuni | bg | user,course,homework
judge.softuni | bg | contest,bg
google | bg | search,query
zamunda | net
end
'''