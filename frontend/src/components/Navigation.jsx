import { Disclosure } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import { motion } from 'framer-motion';
import { useAuth } from '../context/AuthContext.jsx';

const navigation = [
  { name: 'Goals', href: '#goals' },
  { name: 'Personal Space', href: '#personal' },
  { name: 'Planner', href: '#planner' },
  { name: 'Tracker', href: '#tracker' },
  { name: 'Journal', href: '#journal' },
  { name: 'Community', href: '#community' }
];

export default function Navigation() {
  const { profile } = useAuth();

  return (
    <Disclosure as="nav" className="sticky top-0 z-50 bg-abyss/80 backdrop-blur-xl border-b border-white/5">
      {({ open }) => (
        <>
          <div className="mx-auto max-w-7xl px-6">
            <div className="flex h-16 items-center justify-between">
              <motion.a
                href="#top"
                className="text-lg font-display tracking-[0.2em] uppercase text-aurora"
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                Find Your Balance
              </motion.a>
              <div className="hidden md:flex items-center gap-6">
                {navigation.map((item) => (
                  <motion.a
                    key={item.name}
                    href={item.href}
                    className="text-sm font-medium text-stardust/70 hover:text-aurora transition"
                    whileHover={{ scale: 1.05 }}
                  >
                    {item.name}
                  </motion.a>
                ))}
              </div>
              <div className="hidden md:block text-right">
                <p className="text-xs uppercase text-stardust/60">Logged in as</p>
                <p className="font-semibold text-stardust">
                  {profile?.full_name || 'Guest Explorer'}
                </p>
              </div>
              <div className="md:hidden flex items-center">
                <Disclosure.Button className="inline-flex items-center justify-center rounded-md p-2 text-stardust hover:bg-white/10 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-aurora">
                  <span className="sr-only">Open main menu</span>
                  {open ? <XMarkIcon className="block h-6 w-6" aria-hidden="true" /> : <Bars3Icon className="block h-6 w-6" aria-hidden="true" />}
                </Disclosure.Button>
              </div>
            </div>
          </div>

          <Disclosure.Panel className="md:hidden border-t border-white/5 bg-abyss/95">
            <div className="space-y-1 px-4 pb-4 pt-2">
              {navigation.map((item) => (
                <Disclosure.Button
                  key={item.name}
                  as="a"
                  href={item.href}
                  className="block rounded-md px-3 py-2 text-base font-medium text-stardust/80 hover:bg-white/10"
                >
                  {item.name}
                </Disclosure.Button>
              ))}
            </div>
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  );
}
