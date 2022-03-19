import React from 'react'

import "../css/login.css"
import "../css/border.css"
import "../css/button.css"

export default function Signup() {
    const submit_signup = ()=>{
        ;
    }
  return (
      
    <div class = "main_box">
    <div class = "title">Brog</div>
    <hr></hr>
    
        <div class = "sub_box left_right_border">
            <div class = "sub_title">Think-outside-the-box</div>
            <div class = "input_group">
                <input size={35} class = "myinput input_border" type='text' placeholder = "输入账号"></input>
                <input size={35} class = "myinput input_border" type='text' placeholder = "输入用户名"></input>
                <input size={35} class = "myinput input_border" type='text' placeholder = "输入密码"></input>
            </div>
        </div>
        <div class = "btn_group">
            <button class = "btn" onClick={submit_signup}>注册</button>
        </div>
    </div>
  )
}
