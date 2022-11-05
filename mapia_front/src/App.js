import { useState } from 'react';
import Chat_area from './chat/chat_area';
import Login_area from './login/login_area';

function App() {
  //앱 최상단에서 관리
  const [token, setToken] = useState(false)
  const [room, setRoom] = useState("py")
  const [name, setName] = useState("Anonymous")

  return (
    <>
      <Login_area
        setRoom={setRoom}
        room={room}
        token={token}
        setToken={setToken}
        name={name}
        setName={setName}
      />
      <Chat_area token={token} room={room}/>
      
    </>
  );
}

export default App;
