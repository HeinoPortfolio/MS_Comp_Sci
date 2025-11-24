const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "http://localhost:3000", // Allow requests from your React app
    methods: ["GET", "POST"],
  },
});

const PORT = 4000;

io.on("connection", (socket) => {
  console.log(`User connected: ${socket.id}`);

  // Example: emit a notification event after a delay or on a trigger
  setTimeout(() => {
    socket.emit("receive_notification", {
      message: "A new event occurred!",
      link: "https://heinoportfolio.github.io/",
      type: "info",
    });
  }, 5000); // Emits a notification 5 seconds after connection

  socket.on("disconnect", () => {
    console.log("User disconnected: ", socket.id);
  });
});

server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
