class ResponseGenerator:
    def __init__(self, mode="rules"):
        self.mode = mode

    def generate(self, intent, processed_input, action_result=None):
        if self.mode != "rules":
            return (
                f"Response mode '{self.mode}' is not connected yet. "
                "Using rule-based responses for now."
            )

        name = intent.get("name")

        if name == "greeting":
            return "Hello! I'm Noxaria. How can I help you?"

        if name == "hello":
            return "Hello! I'm Noxaria. How can I help you?"

        if name == "goodbye":
            return "Goodbye! I'll be here when you need me."

        if name == "thanks":
            return "You're welcome!"

        if name == "help":
            return (
                "I can respond to greetings, tell you the time and date, "
                "and recognize requests to open applications, search files, "
                "or create reminders. The latter actions are not implemented yet."
            )

        if name == "identity":
            return (
                "I'm Noxaria, your personal assistant project. "
                "I'm currently running with a basic rule-based engine."
            )

        if name == "get_time":
            return (
                f"The current local time is {action_result}."
                if action_result else "I couldn't retrieve the time."
            )

        if name == "get_date":
            return (
                f"Today is {action_result}."
                if action_result else "I couldn't retrieve the date."
            )

        if name == "open_application":
            return (
                "I recognized an application-launch request, but launching "
                "applications has not been enabled yet."
            )

        if name == "search_files":
            return (
                "I recognized a file-search request, but file searching "
                "has not been implemented yet."
            )

        if name == "create_reminder":
            return (
                "I recognized a reminder request, but the reminder system "
                "has not been implemented yet."
            )

        return (
            "I don't understand that request yet. Try asking for the time "
            "or date, or type 'help' to see what I can do."
        )
