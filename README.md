# Instructions To Run

The code can be tested by copy-pasting the below python code at the bottom of the ```Transaction.py``` file. The python program can be run via ```python Transaction.py``` for MacOS or ```py Transaction.py``` for Windows. 

**Note:**
- Exception-raising statments (marked "ERROR-RAISING") will need to be commented out in order to run statements that follow them.

```python
inmemoryDB = Transaction()
# should return null, because A doesn’t exist in the DB yet
print(inmemoryDB.get("A"))
# should throw an error because a transaction is not in progress
inmemoryDB.put("A", 5) # ERROR-RAISING
# starts a new transaction
inmemoryDB.begin_transaction()
# set’s value of A to 5, but its not committed yet
inmemoryDB.put("A", 5)
# should return null, because updates to A are not committed yet
print(inmemoryDB.get("A"))
# update A’s value to 6 within the transaction
inmemoryDB.put("A", 6)
# commits the open transaction
inmemoryDB.commit()
# should return 6, that was the last value of A to be committed
print(inmemoryDB.get("A"))
# throws an error, because there is no open transaction
inmemoryDB.commit()  # ERROR-RAISING
# throws an error because there is no ongoing transaction
inmemoryDB.rollback()  # ERROR-RAISING
# should return null because B does not exist in the database
print(inmemoryDB.get("B"))
# starts a new transaction
inmemoryDB.begin_transaction()
# Set key B’s value to 10 within the transaction
inmemoryDB.put("B", 10)
# Rollback the transaction - revert any changes made to B
inmemoryDB.rollback()
# Should return null because changes to B were rolled back
print(inmemoryDB.get("B"))
```

# Future Assignment Modifications

I think the instrutions were very clear for this assignment. I personally found them very easy to follow, and I found the assignment very reasonable to complete. I think the assignment could maybe be improved by including some more complex user interactions and/or true database usage. I also think that a more universal testing script/suite could make student testing and instructor grading much easier. Overall though, this was actually one of my favorite assignments.