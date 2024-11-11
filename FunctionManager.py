class FunctionManager:
    #//Constants
    __COMMAND_CHARACTER: str = "$";
    
    #//Public Functions
    def __init__(self):
        self.binaryDatabases: dict = {};
    
    def run(self) -> None:
        while True:
            print("1 | Text File Handling\n2 | Binary File Handling\nq | Quit");
            userInput = input(">>");
            
            import Log;
            
            if (userInput == 'q'):
                self.__cleanup();
                
                break;
            
            
            elif (userInput == '1'):
                Log.console_message(
                    "Running text interface"
                );
                
                self.__loop_text();
                
            elif (userInput == '2'):
                Log.console_message(
                    "Running binary interface"
                );
                
                self.__loop_binary();
                
            else:
                Log.console_message(
                    "Invalid Choice",
                    1
                );
            
    
    
    #//Internal Functions
    def __parse_args(self, userInput: str) -> dict:        
        arguments: dict = {};
        userInputSplit: list = userInput.strip().split('-')
        
        for token in userInputSplit:
            tokenSplit: tuple = token.partition(" ");
            arguments[tokenSplit[0].strip()] = tokenSplit[2].strip();
            
            
        return arguments;
        
    def __loop_binary(self) -> None:
        import pickle;
        try:
            with open("data/binaryDatabaseCache.bin", "rb") as cacheFile:
                cacheData: dict = pickle.load(cacheFile);
                self.binaryDatabases = cacheData;
        except:
            import Log;
            Log.console_message(
                "No previous binary databases found"
            );
            self.binaryDatabases = {};
        
        
        while True:
            userInput: str = input(">> ").strip();
            if (userInput.startswith(self.__COMMAND_CHARACTER)):
                userInput = userInput[1:].strip();
                
                if (userInput == "quit"):
                    with open("data/binaryDatabaseCache.bin", "wb") as cacheFile:
                        import pickle;
                        pickle.dump(
                            self.binaryDatabases,
                            cacheFile
                        );
                    
                    break; 
                
                
                elif (userInput == "help"):
                    import Text;
                    Text.print_text(
                        "data/help.txt"
                    );
                    
                
                elif (userInput.startswith("create")):
                    arguments: list = self.__parse_args(userInput.partition(' ')[-1]);
                    dbName: str;
                    dbPath: str;
                    try:
                        dbName = arguments['n'];
                        dbPath = arguments['p'];
                        
                        import Binary
                        
                        self.binaryDatabases[dbName.strip()] = Binary.BinaryDatabase(
                            dbPath
                        );
                        
                        import Log;
                        Log.console_message(
                            f"Created binary database '{dbName}' path: {dbPath}"
                        );
                        
                    except KeyError:
                        import Log;
                        Log.console_message(
                            "Missing arguments -p and or -n for path and name",
                            0
                        );
                    
                    
                elif (userInput.startswith("addcolumn")):
                    dbName: str;
                    arguments: list = self.__parse_args(userInput.partition(' ')[-1]);
                    
                    try:
                        dbName = arguments['n'];
                        self.binaryDatabases[dbName].add_column(
                            arguments
                        );
                        

                        
                    except KeyError:
                        import Log;
                        Log.console_message(
                            "Missing argument -n for db name or invalid db name"
                        );
                
                
                elif (userInput.startswith("insertdata")):
                    dbName: str;
                    arguments = self.__parse_args(userInput.partition(' ')[-1]);
                    
                    try:
                        dbName = arguments['n'];
                        
                        self.binaryDatabases[dbName].insert_values(
                            arguments
                        );
                    except KeyError:
                        import Log;
                        Log.console_message(
                            "Missing argument -n for db name or invalid db name"
                        );                       
                
                
                elif (userInput.startswith("showall")):
                    dbName: str;
                    arguments: list = self.__parse_args(userInput.partition(' ')[-1]);
                    
                    try:
                        dbName = arguments['n'];
                        
                        self.binaryDatabases[dbName].view_values(
                            arguments
                        );
                        
                    except KeyError:
                        import Log;
                        Log.console_message(
                            "Missing argument -n for db name or invalid db name"
                        );
                
        import Log;
        Log.console_message(
            "Binary interface closed"
        ); 
            
        
    def __loop_text(self) -> None:        
        while True:
            userInput: str = input(">> ").strip();
            
            if (userInput.startswith(self.__COMMAND_CHARACTER)):
                userInput = userInput[1:].strip();
                
                if (userInput == "quit"):
                    break; 
                
                
                elif (userInput == "help"):
                    import Text;
                    Text.print_text(
                        "data/help.txt"
                    );
                
                
                elif (userInput.startswith("read")):
                    arguments: dict = self.__parse_args(userInput.partition(" ")[-1]);
                    
                    import Text;
                    Text.print_text(arguments);
                                             
                        
                elif (userInput.startswith("copyfromfile")):
                    arguments: dict = self.__parse_args(userInput.partition(" ")[-1]);
                    
                    import Text;
                    Text.copy_from_file(arguments);
    
                    
                elif (userInput.startswith("stat")):
                    arguments: dict = self.__parse_args(userInput.partition(" ")[-1])
                    
                    import Text;
                    Text.stats(arguments);
                
        import Log;
        Log.console_message(
            "Text interface closed"
        );
        
    def __cleanup(self) -> None:
        import Log;
        Log.console_message(
            "Program terminated safely"
        );
    
    