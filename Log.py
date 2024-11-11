import datetime;

def console_message(consoleMessage: any, messageLevel: int = 2) -> None:
    currentTime: any = datetime.datetime.now();
    messageLevelLabels: tuple = ("ERROR", "WARNING", "INFO");
    
    message: str = f"<{messageLevelLabels[messageLevel]} @ {currentTime}> {consoleMessage}"
    
    print(message);
    
    with open("data/log.txt", "a") as logFile:
        logFile.write(message + "\n")
