# Constant values
PROCESS_STATUS:dict = {"Pending", "In Progress", "Failed", "Completed"}
FILE_TYPES:dict = {"pdf", "wav", "mp3", "mp4", "txt", "json"}
MSG_INVALID_VALUES:str = "Invalid values provided for the process."

# ProcessItem class to represent an item in a process.
class ProcessItem:
    def __init__(self, process_id:str, source_id:str , source_type: str, source_uri: str, source_name: str, convert_to: str, destination_uri: str):
        self.process_id:str = process_id
        self.source_id:str = source_id
        self.source_type:str = source_type
        self.source_uri:str = source_uri
        self.source_name:str = source_name
        self.convert_to:str = convert_to
        self.destination_uri:str = destination_uri
        self.process_result:str

        # Validate the values provided for the process item.
        if not self.values_ok():
            raise ValueError(f"{self.__class__}: {MSG_INVALID_VALUES}")

        # Validate the values provided for the process item.
        def values_ok(self):
            # Check if the values of the process item are valid.
            if self.process_id is None or source_id is None or source_name is None:
                return False
            if self.source_type not in FILE_TYPES:
                return False
            if self.convert_to not in FILE_TYPES:
                return False
            return True

# Process class to represent a process in the system.
class Process:
    def __init__(self, process_id:str, process_status:str, process_results:str):
        self.process_id:str = process_id
        self.process_status:str = process_status
        self.process_results:str = process_results
        self.source_items: list[ProcessItem] = []
        
        # Validate the values provided for the process.
        if not self.values_ok():
            raise ValueError(f"{self.__class__}: {MSG_INVALID_VALUES}")

    # Validate the values provided for the process.
    def values_ok(self):
        if self.process_id is None:
            return False
        if self.process_status not in PROCESS_STATUS:
            return False
        
    def add_process_item(self, process_item: ProcessItem):
        # Add a process item to the process.
        if not isinstance(process_item, ProcessItem):
            raise TypeError("process_item must be an instance of ProcessItem")
        self.source_items.append(process_item)