/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        "primary": "#f8f8f8",
        "secondary": "#686868",
        "accent": "#a0a0a0",
        "error": "#D92525",
        "succes": "#A3CCAB"
      }
    },
  },
  plugins: [],
}

