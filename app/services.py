from .repositories import JSONRepository

class JSONProcessingService:
    def __init__(self):
        self.repository = JSONRepository()

    def process(self, json_data):
        # Process the JSON data
        processed_data = self.repository.process(json_data)
        return processed_data
