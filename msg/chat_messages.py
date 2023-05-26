class ChatMessages:
    def __init__(self, data):
        self.messages: [] = data["messages"]
        self.model: str = data["model"]
        self.temperature = data["temperature"]
        self.frequency_penalty = 0.0
        self.presence_penalty = data["presence_penalty"]
        self.stream: bool = data["stream"] if "stream" in data else False
