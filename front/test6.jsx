import React, { useState, memo, useCallback, useMemo } from 'react'

const Child = memo( (props)=> {//不受父组件的更新而再次更新
    console.log(props.dosth());
    return <div>child
        <button onClick={()=>props.dosth()}>ww_child</button>
    </div>
})

export default function App() {
    const [num, setNum] = useState(1);
    const dosth2 = ()=>{setNum(num+1)};
    const dosth3 = useCallback(() => setNum(num=>num+1), []);

    //高阶函数
    const dosth = useMemo(() => {
        return () => setNum(num=>num+1);
    }, [])
  return (
    <div>App
        <h3>数字为{num}</h3>
        <button onClick={()=>{setNum(num+1)}}>ww</button>
        <hr/>
        <Child dosth = {dosth} />
    </div>
  )
}
