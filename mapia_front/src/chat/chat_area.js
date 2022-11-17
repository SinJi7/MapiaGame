import React, { Component } from 'react';

import "../App_design.css"

class ChatArea extends Component
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
        this.setState({ input: ""})
        event.preventDefault()
    }
    viewer(){
        const view_message = this.props.messages
        return (<>
        {
        view_message.map(e => <li className='chat_block'> <div className='profile'><strong>{e.user_name}</strong></div> <div className="message">{e.message}</div></li>)
        }
        </>)
    }

    render()
    {
        return(
        <div className='chat_area'>
            <div className="chat_view">
                {this.viewer()}
            </div>

            <form className="chat_input_area" onSubmit={this.handleSubmit}>
                <input className='chat_input'
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

export default ChatArea;
