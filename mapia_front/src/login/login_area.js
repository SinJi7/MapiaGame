
import React, { Component } from 'react'
// import { useState } from 'react';
// import { socket } from '../socket_connet';
// import { useAsync } from "react-async"
// import axios from 'axios';
//import io from 'socket.io-client';

class Login_area extends Component {
    constructor(props) {
        super(props)

        this.state = {
            user_name: 'test',
            room_name: 'room1'
        }

        this.handle_change_user = this.handle_change_user.bind(this)
        this.handle_change_room = this.handle_change_room.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handle_change_user(event) {
        this.setState({ user_name: event.target.value })
    }
    handle_change_room(event) {
        this.setState({ room_name : event.target.value })
    }
    handleSubmit(event)
    {
        //console.log("dsklsd")
        this.props.join_room(
            this.state.room_name,
            this.state.user_name
        )
        event.preventDefault()
    }
    
    render() {
        return (
        <div>
            <form onSubmit={this.handleSubmit}>
                Name <input
                    type="text"
                    placeholder="kevin"
                    value={this.state.user_name}
                    onChange={this.handle_change_user}
                /> <br/>
                Room <input
                    type="text"
                    placeholder="room_a"
                    value={this.state.room_name}
                    onChange={this.handle_change_room}
                /> <br/>
                <button type='submit'>Join</button>
            </form>
        </div>
        )
    }
}



export default Login_area;