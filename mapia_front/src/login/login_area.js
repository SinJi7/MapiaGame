
import React, { Component } from 'react'

class LoginArea extends Component {
    constructor(props) {
        super(props)

        this.state = {
            user_name: Math.random().toString(36).substring(2, 12),
            room_name: 'room1'
        }

        this.handle_change_user = this.handle_change_user.bind(this)
        this.handle_change_room = this.handle_change_room.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.start_handleSubmit = this.start_handleSubmit.bind(this)

    }

    handle_change_user(event) {
        this.setState({ user_name: event.target.value })
    }
    handle_change_room(event) {
        this.setState({ room_name: event.target.value })
    }

    start_handleSubmit(event) {
        console.log(this.props.user_name)
        this.props.game_startting(
            this.props.user_name,
            this.props.room_name
        )
        event.preventDefault()
    }

    //login area
    handleSubmit(event) {
        //console.log("dsklsd")
        this.props.join_room(
            this.state.room_name,
            this.state.user_name
        )
        this.props.update_room_user(this.state.user_name, this.state.room_name)
        event.preventDefault()
    }

    render() {
        return (
            <div className='form_area'>
                <form className='login' onSubmit={this.handleSubmit}>
                    Name <input
                        type="text"
                        placeholder="kevin"
                        value={this.state.user_name}
                        onChange={this.handle_change_user}
                    /> <br />
                    Room <input
                        type="text"
                        placeholder="room_a"
                        value={this.state.room_name}
                        onChange={this.handle_change_room}
                    /> <br />

                    <button type='submit'>Join</button>
                </form>

                <form onSubmit={this.start_handleSubmit}>
                    <button type='submit'> Start</button>
                </form>
            </div>
        )
    }
}


export default LoginArea;