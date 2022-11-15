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
      room_name : "",
      user_name : "",
      messages : [{user_name: "admin", message: "connect..."},
    ],
      users : [
    ],
      time: "afternoon",
      target_type  : "투표",
      target : "",
      job_name: ""
    }
    this.join_room = this.join_room.bind(this)
    this.send_message = this.send_message.bind(this)
    this.setTarget = this.setTarget.bind(this)
    this.game_startting = this.game_startting.bind(this)
    this.update_room_user = this.update_room_user.bind(this)

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

    socket.on("game_start", (data) => {
      socket.emit("join_mapia", {
        user_name: this.state.user_name,
        room_name: this.state.room_name,
      })
      socket.emit("get_job", {
        user_name: this.state.user_name,
        room_name: this.state.room_name
      })
    })
    
    socket.on("set_job", (data) => {
      this.setState({job_name: data["job_name"]})
    })


    //target 수집 요청시 응답
    socket.on("get_target", (data) => {
      socket.emit("send_target", {
        type: data["type"],
        user_name: this.state.user_name,
        room_name: this.state.room_name,
        target_name : this.state.target
      })

    })

    //미구현
    socket.on("time_update", (data) =>{
      this.setState({time: data["time"]})
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
  game_startting(user_name, room_name){
    console.log("start")
    socket.emit("game_start", {
      user_name : user_name,
      room_name : room_name
    })
  }

  update_room_user(user_name, room_name)
  {
    this.setState({user_name: user_name, room_name: room_name})
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
        game_startting={this.game_startting}
        user_name= {this.state.user_name}
        room_name= {this.state.room_name}
        update_room_user={this.update_room_user}
      />
      <div className='game_state'>
        시간: {this.state.time}
        직업: {this.state.job_name}
      </div>
      <Chat_area
        send_message={this.send_message}
        messages={this.state.messages}
        room_name={this.state.room_name}
        user_name={this.state.user_name}
      />
      <Users_area
        users={this.state.users}
        setTarget={this.state.target}
      /> 

    </div>)
  }
}


export default App;
