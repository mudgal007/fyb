import { motion } from 'framer-motion';

export default function HeroBanner() {
  return (
    <section className="relative overflow-hidden py-20" id="top">
      <div className="absolute inset-0 -z-10">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 via-purple-500/5 to-transparent blur-3xl" />
        <motion.div
          className="absolute top-1/2 left-1/2 h-[600px] w-[600px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-aurora/10 blur-3xl"
          animate={{ scale: [1, 1.1, 1], opacity: [0.4, 0.7, 0.4] }}
          transition={{ repeat: Infinity, duration: 12, ease: 'easeInOut' }}
        />
      </div>
      <div className="mx-auto max-w-6xl px-6">
        <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.9 }}>
          <p className="text-sm uppercase tracking-[0.4em] text-aurora/70">Productivity · Wellness · Community</p>
          <h1 className="mt-6 text-4xl md:text-6xl font-display leading-tight text-stardust">
            A galaxy of rituals to help you find your balance.
          </h1>
          <p className="mt-6 max-w-2xl text-lg text-stardust/70">
            Architect life goals, craft daily rituals, and tune into a community that keeps your mind, body, and ambitions in sync.
            Find Your Balance is a futuristic command center for your most intentional self.
          </p>
          <div className="mt-10 flex flex-wrap gap-4">
            <motion.a
              href="#goals"
              className="inline-flex items-center rounded-full bg-aurora px-6 py-3 text-sm font-semibold text-abyss shadow-glow"
              whileHover={{ scale: 1.05 }}
            >
              Begin the reflection orbit
            </motion.a>
            <motion.a
              href="#community"
              className="inline-flex items-center rounded-full border border-aurora/40 px-6 py-3 text-sm font-semibold text-aurora"
              whileHover={{ scale: 1.05 }}
            >
              Visit the community hub
            </motion.a>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
