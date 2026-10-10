import re


class IntentRecognition:
    RULES = [
        ("greeting", re.compile(
            r"^(hi|hello|hey|good morning|good afternoon|good evening)[!. ]*$"
        )),
        ("goodbye", re.compile(
            r"^(bye|goodbye|see you|see you later)[!. ]*$"
        )),
        ("thanks", re.compile(
            r"^(thanks|thank you|thank you so much|much appreciated)[!. ]*$"
        )),
        ("help", re.compile(
            r"^(help|help me|what can you do)\??$"
        )),
        ("identity", re.compile(
            r"^(who are you|what are you|what is noxaria)[?!. ]*$"
        )),
        ("get_time", re.compile(
            r"^(what time is it|tell me the time|current time)[?!. ]*$"
        )),
        ("get_date", re.compile(
            r"^(what is the date|what's the date|what day is it|today's date)[?!. ]*$"
        )),
        ("open_application", re.compile(
            r"^(open|launch|start|run)\s+.+$"
        )),
        ("search_files", re.compile(
            r"^(find|search for|locate)\s+.+$"
        )),
        ("create_reminder", re.compile(
            r"^(remind me|set a reminder|create a reminder)\b.*$"
        )),
    ]

    def classify(self, processed_input: dict) -> dict:
        text = processed_input["normalized"]

        for intent_name, pattern in self.RULES:
            if pattern.fullmatch(text):
                return {
                    "name": intent_name,
                    "confidence": 1.0,
                    "method": "rules",
                }

        return {
            "name": "unknown",
            "confidence": 0.0,
            "method": "rules",
        }
