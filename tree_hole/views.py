import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from .models import Challenge, KnowledgeBlock


def _payload(request):
    try:
        return json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return {}


def _challenge_json(challenge):
    return {
        "id": challenge.id,
        "title": challenge.title,
        "description": challenge.description,
        "author": challenge.author_name,
        "discipline": challenge.discipline,
        "tags": [tag.strip() for tag in challenge.tags.split(",") if tag.strip()],
        "hearts": challenge.hearts,
        "blocks": challenge.blocks.count(),
        "created_at": challenge.created_at.isoformat(),
    }


def home(request):
    return render(request, "home.html")


@require_GET
def challenges(request):
    return JsonResponse({"challenges": [_challenge_json(item) for item in Challenge.objects.all()]})


@require_POST
@csrf_exempt
def create_challenge(request):
    data = _payload(request)
    title, description = data.get("title", "").strip(), data.get("description", "").strip()
    if not title or not description:
        return JsonResponse({"error": "A title and context are required."}, status=400)
    challenge = Challenge.objects.create(
        title=title[:120], description=description, discipline=data.get("discipline", "Other")[:50],
        tags=data.get("tags", "")[:240], author_name=data.get("author", "Alex")[:80],
    )
    return JsonResponse(_challenge_json(challenge), status=201)


@require_POST
@csrf_exempt
def add_heart(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    challenge.hearts += 1
    challenge.save(update_fields=["hearts"])
    return JsonResponse({"hearts": challenge.hearts})


@require_POST
@csrf_exempt
def add_block(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    data = _payload(request)
    body = data.get("body", "").strip()
    if not body:
        return JsonResponse({"error": "A knowledge block cannot be empty."}, status=400)
    block = KnowledgeBlock.objects.create(
        challenge=challenge, body=body, author_name=data.get("author", "Alex")[:80],
        discipline=data.get("discipline", "")[:50],
    )
    return JsonResponse({"id": block.id, "body": block.body, "blocks": challenge.blocks.count()}, status=201)
