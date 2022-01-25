<template>
  <el-container>
    <el-aside style="padding-bottom: 20px;padding-top: 20px">
      <reader-aside/>
    </el-aside>
    <el-main>
      <reader-main/>
    </el-main>
  </el-container>
</template>

<script>
import main from "./main";
import aside from "./aside";

export default {
  name: "reader",
  components:{
    'reader-aside':aside,
    'reader-main':main,
  },
  mounted() {
    document.title='填写标题'
  }
}
</script>

<style scoped>

</style>