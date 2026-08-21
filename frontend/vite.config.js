import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Dev server proxies /drugs/* to the FastAPI backend so the frontend
// can call a relative path and never needs to know the backend's host.
// Change the target below if your backend runs somewhere other than
// http://localhost:8000.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/drugs': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
