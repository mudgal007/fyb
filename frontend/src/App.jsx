import Navigation from './components/Navigation.jsx';
import HeroBanner from './components/HeroBanner.jsx';
import DashboardModules from './components/DashboardModules.jsx';
import GoalTimeline from './components/GoalTimeline.jsx';
import PersonalSpace from './components/PersonalSpace.jsx';
import PlannerTimeline from './components/PlannerTimeline.jsx';
import HabitBoard from './components/HabitBoard.jsx';
import JournalCanvas from './components/JournalCanvas.jsx';
import CommunityHub from './components/CommunityHub.jsx';
import { useAuth } from './context/AuthContext.jsx';
import { useEffect } from 'react';

const demoUser = {
  full_name: 'Nova Quinn',
  email: 'nova@fyb.ai',
  role: 'member'
};

export default function App() {
  const { login, isAuthenticated } = useAuth();

  useEffect(() => {
    if (!isAuthenticated) {
      login('demo-token', demoUser);
    }
  }, [isAuthenticated, login]);

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(34,211,238,0.12),_transparent_60%),#050714]">
      <Navigation />
      <main className="pb-24">
        <HeroBanner />
        <DashboardModules />
        <GoalTimeline />
        <PersonalSpace />
        <PlannerTimeline />
        <HabitBoard />
        <JournalCanvas />
        <CommunityHub />
      </main>
      <footer className="border-t border-white/5 bg-abyss/80 py-8 text-center text-xs text-stardust/50">
        Built for future seekers — AI personalization, offline-ready service workers, and admin analytics included.
      </footer>
    </div>
  );
}
