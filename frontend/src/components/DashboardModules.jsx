import { useState } from 'react';
import { Reorder, motion } from 'framer-motion';
import { ChartBarIcon, RocketLaunchIcon, SparklesIcon } from '@heroicons/react/24/outline';

const MODULES = [
  {
    id: 'goals',
    title: 'Goals & Timeline',
    description: 'Zoom across your 10-year to 1-month ambitions and see momentum at a glance.',
    icon: RocketLaunchIcon
  },
  {
    id: 'planner',
    title: 'Planner AI',
    description: 'Drag rituals into your holographic calendar and sync across calendars instantly.',
    icon: ChartBarIcon
  },
  {
    id: 'mood',
    title: 'Mood & Habit Pulse',
    description: 'Track streaks, moods, and receive adaptive nudges tuned to your energy.',
    icon: SparklesIcon
  }
];

export default function DashboardModules() {
  const [modules, setModules] = useState(MODULES);

  return (
    <section className="mx-auto mt-10 max-w-6xl px-6" aria-labelledby="dashboard-modules">
      <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 id="dashboard-modules" className="section-title">
            Compose your personal mission control
          </h2>
          <p className="mt-3 max-w-2xl text-stardust/60">
            Reorder the core experiences to match your focus. Each module updates in real-time as you progress.
          </p>
        </div>
        <p className="text-sm text-stardust/50">Drag & drop to prioritize</p>
      </div>
      <Reorder.Group axis="x" values={modules} onReorder={setModules} className="mt-8 grid gap-6 md:grid-cols-3">
        {modules.map((module) => (
          <Reorder.Item key={module.id} value={module}>
            <motion.div
              className="glass-panel p-6 h-full"
              whileHover={{ translateY: -6 }}
              transition={{ type: 'spring', stiffness: 120 }}
            >
              <div className="flex items-center gap-4">
                <module.icon className="h-10 w-10 text-aurora" aria-hidden="true" />
                <h3 className="text-lg font-semibold text-stardust">{module.title}</h3>
              </div>
              <p className="mt-4 text-sm text-stardust/60">{module.description}</p>
            </motion.div>
          </Reorder.Item>
        ))}
      </Reorder.Group>
    </section>
  );
}
