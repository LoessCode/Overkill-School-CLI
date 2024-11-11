import FunctionManager

if (__name__ == "__main__"): 
    print('\n'*15);
    
    with open("data/log.txt", "w"):
        pass;
    
    functionManager: FunctionManager = FunctionManager.FunctionManager();
    functionManager.run();
    
    