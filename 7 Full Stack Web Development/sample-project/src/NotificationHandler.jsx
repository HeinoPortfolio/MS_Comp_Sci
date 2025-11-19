// NotificationHandler.jsx (Global component for notifications)
import { useEffect } from "react";
import io from "socket.io-client";
import PropTypes from "prop-types";

const socket = io("http://localhost:3000");

const NotificationHandler = ({ displayPopup }) => {
  useEffect(() => {
    socket.on("newPostNotification", (notification) => {
      console.log("Received notification:", notification.message);
      displayPopup({
        message: notification.message,
        link: notification.postLink,
      });
    });

    return () => {
      socket.off("newPostNotification");
    };
  }, [displayPopup]);

  return null;
};

NotificationHandler.propTypes = {
  displayPopup: PropTypes.func.isRequired,
};

export default NotificationHandler;
