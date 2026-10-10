import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from core.assistant.service import AssistantService

assistant = AssistantService(response_mode="rules")


def home(request):
    return render(request, "core/home.html")


@require_POST
def chat_api(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON request."}, status=400)

    if not isinstance(data, dict):
        return JsonResponse(
            {"error": "Request must be a JSON object."},
            status=400,
        )

    try:
        result = assistant.process_message(data.get("message"))
        print("Bot respose:", result)

    except ValueError as error:
        return JsonResponse({"error": str(error)}, status=400)

    return JsonResponse(result)
