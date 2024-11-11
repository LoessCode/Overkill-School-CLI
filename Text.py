
def print_text(arguments: dict) -> None:
    filePath: str;
    modifier: str = "none";
    fileObject: TextIOWrapper;
    
    try:
        filePath = arguments['p'];

        if ('m' in arguments.keys()):
            modifier = arguments['m'];
    
        fileObject = open(filePath, 'r');
        fileContent: list;
        
        if (modifier == "none"):
            fileContent: list = fileObject.readlines();
        
        elif (modifier == 'reverse'):
            fileContent: list = fileObject.readlines()[::-1];
            
        if ('n' in arguments.keys()):
            for i, line in enumerate(fileContent):
                print(f"{i+1} | {line}", end='');
        else:
            for line in fileContent:
                print(line, end='')
                
        fileObject.close();  
        print();
        
    except KeyError:
        import Log;
        Log.console_message(
            "Missing argument -p for file path"
        );
    except FileNotFoundError:
        import Log;
        Log.console_message(
            "Invalid File Path"
        )
   
        
def copy_from_file(arguments: dict) -> None:
    originFilePath: str;
    destinationFilePath: str;
    
    appendMode: bool = False;
    modifier: str = "none";
    
    originFileObject: TextIOWrapper;
    destinationFileObject: TextIOWrapper;
    
    try:
        originFilePath = arguments['p'];
        destinationFilePath = arguments['d'];
        if ('a' in arguments.keys()):
            appendMode = True;
        if ('m' in arguments.keys() and arguments.get('m')):
            modifier = arguments['m'];
            
        
        originFileObject = open(originFilePath, "r");
        if (appendMode):
            destinationFileObject = open(destinationFilePath, "a");
        else:
            destinationFileObject = open(destinationFilePath, "w");
        
        originFileContent: str = originFileObject.read();    
        
        if (modifier == "none"):
            destinationFileObject.write(originFileContent);
        elif (modifier == "flipcase"):
            modifiedFileContent: str = "";
            for character in originFileContent:
                if (character.islower()):
                    modifiedFileContent += character.upper();
                elif (character.isupper()):
                    modifiedFileContent += character.lower();
                else:
                    modifiedFileContent += character;    
                    
            destinationFileObject.write(modifiedFileContent);
            
        destinationFileObject.write("\n");
                
        originFileObject.close();
        destinationFileObject.close();
        
        import Log;
        Log.console_message(
            f"Copied all contents from {originFilePath} to {destinationFilePath} successfully."
        )
                    
    except KeyError:
        import Log;
        Log.console_message(
            "Missing arguments -p and -d for source and destination path.",
            0
        );
        
    except FileNotFoundError:
        import Log;
        Log.console_message(
            "Invalid file path(s)",
            0
        );
        

def stats(arguments: dict) -> None:
    filePath: str;
    fileObject: TextIOWrapper;
    
    try:
        filePath = arguments['p'];
        
        fileObject = open(filePath, "r");
        fileContent: list = fileObject.readlines();
        
        lineCount: int = len(fileContent);
        emptyLineCount: int = 0;
        characterCount: int = 0;
        
        for line in fileContent:
            if (line.strip() == ""):
                emptyLineCount+=1;
            else:
                characterCount+=len(line);
             
        print(f"{len(fileContent)} lines in file");
        print(f"{emptyLineCount} empty lines");
        print(f"{characterCount/lineCount} average characters per line");
        print(f"{characterCount/(lineCount-emptyLineCount)} average characters per non empty line");
        
        
    except KeyError:
        import Log;
        Log.console_message(
            "Missing argument -p for file path"
        );
    except FileNotFoundError:
        import Log;
        Log.console_message(
            "Invalid File Path"
        )
        
    
    
    
    
    
    
    
    
