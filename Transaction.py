class Transaction:
    def __init__(self): 
        self.activeTransaction = False
        self.pendingTransactions = {}
        self.transactions = {}

    def begin_transaction(self):
        if self.activeTransaction:
            raise Exception("Active transaction already exists")
        else:
            self.activeTransaction = True
            print("Transaction started")

    def put(self, key, value):
        if not self.activeTransaction:
            raise Exception("No active transaction")
        else:
            self.pendingTransactions[key] = value
            print(f"Successfully put {key} : {value}")

    def get(self, key):
        if key in self.transactions:
            return self.transactions[key]
        return None

    def commit(self):
        if not self.activeTransaction:
            raise Exception("No active transaction")
        self.activeTransaction = False
        self.transactions.update(self.pendingTransactions)
        pendingTransactions = {}
        print("Transaction committed")

    def rollback(self):
        if not self.activeTransaction:
            raise Exception("No active transaction")
        self.activeTransaction = False
        self.pendingTransactions = {}
        print("Transaction changes rolled back")