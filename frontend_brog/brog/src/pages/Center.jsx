import React, { useState } from 'react'
import "../css/center.css"
import "../css/border.css"
import "../css/button.css"
import image from "../img/frog.png"
export default function Center() {
    const name = "JOUK";
    const [activeName, setActiveName] = useState("阅读历史");
  return (
    <div class = "center_box">
        <div class = "center_navi top_bottom_border">
            <div class = "icon">
                <img class="img" src={image}></img>
            </div>
            <div class = "center_name">
                {name}
            </div>
            <div class = "center_btn_group">
                <button class = "btn_big">阅读记录</button>
                <button class = "btn_big">我的笔记</button>
                <button class = "btn_big">消息</button>
            </div>
        </div>
        <div class = "center_show left_right_border">
            <div class = "center_title top_bottom_border_small">
                {activeName}
            </div>
            <div class = "center_window">
                
            </div>
        </div>
    </div>
  )
}
