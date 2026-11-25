from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Poem, Task
from .forms import AnswerForm


def _seed_defaults_if_needed() -> None:
    # Maak een standaard gedicht als er nog geen actief gedicht bestaat
    if not Poem.objects.filter(active=True).exists():
        Poem.objects.create(
            title="Voorbeeldgedicht",
            body=(
                "Dit is een voorbeeldgedicht voor je surprise-site.\n"
                "Pas het aan in de admin onder 'Poems'."
            ),
            active=True,
        )
    # Maak drie voorbeeldopdrachten als er nog geen bestaan
    if Task.objects.count() == 0:
        Task.objects.create(order=1, question="Wat is 2 + 3?", correct_answer="5", digit="1")
        Task.objects.create(order=2, question="Welke kleur krijg je door rood en geel te mengen?", correct_answer="oranje", digit="4")
        Task.objects.create(order=3, question="Vul het woord aan: Sinter_____", correct_answer="klaas", digit="7")


@login_required
def home(request: HttpRequest) -> HttpResponse:
    _seed_defaults_if_needed()

    poem = Poem.objects.filter(active=True).order_by("-created_at").first()
    tasks = list(Task.objects.order_by("order")[:3])

    # Zorg dat we exact 3 taken tonen (als beheerder er minder/of meer heeft gemaakt)
    tasks = (tasks + [])[0:3]

    result: dict | None = None
    combination: str | None = None
    revealed: str | None = None

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid() and len(tasks) == 3:
            answers = [
                form.cleaned_data["answer1"],
                form.cleaned_data["answer2"],
                form.cleaned_data["answer3"],
            ]
            checks: list[bool] = []
            for task, ans in zip(tasks, answers, strict=False):
                ok = task.correct_answer.strip().lower() == str(ans).strip().lower()
                checks.append(ok)

            correct_count = sum(1 for c in checks if c)
            score = round((correct_count / max(1, len(tasks))) * 10, 1)

            if all(checks):
                combination = "".join(t.digit for t in tasks)
            else:
                revealed = "".join(t.digit if ok else "?" for t, ok in zip(tasks, checks, strict=False))

            result = {
                "correct_count": correct_count,
                "total": len(tasks),
                "score": score,
            }
    else:
        form = AnswerForm()

    context = {
        "poem": poem,
        "tasks": tasks,
        "form": form,
        "result": result,
        "combination": combination,
        "revealed": revealed,
    }
    return render(request, "poemlock/home.html", context)
