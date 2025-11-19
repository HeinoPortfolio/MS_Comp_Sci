// server.js (Backend)
import express from "express";
import { createServer } from "node:http";
import { Server as SocketIOServer } from "socket.io";
import mongoose from "mongoose";
import cors from "cors";

// MongoDB Connection
mongoose
  .connect("mongodb://localhost:27017/post_db", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Post Schema and Model (example)
const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  link: String,
  createdAt: { type: Date, default: Date.now },
});
const Post = mongoose.model("Post", postSchema);

const app = express();
const httpServer = createServer(app);
const io = new SocketIOServer(httpServer, {
  cors: {
    origin: "http://localhost:5173", // Frontend URL
    methods: ["GET", "POST"],
  },
});

app.use(cors());
app.use(express.json());

// API endpoint to create a new post
app.post("/api/posts", async (req, res) => {
  try {
    const { title, content } = req.body;

    const newPost = new Post({ title, content });
    //await newPost.save(); // Save the document first to get the _id
    const new_post = await newPost.save();

    // newPost.link = `/posts/${newPost._id}`;
    newPost.link = "https://heinoportfolio.github.io/";

    io.emit(
      "newPostNotification",
      {
        message: `A new post titled "${newPost.title}" has been added!`,
        postLink: newPost.link,
        postId: newPost._id,
      },
      console.log("Created the new post nofication backend!!! "),
      console.log("Value of the new post with title: ", new_post.title),
      console.log("Value of the new post content: \n", new_post.content)
    );

    res.status(201).json(newPost);
  } catch (error) {
    console.error("API Error:", error);
    res
      .status(500)
      .json({ error: "Failed to create post", details: error.message });
  }
});

io.on("connection", (socket) => {
  console.log("A user connected:", socket.id);
  socket.on("disconnect", () => {
    console.log("User disconnected:", socket.id);
  });
});

const PORT = 3000;
httpServer.listen(PORT, () => console.log(`Server running on port ${PORT}`));
