import dotenv from 'dotenv'
dotenv.config()

import { initDatabase } from './db/init.js'


import { app } from './app.js'
//const PORT = 3000
const PORT = process.env.PORT

// Initialize the database
await initDatabase()

app.listen(PORT)

console.info(`Express server running on http://localhost:${PORT}`)