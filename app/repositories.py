class JSONRepository:
    def process(self, json_data):
        # Example processing: Capitalize all string values in JSON
        def capitalize_strings(data):
            if isinstance(data, dict):
                return {k: capitalize_strings(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [capitalize_strings(v) for v in data]
            elif isinstance(data, str):
                return data.capitalize()
            else:
                return data

        return capitalize_strings(json_data)
