
import itertools
class TransactionID:
    def __init__(self, start_id):
        self._start_id = start_id


    def next(self):
        self._start_id +=1
        return self._start_id
    
class Account:
    # transaction_counter=itertools.count(100)
    transaction_counter=TransactionID(100)

    def make_transaction(self):
        # new_trans_id=next(Account.transaction_counter)
        new_trans_id=Account.transaction_counter.next()
        return new_trans_id


a1=Account()
a2=Account()

print(a1.make_transaction())

print(a2.make_transaction())

print(a1.make_transaction())

