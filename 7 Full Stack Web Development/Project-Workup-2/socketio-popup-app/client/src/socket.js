import { io } from "socket.io-client";

const URL = "http://localhost:4000"; // Match your backend port
export const socket = io(URL);
