// PostForm.jsx (Frontend Component to create a post)
//import React from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import axios from "axios";

const createPost = async (newPostData) => {
  const response = await axios.post(
    "http://localhost:3000/api/posts",
    newPostData
  );
  return response.data;
};

const PostForm = () => {
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: createPost,
    onSuccess: () => {
      // Invalidate the 'posts' query
      queryClient.invalidateQueries({ queryKey: ["posts"] });
    },
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    mutation.mutate(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="title" placeholder="Title" required />
      <textarea name="content" placeholder="Content" required />
      <button type="submit" disabled={mutation.isLoading}>
        {mutation.isLoading ? "Creating..." : "Create Post"}
      </button>
    </form>
  );
};

export default PostForm;
