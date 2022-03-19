import React from 'react'
import { useNavigate } from 'react-router-dom'
import "../css/login.css"
import "../css/border.css"
import "../css/button.css"
export default function Login() {
    const navigate = useNavigate();


    const signup = ()=>{
        navigate('/signup');
    }
    const submit_login = () => {
        ;
    }
    const forget_pwd = () =>{
        // navigate('/forget');
    }
  return (
    <div class = "main_box">
    <div class = "title">Brog</div>
    <hr></hr>
    
        <div class = "sub_box left_right_border">
            <div class = "sub_title">Think-outside-the-box</div>
            <div class = "input_group">
                <input size={35} class = "myinput input_border" type='text' placeholder = "账号"></input>
                <input size={35} class = "myinput input_border" type='text' placeholder = "密码"></input>
                <div class = "forget" onClick={forget_pwd}>忘记密码？</div>
            </div>
        </div>
        <div class = "btn_group">
            <button class = "btn" onClick={submit_login}>登录</button>
            <button class = "btn" onClick={signup}>注册</button>
        </div>
    </div>
  )
}
