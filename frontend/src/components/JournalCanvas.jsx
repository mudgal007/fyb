import { useMemo } from 'react';
import { motion } from 'framer-motion';

function generateParticles(seed = 12) {
  return Array.from({ length: seed }, (_, index) => ({
    id: index,
    size: Math.random() * 80 + 30,
    x: Math.random() * 100,
    y: Math.random() * 100,
    hue: Math.floor(Math.random() * 360)
  }));
}

export default function JournalCanvas() {
  const particles = useMemo(() => generateParticles(), []);

  return (
    <section id="journal" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="grid gap-6 md:grid-cols-[2fr,1fr]">
        <div className="glass-panel p-8">
          <h2 className="section-title">Journal</h2>
          <p className="mt-2 text-stardust/60">
            Rate your day across life areas, capture gratitude, highlights, feelings, and paint your mood with AI pigments.
          </p>
          <div className="mt-6 space-y-4">
            <div>
              <p className="text-xs uppercase tracking-[0.3em] text-aurora/70">Daily Reflection</p>
              <p className="mt-2 text-sm text-stardust/70">
                “Focus more on mindful meals, reduce evening screen time, amplify collaborations that spark joy.”
              </p>
            </div>
            <div>
              <p className="text-xs uppercase tracking-[0.3em] text-aurora/70">End-of-day Thoughts</p>
              <p className="mt-2 text-sm text-stardust/70">
                Gratitude: “Evening walk with family.” Highlight: “Prototype review went stellar.” Feeling: “Serene.”
              </p>
            </div>
          </div>
        </div>
        <div className="glass-panel relative overflow-hidden">
          <p className="p-6 text-sm text-stardust/60">
            AI Paint Screen
            <span className="block text-xs text-stardust/40">Inspired by your mood metrics.</span>
          </p>
          <div className="relative h-72">
            {particles.map((particle) => (
              <motion.div
                key={particle.id}
                className="absolute rounded-full mix-blend-screen"
                style={{
                  width: particle.size,
                  height: particle.size,
                  left: `${particle.x}%`,
                  top: `${particle.y}%`,
                  background: `radial-gradient(circle at center, hsla(${particle.hue}, 90%, 70%, 0.8), transparent 70%)`
                }}
                initial={{ scale: 0.4, opacity: 0 }}
                animate={{ scale: [0.8, 1.1, 0.9], opacity: [0.2, 0.8, 0.4] }}
                transition={{ repeat: Infinity, duration: 8, delay: particle.id * 0.1 }}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
