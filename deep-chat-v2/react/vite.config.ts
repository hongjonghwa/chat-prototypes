import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server:{
    host: '0.0.0.0',
    allowedHosts: true,
  },
  preview:{
    host: '0.0.0.0',
    allowedHosts: true,
  },
})

// ...
// import dotenv from 'dotenv'
// dotenv.config()
// const ALLOWED_HOSTS = process.env['ALLOWED_HOSTS']?.split(',')

