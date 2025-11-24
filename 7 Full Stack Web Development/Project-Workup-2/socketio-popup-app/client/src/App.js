import React, { useState, useEffect } from "react";
import { socket } from "./socket";
import NotificationPopup from "./components/NotificationPopup";
import "./App.css";

function App() {
  const [notification, setNotification] = useState(null);

  useEffect(() => {
    const handleNotification = (data) => {
      setNotification(data);
    };

    socket.on("receive_notification", handleNotification);

    // Cleanup function to remove the listener when the component unmounts
    return () => {
      socket.off("receive_notification", handleNotification);
    };
  }, []);

  const closeNotification = () => {
    setNotification(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Socket IO</h1>
      </header>
      <NotificationPopup
        message={notification?.message}
        type={notification?.type}
        link={notification?.link}
        onClose={closeNotification}
      />
    </div>
  );
}

export default App;
