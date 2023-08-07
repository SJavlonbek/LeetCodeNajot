def finalValueAfterOperations(operations):
    return operations.count("++X")+operations.count("X++")-operations.count("--X")-operations.count("X--")

print(finalValueAfterOperations(["--X","X++","X++"]))