import { motion } from 'framer-motion';
import { communityHighlights } from '../data/mockData.js';
import { useRealtime } from '../context/RealtimeContext.jsx';

export default function CommunityHub() {
  const { events } = useRealtime();

  return (
    <section id="community" className="mx-auto mt-16 max-w-6xl px-6">
      <div className="glass-panel p-8">
        <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="section-title">Community</h2>
            <p className="mt-2 text-stardust/60">
              Greeted daily with motivational quotes, join global posts, and participate in events that elevate everyone.
            </p>
          </div>
          <div className="text-sm text-aurora/80">
            Live activity stream
            <span className="ml-2 inline-flex h-2 w-2 animate-pulse rounded-full bg-aurora" aria-hidden="true" />
          </div>
        </div>
        <div className="mt-6 grid gap-6 md:grid-cols-[2fr,1fr]">
          <div className="space-y-4">
            {communityHighlights.map((post, index) => (
              <motion.article
                key={post.title}
                className="rounded-2xl border border-white/10 bg-white/5 p-6"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
              >
                <h3 className="text-lg font-semibold text-stardust">{post.title}</h3>
                <p className="mt-3 text-sm text-stardust/60">{post.body}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {post.tags.map((tag) => (
                    <span
                      key={tag}
                      className="rounded-full bg-aurora/10 px-3 py-1 text-xs uppercase tracking-wide text-aurora"
                    >
                      #{tag}
                    </span>
                  ))}
                </div>
              </motion.article>
            ))}
          </div>
          <aside className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h3 className="text-sm uppercase tracking-[0.3em] text-aurora/70">Live Feed</h3>
            <ul className="mt-4 space-y-3 text-sm text-stardust/70">
              {events.length === 0 && <li className="text-stardust/40">Share a goal update to see live activity.</li>}
              {events.map((event, index) => (
                <li key={`${event.payload?.message || index}-${index}`} className="rounded-xl bg-white/5 p-3">
                  <p className="text-xs text-aurora/60">{event.type}</p>
                  <p>{event.payload?.message || 'A new action just happened.'}</p>
                </li>
              ))}
            </ul>
          </aside>
        </div>
      </div>
    </section>
  );
}
