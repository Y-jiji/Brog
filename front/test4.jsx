import React, { createContext, useContext, useState } from 'react'


const NumContext = createContext()

function Child(){
    const {num, sets} = useContext(NumContext);
    return (
        <NumContext.Consumer>
            {
                ({num, sets}) => (
                    <>
                    <h2>
                        {num}
                    </h2>
                    <button onClick={()=>sets(num+1)}>we</button>
                    </>
                )
            }
        </NumContext.Consumer>
    )
}

function Father(){
    return (
    <NumContext.Consumer>
        {
            ({num}) => {
                <>
                    <h1>
                        {num}
                    </h1>
                    <Child />
                </>
            }
        }
    </NumContext.Consumer>
    )
}

export default function App() {
    //创建上下文空间
    const [num, sets] = useState(1);
  return (
    <NumContext.Provider value={{num, sets}}>
        <>
        <div>test4</div>
        <Father />
        </>
    </NumContext.Provider>
    
  )
}
