import React, { useState } from 'react';
import { socket } from '../socket_connet';

function Login_area(props)
{

    const handleSubmit = (event) => {
        //get요청 구현하기
        const data = {room: props.room, name: props.name}

    };
    const room_handleChange = ({ target: { value } }) => props.setRoom(value);
    const name_handleChange = ({ target: { value } }) => props.setName(value);
    return(
        <form class="login_area" onSubmit={handleSubmit}>
            Token: {props.token}
            room_number <input value={props.room} onChange={room_handleChange}></input>
            name : <input value={props.name} onChange={name_handleChange}></input>
        </form>
    )
}

export default Login_area;