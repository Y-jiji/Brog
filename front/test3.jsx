import React, { useEffect, useState } from 'react'

export default function App() {
    const [num1, sets] = useState(1);
    useEffect(()=>{alert(num1)}, [num1])
    //监控变量num1，如果监测所有，则第二个参数不需要,不想监控，则空数组


    useEffect(()=>{
        return ()=>{
            console.log("垃圾回收");
        }
    })
  return (
    <div>test3
        <span>{num1}</span>
        <button onClick={()=>sets(num1+1)}>ss</button>
    </div>
  )
}
