from __future__ import annotations

import random
from datetime import datetime
from typing import Iterable

MOOD_LIBRARY = {
    "happy": [
        "Keep sharing that joy — plan a surprise for someone you love!",
        "Channel your energy into a passion project today.",
    ],
    "stressed": [
        "Try a 5-minute breathing session and block time for deep work.",
        "Delegate one task and schedule a micro-break with movement.",
    ],
    "low": [
        "Reach out to a friend who makes you smile and revisit a gratitude note.",
        "Set a tiny win for the next hour and reward yourself with your favorite track.",
    ],
}


def generate_mood_suggestion(mood: str, intensity: float) -> str:
    suggestions = MOOD_LIBRARY.get(mood.lower(), [])
    if not suggestions:
        suggestions = [
            "Reflect on one bright spot today and plan a rejuvenating activity.",
            "Balance your energy with a hydration break and mindful stretching.",
        ]
    idx = 0 if intensity > 0.6 else 1
    return suggestions[idx % len(suggestions)]


def nudge_for_goal_progress(goal_title: str, progress: float) -> str:
    if progress >= 1.0:
        return f"Goal '{goal_title}' complete! Capture the win in your journal."
    remaining = max(0, 100 - int(progress * 100))
    return f"You're {remaining}% away from '{goal_title}'. Schedule a focused session this week."


def daily_welcome_message(name: str) -> str:
    greetings = [
        "Illuminate your path today",
        "Every rhythm counts",
        "Design the balance you crave",
    ]
    return f"{random.choice(greetings)}, {name}!"
