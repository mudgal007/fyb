import { motion } from 'framer-motion';
import { personalLists } from '../data/mockData.js';

const LIST_TITLES = {
  books: 'Books to Read',
  skills: 'Skills to Acquire',
  wishlist: 'Wishlist',
  travel: 'Travel',
  movies: 'Movies',
  events: 'Events',
  people: 'People in My Space'
};

export default function PersonalSpace() {
  return (
    <section id="personal" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        {Object.entries(personalLists).map(([key, entries], index) => (
          <motion.div
            key={key}
            className="glass-panel p-6"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.05, duration: 0.5 }}
          >
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-stardust">{LIST_TITLES[key]}</h3>
              <span className="text-xs uppercase tracking-[0.2em] text-aurora/60">{entries.length} entries</span>
            </div>
            <ul className="mt-4 space-y-2 text-sm text-stardust/70">
              {entries.map((entry, idx) => (
                <li key={idx} className="rounded-xl bg-white/5 px-4 py-2">
                  {typeof entry === 'string' ? (
                    entry
                  ) : (
                    <div>
                      <p className="font-medium text-stardust">{entry.name}</p>
                      <p className="text-xs text-stardust/60">“{entry.quote}”</p>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          </motion.div>
        ))}
      </div>
      <motion.div
        className="mt-10 grid gap-6 md:grid-cols-3"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        variants={{ hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0, transition: { staggerChildren: 0.1 } } }}
      >
        {['best traits', 'areas to improve', 'sources of joy'].map((title) => (
          <motion.div key={title} className="glass-panel p-6" variants={{ hidden: { opacity: 0, y: 10 }, visible: { opacity: 1, y: 0 } }}>
            <p className="text-sm uppercase tracking-[0.3em] text-aurora/70">{title}</p>
            <p className="mt-3 text-sm text-stardust/70">
              Capture reflection prompts daily. The AI companion surfaces patterns and recommends what to do more—or less—of.
            </p>
          </motion.div>
        ))}
      </motion.div>
    </section>
  );
}
