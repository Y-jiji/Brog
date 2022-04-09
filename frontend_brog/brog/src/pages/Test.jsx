import React, { useEffect, useState } from 'react'
import Test_item from './Test_item'
export default function Test() {
    const [l, setL] = useState([]);
    useEffect(()=>{
        // let tmp = [];
        for (let i = 0; i < 10; i++){
            l.push(<Test_item key={i} />)
        }
        let tmp = [];
        tmp = l.slice(0);
        setL(tmp);
        console.log(l)
        return () => {}
    }, [])
    console.log(l)
  return (
    
        l
    
  )
}
