import React, { useState } from 'react';

function Chat_view(props) {
    return (
        <div className="chat_view">
            {props.chat_log.reverse().map(e => <li class="Chatting_Block">{e.name} : {e.chat}</li>)}
        </div>
    )
}

export default Chat_view;
