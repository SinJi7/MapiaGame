import ChatArea from './chat/chat_area';
import LoginArea from './login/login_area';
import UsersArea from './controller/Users';

import "./App_design.css"

import React, { Component } from 'react'
import io from 'socket.io-client'
const socket = io.connect('http://localhost:4000');

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      token: false,
      room_name: "",
      user_name: "",
      messages: [{ user_name: "안내", message: "Join을 눌러 방에 입장" },
      ],
      users: [
      ],
      time: "Chat",
      target_type: "투표",
      target: "",
      job_name: ""
    }
    this.join_room = this.join_room.bind(this)
    this.send_message = this.send_message.bind(this)
    this.setTarget = this.setTarget.bind(this)
    this.game_startting = this.game_startting.bind(this)
    this.update_room_user = this.update_room_user.bind(this)

  }
  componentDidMount() {
    this.setSocketListeners()
  }

  setSocketListeners() {
    socket.on("message", (data) => {
      console.log(data)
      const body = { user_name: data["user_name"], message: data["message"] }
      this.setState({ messages: [body, ...this.state.messages] })
    })

    socket.on("update_user_list", (data) => {
      this.setState({ users: data.users })
    })

    socket.on("test", (data) => {
      console.log(data)
    })

    socket.on("user_update", (data) => {
      this.setState({ users: data.users })
    })

    socket.on("game_start", (data) => {
      this.setState({time: "afternoon"})
      socket.emit("join_mapia", {
        user_name: this.state.user_name,
        room_name: this.state.room_name,
      })
      socket.emit("get_job", {
        user_name: this.state.user_name,
        room_name: this.state.room_name
      })
    })

    socket.on("end_game", (data) => {
      this.setState({time: "Chat"})
    })

    socket.on("set_job", (data) => {
      this.setState({ job_name: data["job_name"] })
    })


    //target 수집 요청시 응답
    socket.on("get_target", (data) => {
      socket.emit("send_target", {
        type: data["type"],
        user_name: this.state.user_name,
        room_name: this.state.room_name,
        target_name: this.state.target
      })

    })

    //미구현
    socket.on("time_update", (data) => {
      this.setState({ time: data["time"] })
    })
  }

  // User act
  join_room(room_name, user_name) {
    this.setState({ room: room_name, name: user_name }, () => {
      socket.emit("join_room", { room_name, user_name });
    });
  }

  send_message(message, room_name, user_name) {
    //console.log(user_name)
    socket.emit("message", {
      room_name: room_name,
      user_name: user_name,
      message: message,
      time: Date.now()
    })
  }
  game_startting(user_name, room_name) {
    console.log("start")
    socket.emit("game_start", {
      user_name: user_name,
      room_name: room_name
    })
  }

  update_room_user(user_name, room_name) {
    this.setState({ user_name: user_name, room_name: room_name })
  }
  //game
  setTarget(name) {
    this.setState({ target: name });
  }

  render() {
    return (
    <>
    <p className='title'>Mapia Game</p>
    <div className='top_area'>

      <div className='interface'>
        <LoginArea
          join_room={this.join_room}
          game_startting={this.game_startting}
          user_name={this.state.user_name}
          room_name={this.state.room_name}
          update_room_user={this.update_room_user}
        />
        <div className='game_state'>
          <p><strong>Game</strong> {this.state.time}</p>
          <p><strong>Job</strong> {this.state.job_name}</p>
        </div>
      </div>

      <div className='top_chat_area'>
        <ChatArea
          send_message={this.send_message}
          messages={this.state.messages}
          room_name={this.state.room_name}
          user_name={this.state.user_name}
        />
        <UsersArea
          users={this.state.users}
          setTarget={this.setTarget}
        />
      </div>

    </div>
    </>
    )
  }
}


export default App;
