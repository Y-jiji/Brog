<template>
  <el-space direction="vertical" :size="70" class="main">
    <el-avatar src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"/>
    <div>{username}</div>
    <el-button class="button"><el-badge value="5"/>阅读历史</el-button>
    <el-button class="button"><el-badge value="5"/>我的笔记</el-button>
    <el-button class="button"><el-badge value="5"/>消息</el-button>
  </el-space>
</template>

<script>

export default {
}
</script>

<style scoped>
.main {
  width: 100%;
  height: 100%;
  color: #000;
  outline: none;
  font-size: x-large;
  letter-spacing: 1px;
  padding: 15px 15px;
  box-sizing: border-box;
  border: none;
  border-top: 1.5px solid #000000;/*增加边框*/
  border-bottom: 1.5px solid #000000;
  border-radius: 10px 10px 10px 10px;/*我们都知道border-radius后面如果是4个值的话,依次代表的是左上角、右上角、右下角、左下角。就这样使边框有弯曲*/
  background: #fff;
}
.button {
  width: 15em;
  font-size: medium;
  border-color: #1B455A;
  border-bottom: 0;
  border-top: 0;
  border-radius: 10px 10px 10px 10px;
}
</style>