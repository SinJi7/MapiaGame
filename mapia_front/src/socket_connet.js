import io from 'socket.io-client';

export let socket = io.connect("http://localhost:4000/");