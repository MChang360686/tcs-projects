class Company:

    def __init__(self, hash, name, parent, children, amt_owed, due_date):
        self.hash = hash
        self.name = name
        self.parent = parent
        self.children = children
        self.amt_owed = amt_owed
        self.due_date = due_date

    def get_amt_owed(self):
        return self.amt_owed

class HierarchalTracker:

    def __init__(self):
        self.companies = {}

    def add_company(self, hash, name, parent, children, amt_owed, due_date):
        self.companies[hash] = Company(hash, name, parent, children, amt_owed, due_date)

    def get_comp_info(self, hash):
        return self.companies[hash]
    
    def update_company(self, hash, updt_company):
        if hash in self.companies.keys():
            self.companies[hash] = updt_company
        else:
            return None