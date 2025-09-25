from fastapi import APIRouter

from app.api.routes import auth, community, goals, habits, journal, mood, personal, planner, tracker

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"])
api_router.include_router(habits.router, prefix="/habits", tags=["habits"])
api_router.include_router(mood.router, prefix="/mood", tags=["mood"])
api_router.include_router(journal.router, prefix="/journal", tags=["journal"])
api_router.include_router(planner.router, prefix="/planner", tags=["planner"])
api_router.include_router(tracker.router, prefix="/tracker", tags=["tracker"])
api_router.include_router(personal.router, prefix="/personal", tags=["personal"])
api_router.include_router(community.router, prefix="/community", tags=["community"])
