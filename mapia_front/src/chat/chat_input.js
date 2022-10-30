import React, { useState } from 'react';

function Chat_input(props)
{
    const [chat, setChat] = useState("");
    const handleSubmit = (event) => {
        event.preventDefault();
        props.addChat(chat, props.id);
    };

    const handleChange = ({ target: { value } }) => setChat(value);
    return (
        <form onSubmit={handleSubmit}>
            <input value={chat} onChange={handleChange} ></input>
            <button type="submit">SEND</button>
        </form>
    )
}

export default Chat_input;