import React, { useRef, useState } from 'react'

// 受控组件和不受控组件
export default function App() {
    const [value, setValue] = useState("asd");
    const inputChange = (e) =>{
        console.log(e.target.value);
        setValue(e.target.value);
    }
    const element = useRef(null);
  return (
      <>
        <div>App</div>
        <input type = "text" value={value} onChange={inputChange} />
        
        <input  type = "text" ref={element} />
        <button onClick={()=>console.log(element.current.value)}>打印</button>
    </>
  )
}
