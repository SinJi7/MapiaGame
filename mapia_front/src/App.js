import Chat_area from './chat/chat_area';
import Login_area from './login/login_area';
import Users_area from './controller/Users';


import React, { Component } from 'react'
import io from 'socket.io-client'
const socket = io.connect('http://localhost:4000');

class App extends Component{
  constructor (props) {
    super(props);
    this.state = {
      token : false,
      room : "",
      name : "",
      messages : [{user_name: "admin", message: "connect..."},
    ],
      users : [
    ],
      time: "aftermoon",
      target : "",
    }
    this.join_room = this.join_room.bind(this)
    this.send_message = this.send_message.bind(this)
    this.setTarget = this.setTarget.bind(this)
  }
  componentDidMount () {
    this.setSocketListeners()
  }

  setSocketListeners()
  {
    socket.on("message", (data) => {
      console.log(data)
      const body = {user_name : data["user_name"], message : data["message"]}
      this.setState({messages : [... this.state.messages, body]})
    })

    socket.on("update_user_list", (data) => {
      this.setState({users : data.users})
    })

    socket.on("test", (data) => {
      console.log(data)
    })

    socket.on("user_update", (data) => {
      
      this.setState({users : data.users})
    })

    //미구현
    socket.on("night", () =>{
    })

    socket.on("aftermoon", () => {

    })


  }
  // User act
  join_room(room_name, user_name){
    this.setState({room : room_name, name: user_name}, () => {
      socket.emit("join_room", {room_name, user_name});
    });
  }

  send_message(message, room_name, user_name)
  {
    //console.log(user_name)
    socket.emit("message", {
      room_name: room_name,
      user_name : user_name,
      message : message,
      time: Date.now()
    })
  }
  //game
  setTarget(name)
  {
    this.setState({target : name});
  }

  render()
  {
    return(<div>
      Mapia Game
      <Login_area
        join_room={this.join_room} 
      />
      <Chat_area
        send_message={this.send_message}
        messages={this.state.messages}
        room_name={this.state.room}
        user_name={this.state.name}
      />
      <Users_area
        users={this.state.users}
        setTarget={this.state.target}
      /> 

    </div>)
  }
}


export default App;
