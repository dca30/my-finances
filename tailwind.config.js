/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "app/templates/**/*.html",
    "app/static/**/*.css",
    "node_modules/@shadcn/ui/dist/**/*.{js,ts,jsx,tsx}", 
],
  theme: {
    extend: {},
  },
  plugins: [],
};
