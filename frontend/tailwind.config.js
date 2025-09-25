/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        abyss: '#050714',
        aurora: '#6ee7ff',
        nebula: '#a855f7',
        cyber: '#22d3ee',
        stardust: '#f8fafc'
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Space Grotesk', 'sans-serif']
      },
      boxShadow: {
        glow: '0 0 30px rgba(110,231,255,0.35)'
      }
    }
  },
  plugins: []
};
