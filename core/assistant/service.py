from core.assistant.input_processor import InputProcessor
from core.assistant.intent_recognition import IntentRecognition
from core.assistant.action_router import ActionRouter
from core.assistant.response_generator import ResponseGenerator


class AssistantService:
    def __init__(self, response_mode="rules"):
        self.input_processor = InputProcessor()
        self.intent_recognition = IntentRecognition()
        self.action_router = ActionRouter()
        self.response_generator = ResponseGenerator(mode=response_mode)

    def process_message(self, message):
        processed = self.input_processor.process(message)
        intent = self.intent_recognition.classify(processed)

        action_result = None
        if intent["name"] in ("get_time", "get_date"):
            action_result = self.action_router.execute(intent)

        reply = self.response_generator.generate(
            intent,
            processed,
            action_result,
        )

        return {
            "reply": reply,
            "intent": intent["name"],
            "method": intent["method"],
        }
