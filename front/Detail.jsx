import React from 'react'
import { useLocation } from 'react-router-dom'
export default function Detail() {
  let location = useLocation();
  console.log(location.state.username)
  return (
    <div>Detail
      <span>{location.state.username}</span>
    </div>
  )
}
