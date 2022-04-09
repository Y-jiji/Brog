import React from "react";
import "./s.css"
const mystyle = {backgroundColor: "red"};
let arr = ["a", "b", "c"];



class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            num : 1
        }
    }

    render(){
        
        return (
            <>
                {/* 测试 */}
                <div className="ez">hahah</div>
                <h2 style={mystyle}>内容--{this.state.num}</h2>
                <ul>
                    {
                        //列表循环map，只有map有返回值 圆括号无所谓 花括号必写
                        arr.map((item, index)=>{
                            return (<li key={index}>{item}</li>)
                        })
                    }
                </ul>
                <button onClick={()=>this.addNum()}>button</button>
                <button onClick={()=>this.addNum.bind(this)}>button</button>
            </>
        )
    }
    addNum(){
        this.setState({num: this.state.num+1});
        alert(123);
    }
}


export default App;

