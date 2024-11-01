class MessageRepository:
    def __init__(self):
        self.storage_file = '/app/messages/message_storage.txt'

    def save_message(self, message) -> int:
        # Save message to persistent storage and return id
        message_id = self._get_next_id()

        with open(self.storage_file, 'a') as file:
            file.write(f"{message_id},{message}\n")
            print(f"Saved message: {message_id},{message}")  # Debugging print

        return message_id

    def _get_next_id(self) -> int:
        try:
            with open(self.storage_file, 'r') as file:
                count = sum(1 for _ in file)  # Count lines to determine next ID
                print(f"Current message count: {count}")  # Debugging print
                return count + 1
        except FileNotFoundError:
            return 1  # Start with ID 1 if the file does not exist

    def get_message(self, id: int) -> str:
        # Return message with id from storage
        try:
            with open(self.storage_file, 'r') as file:
                for line in file:
                    line_id, message = line.strip().split(',', 1)  # Split on the first comma
                    if int(line_id) == id:
                        return message.strip()  # Return the message associated with the ID
            return None  # Return None if message not found
        except FileNotFoundError:
            return None  # Return None if the file does not exist
