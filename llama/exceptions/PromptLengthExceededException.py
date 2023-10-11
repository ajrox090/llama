class PromptLengthExceededException(Exception):
    def __init__(self, message="The prompt length exceeds the maximum token limit"):
        self.message = message
        super().__init__(self.message)
