import { motion } from 'framer-motion';
import { plannerEntries } from '../data/mockData.js';

const TYPE_STYLES = {
  priority: 'bg-aurora/20 text-aurora border border-aurora/30',
  work: 'bg-cyan-500/10 text-cyan-200 border border-cyan-400/30',
  self_care: 'bg-purple-500/10 text-purple-200 border border-purple-400/20',
  family: 'bg-pink-500/10 text-pink-200 border border-pink-400/20',
  health: 'bg-emerald-500/10 text-emerald-200 border border-emerald-400/20'
};

export default function PlannerTimeline() {
  return (
    <section id="planner" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="glass-panel p-8">
        <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="section-title">Planner</h2>
            <p className="mt-2 text-stardust/60">
              Month-at-a-glance with instant Google Calendar sync. Build the perfect day with priorities, errands, and self-care.
            </p>
          </div>
          <div className="text-sm text-aurora/80">Auto-sync enabled · Smart prioritization active</div>
        </div>
        <div className="mt-8 space-y-6">
          {plannerEntries.map((entry) => (
            <div key={entry.date} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <div className="flex items-center justify-between">
                <p className="text-sm uppercase tracking-[0.3em] text-aurora/70">{entry.date}</p>
                <p className="text-xs text-stardust/50">Synced with Google Calendar</p>
              </div>
              <div className="mt-4 flex flex-wrap gap-3">
                {entry.items.map((item, index) => (
                  <motion.span
                    key={item.title}
                    className={`rounded-full px-4 py-2 text-xs font-medium ${TYPE_STYLES[item.type] || 'bg-white/10 text-stardust/80 border border-white/10'}`}
                    initial={{ opacity: 0, y: 10 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1, duration: 0.4 }}
                  >
                    {item.title}
                  </motion.span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
