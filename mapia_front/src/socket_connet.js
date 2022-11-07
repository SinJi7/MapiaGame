import io from 'socket.io-client';

export let socket = io.connect("http://localhost:4000/");

// import React from 'react';
// import io from 'socket.io-client';
        
// const SOCKET_ADDR = 'http://localhost:4000/';
        
// export const socket = io(SOCKET_ADDR);

// const socket = io("localhost:5001/", {
//     transports: ["websocket"],
//     cors: {
//       origin: "http://localhost:3000/",
//     },
//   });