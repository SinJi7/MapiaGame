import React, { Component, useEffect, useState } from 'react';
//import io from 'socket.io-client';
// import Chat_input from './chat_input';
// import Chat_view from './chat_view';

// import { socket } from '../socket_connet';

//const socket = io.connect("http://localhost:4000/")

class Chat_area extends Component
{
    constructor(props) {
        super(props)
        this.state = {
            input : ""
        }

        this.handle_change_input = this.handle_change_input.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.viewer = this.viewer.bind(this) //나중에 지워보기
    }
    handle_change_input(event) {
        this.setState({ input: event.target.value})
    }

    handleSubmit(event){
        this.props.send_message(this.state.input, this.props.room_name, this.props.user_name)
        event.preventDefault()
    }
    viewer(){
        const view_message = this.props.messages.slice(-10)
        return (<>
        {
        view_message.map(e => <li class="message_block">{e.user_name} : {e.message}</li>)
        }</>)
    }

    render()
    {
        return(
        <div>
            <div className="chat_view">
                {this.viewer()}
            </div>

            <form className="chat_input" onSubmit={this.handleSubmit}>
                <input
                type="text"
                placeholder="send message...."
                value={this.state.input}
                onChange={this.handle_change_input}
                />
                <button type='submit'>send</button>
            </form>
        </div>
        )
    }
}

// function Chat_areas(props)
// {
//     const [chatlog, setChatlog] = useState([])
//     useEffect(()=>{
//         socket.on('message',(e)=>{ //{name,chat}
//             console.log(e)
//             //setChatlog([...chat,{name,chat}])
//         })  
//     },[])

//     const addChat = (chat) => 
//     {
//         console.log("emit")
//         socket.emit('message',"dskfla")
//         //socket.emit('message',{room_name: props.room, token : props.token, message: chat, time: 1})
//         //setChatlog([...chat,{name,chat}])
//     }

//     return (
//         <div className="chat_area">
//             <Chat_view chat_log={chatlog}/>
//             <Chat_input addChat={addChat}/>
//         </div>
//     )
// }

export default Chat_area;
