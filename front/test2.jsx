// import React, { Component } from 'react'

// export default class test2 extends Component {
//   render() {
//     return (
//       <div>test2</div>
//     )
//   }
// }

import {useState} from 'react'

export default function App(){
    //Hook 只能用在最顶层
    const [xxx, setXxx] = useState('hello world');
    
    return (
        <>
            <h2>{xxx}</h2>
            <button onClick={()=>setXxx('weqweq')}>re</button>
        </>
    )
}