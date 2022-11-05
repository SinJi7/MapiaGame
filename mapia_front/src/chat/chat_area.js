import React, { useEffect, useState } from 'react';
//import io from 'socket.io-client';
import Chat_input from './chat_input';
import Chat_view from './chat_view';

import { socket } from '../socket_connet';

//const socket = io.connect("http://localhost:4000/")

function Chat_area(props)
{
    const [chatlog, setChatlog] = useState([])
    useEffect(()=>{
        socket.on('message',(e)=>{ //{name,chat}
            console.log(e)
            //setChatlog([...chat,{name,chat}])
        })  
    },[])

    const addChat = (chat) => 
    {
        console.log("emit")
        socket.emit('message',"dskfla")
        //socket.emit('message',{room_name: props.room, token : props.token, message: chat, time: 1})
        //setChatlog([...chat,{name,chat}])
    }

    return (
        <div className="chat_area">
            <Chat_view chat_log={chatlog}/>
            <Chat_input addChat={addChat}/>
        </div>
    )
}

export default Chat_area;
