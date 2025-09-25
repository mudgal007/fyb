import { motion } from 'framer-motion';
import { habitBlueprints } from '../data/mockData.js';

export default function HabitBoard() {
  return (
    <section id="tracker" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="grid gap-6 md:grid-cols-2">
        <div className="glass-panel p-8">
          <h2 className="section-title">Tracker & Habits</h2>
          <p className="mt-2 text-stardust/60">
            Monthly goals, to-dos, appointments, shopping, budget — all stitched together with custom recurrence and streak rewards.
          </p>
          <div className="mt-6 space-y-4">
            {habitBlueprints.map((habit, index) => (
              <motion.div
                key={habit.title}
                className="rounded-2xl border border-white/10 bg-white/5 p-4"
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
              >
                <div className="flex items-center justify-between">
                  <p className="font-semibold text-stardust">{habit.title}</p>
                  <p className="text-xs text-aurora/70">{habit.streak} day streak</p>
                </div>
                <div className="mt-3 h-2 overflow-hidden rounded-full bg-stardust/10">
                  <motion.div
                    className="h-full bg-gradient-to-r from-aurora to-nebula"
                    initial={{ width: 0 }}
                    whileInView={{ width: `${Math.min(1, habit.streak / habit.target) * 100}%` }}
                    viewport={{ once: true }}
                    transition={{ duration: 1, ease: 'easeOut' }}
                  />
                </div>
                <p className="mt-2 text-xs text-stardust/50">Target: {habit.target} days</p>
              </motion.div>
            ))}
          </div>
        </div>
        <div className="glass-panel p-8">
          <h3 className="text-2xl font-display text-stardust">Mood Tracker</h3>
          <p className="mt-2 text-stardust/60">
            Journal your mood with notes and let the AI companion send personalized cheer-up suggestions.
          </p>
          <MoodVisualizer />
        </div>
      </div>
    </section>
  );
}

function MoodVisualizer() {
  const gradients = ['from-aurora/60', 'from-nebula/60', 'from-cyan-500/60'];
  const dots = Array.from({ length: 30 }, (_, index) => index + 1);

  return (
    <div className="mt-8 grid grid-cols-6 gap-3" aria-label="Mood tracker heatmap">
      {dots.map((dot) => (
        <motion.div
          key={dot}
          className={`aspect-square rounded-2xl bg-gradient-to-br ${gradients[dot % gradients.length]} to-transparent`}
          initial={{ opacity: 0, scale: 0.8 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ delay: dot * 0.02, duration: 0.4 }}
        />
      ))}
    </div>
  );
}
