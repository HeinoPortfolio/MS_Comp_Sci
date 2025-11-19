// App.jsx
import { useState } from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import PostForm from "./PostForm";
import NotificationHandler from "./NotificationHandler";
import "./App.css";

const queryClient = new QueryClient();

function App() {
  const [popupNotification, setPopupNotification] = useState(null);

  const displayPopup = (notificationData) => {
    setPopupNotification(notificationData);
    // Automatically hide popup after a few seconds
    setTimeout(() => setPopupNotification(null), 5000);
  };

  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <h1>Create New Post</h1>
        <PostForm />
        {popupNotification && (
          <div className="popup-notification">
            <p>{popupNotification.message}</p>
            <a href={popupNotification.link}>View Post</a>
          </div>
        )}
      </div>
      {/* NotificationHandler listens for backend events */}
      <NotificationHandler displayPopup={displayPopup} />
    </QueryClientProvider>
  );
}

export default App;
