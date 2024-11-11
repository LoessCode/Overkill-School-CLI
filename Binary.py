class BinaryDatabase:    
    def __init__(self, filePath: str):
        self.dbPath: str = filePath;
        self.columns: list = [];
        
        fileObject: TextIOWrapper = open(self.dbPath, "wb");
        fileObject.close();
        
        self.columns: list = [];
        
    def add_column(self, arguments: dict) -> None:
        try:
            columnHeader: str = arguments['h'];
            columnType: any = eval(arguments['t']);
            
            import Column
            
            self.columns.append(
                Column.Column(
                    columnHeader, columnType
                )
            );
            
            import Log;
            Log.console_message(
                f"Added column '{columnHeader}' of type -> {columnType}"
            );

        except KeyError:
            import Log;
            Log.console_message(
                "Missing arguments -h and or -t for column name and type",
                0
            );


    def insert_values(self, arguments: dict) -> None:
        userInput: str;
        try:
            userInput = arguments['v'].split(","); #//Of the format 'v': "woah, 13"
            
            if (len(userInput) == len(self.columns)):
                writeData: list = [];
                
                for value, column in zip(userInput, self.columns):
                    writeData.append(
                        column.type(value)
                    );
                
                with open(self.dbPath, "ab") as binaryDBFile:
                    import pickle;
                    pickle.dump(writeData, binaryDBFile);
                
            else:
                import Log;
                Log.console_message(
                    "Incorrect number of values",
                    0
                );
            
                
        except KeyError:
            import Log;
            Log.console_message(
                "Missing argument -v for values"
            );
            
        except FileNotFoundError:
            import Log;
            Log.console_message(
                f"Missing database file: {self.dbPath}",
                0
            );
            
    
    def view_values(self, arguments: dict) -> None:
        try:
            with open(self.dbPath, "rb") as dbFile:
                for column in self.columns:
                    print(column.header, ' | ', end='');
                print();

                import pickle;
                while True:
                    print(*pickle.load(dbFile));
        except EOFError:
            print();
    
    