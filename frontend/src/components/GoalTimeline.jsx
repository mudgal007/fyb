import { motion } from 'framer-motion';
import { goalTimeframes } from '../data/mockData.js';

export default function GoalTimeline() {
  return (
    <section id="goals" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="glass-panel p-8">
        <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <h2 className="section-title">Goals & Timeline</h2>
            <p className="mt-3 text-stardust/60">
              Define ambitions across every horizon. Track progress monthly or quarterly and celebrate momentum by life aspect.
            </p>
          </div>
          <div className="text-right text-sm text-aurora/80">
            <p>Work · Family · Social · Personal · Health · Finance · Happiness</p>
            <p className="text-xs text-stardust/50">Synced with your reflections and planner cadence.</p>
          </div>
        </div>
        <div className="mt-10 grid gap-6 md:grid-cols-5">
          {goalTimeframes.map((frame, index) => (
            <motion.div
              key={frame.value}
              className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1, duration: 0.6 }}
            >
              <p className="text-xs uppercase tracking-[0.2em] text-aurora/70">{frame.value}</p>
              <p className="mt-4 text-lg font-semibold text-stardust">{frame.label}</p>
              <div className="mt-6">
                <div className="relative h-2 overflow-hidden rounded-full bg-stardust/10">
                  <motion.div
                    className="absolute inset-y-0 left-0 rounded-full bg-gradient-to-r from-aurora to-nebula"
                    initial={{ width: 0 }}
                    animate={{ width: `${frame.progress * 100}%` }}
                    transition={{ duration: 1.2, ease: 'easeOut' }}
                  />
                </div>
                <p className="mt-2 text-xs text-stardust/50">{Math.round(frame.progress * 100)}% synced</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
