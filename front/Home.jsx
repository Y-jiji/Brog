import React from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
export default function Home() {
  //获取当前路由信息
  const location = useLocation();
  console.log(location);

  //页面跳转
  const navigate = useNavigate();
  const goDetail = () => {
    navigate('/detail', {
      state:{username:'张三'}
    })
  }
  return (
    <div>Home

      <a><Link to="/list">awea</Link></a>
      <button onClick={goDetail}>详情</button>
    </div>
  )
}
