import React, { Component } from 'react';

class UsersArea extends Component {
    constructor(props) {
        super(props)
        this.radio_handle_change = this.radio_handle_change.bind(this)
        this.userRadio = this.userRadio.bind(this)
    }

    radio_handle_change(event) {
        console.log(event.target.value)
        this.props.setTarget(event.target.value)
    }
    userRadio() {
        return (<>
            {this.props.users.map(e => {
                return <><input type="radio" name="userls"value={e.user_name} /> {e.user_name}[{e.info}]<br /></>
            })}
        </>)
    }

    render() {
        return (
            <div className='target_area'>
                <form onChange={this.radio_handle_change}>
                    {this.userRadio()}
                </form>
            </div>)
    }
}

export default UsersArea;