import React, { useState } from 'react';
import { socket } from '../socket_connet';
import { useAsync } from "react-async"
import axios from 'axios';
//import io from 'socket.io-client';


function Login_area(props) {

    const handleSubmit = async (event) => {
        //get요청 구현하기
        event.preventDefault()
        const response = await axios.get('http://localhost:4000/token', {
            params: { room_name: props.room, user_name: props.name },
        })
        console.log("실행")
        
        await socket.emit("addroom", {room_name: props.room, token: response.data.token});

        props.setToken(response.data.token)
    };

    const room_handleChange = ({ target: { value } }) => props.setRoom(value);
    const name_handleChange = ({ target: { value } }) => props.setName(value);
    return (
        <form className="login_area" onSubmit={handleSubmit} >
            Token: {props.token} {" "}
            room_number <input value={props.room} onChange={room_handleChange}></input>
            name : <input value={props.name} onChange={name_handleChange}></input>
            <button type="submit">LOGIN</button>
        </form>
    )
}

export default Login_area;