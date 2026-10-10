from datetime import datetime


class ActionRouter:
    def execute(self, intent: dict):
        name = intent.get("name")

        if name == "get_time":
            return datetime.now().astimezone().strftime("%I:%M %p")

        if name == "get_date":
            return datetime.now().astimezone().strftime("%A, %d %B %Y")

        return None
