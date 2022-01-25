<template>
  <div class="sub-main-w3">
    <form action="#" method="post">
      <h1>Brog</h1>
      <h2 class="form__title">------------</h2>
      <h2 class="form__title1">Think-outside-the-box</h2>
      <div class="form-style-agile">
        <label>

        </label>
        <input placeholder="Email" name="Email" type="text" required="">
      </div>
      <div class="form-style-agile">
        <label>

        </label>
        <input placeholder="Username" name="Name" type="text" required="">
      </div>
      <div class="form-style-agile">
        <label>

        </label>
        <input placeholder="Password" name="Password" type="password" required="">
      </div>
      <div class="form-style-agile">
        <label>

        </label>
        <input placeholder="Confirm Password" name="Cpassword" type="text" required="">
      </div>

      <div class="wrapper">
        <div class="forms-gds">
          <button class="btn" name="login" type="submit" @click.prevent="$router.push('/login')">登录</button>
          <button class="btn" name="register" type="submit">注册</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "register"
}
</script>

<style scoped>
/*--
Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
--*/

/* reset */

html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
dl,
dt,
dd,
ol,
nav ul,
nav li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}

ol,
ul {
  list-style: none;
  margin: 0px;
  padding: 0px;
}

blockquote,
q {
  quotes: none;
}

blockquote:before,
blockquote:after,
q:before,
q:after {
  content: '';
  content: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

/* start editing from here */

a {
  text-decoration: none;
}

.txt-rt {
  text-align: right;
}

/* text align right */

.txt-lt {
  text-align: left;
}

/* text align left */

.txt-center {
  text-align: center;
}

/* text align center */

.float-rt {
  float: right;
}

/* float right */

.float-lt {
  float: left;
}

/* float left */

.clear {
  clear: both;
}

/* clear float */

.pos-relative {
  position: relative;
}

/* Position Relative */

.pos-absolute {
  position: absolute;
}

/* Position Absolute */

.vertical-base {
  vertical-align: baseline;
}

/* vertical align baseline */

.vertical-top {
  vertical-align: top;
}

/* vertical align top */

nav.vertical ul li {
  display: block;
}

/* vertical menu */

nav.horizontal ul li {
  display: inline-block;
}

/* horizontal menu */

img {
  max-width: 100%;
}

/*end reset*/

body {
  /* 弹性盒子 垂直居中	 */
  align-items: center;
  /* 背景颜色为自定义属性 --white	 */
  background-color: white;
  /* 	背景固定。即使一个元素拥有滚动机制，背景也不会随着元素的内容滚动。 */
  background-attachment: fixed;
  /* 	图片居中 */
  background-position: center;
  /* 	background-repeat定义背景图像的重复方式，no-repeat背景图像将仅显示一次 */
  background-repeat: no-repeat;
  /* 把背景图片放大到适合元素容器的尺寸	 */
  background-size: cover;
  /* 网格布局	 */
  display: grid;
  /* 设置height:100vh，能够保证元素无论是否有没有内容，高度都等于屏幕高度。	 */
  height: 100vh;
  /* 沿着对齐容器的中心对齐。	 */
  place-items: center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  -ms-background-size: cover;
  font-family: 'Open Sans', sans-serif;
  font-size: 100%;
}

/*-- title --*/

h1 {
  font-size: 2.5em;
  color: rgb(0, 0, 0);
  letter-spacing: 2px;/*字间距*/
  /*text-align: center;*/
  /*font-style: italic;设置为斜体*/
  margin: 0cm 1cm 0.01cm 1cm;
  text-align:center;
}

h1 span {
  color: #03A9F4;
}

/*-- //title --*/

/*-- content --*/

.sub-main-w3 {
  display: -webkit-flex;
  display: -webkit-box;
  display: -moz-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  align-items: center;
  -webkit-box-pack: center;
  -moz-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
}

.sub-main-w3 form {

  align-items: center;
  width: 500px;
  height: 520px;
  margin: 0 5vw;
  padding: 3.5vw;
  box-sizing: border-box;
  flex-wrap: wrap;
  justify-content: center;
  border-left: 1.5px solid #000000;/*增加边框*/
  border-right: 1.5px solid #000000;
  border-radius: 30px 30px 30px 30px;/*我们都知道border-radius后面如果是4个值的话,依次代表的是左上角、右上角、右下角、左下角。就这样使边框有弯曲*/
}


.form-style-agile {
  margin-bottom: 0.2em;
  flex-basis: 100%;
  -webkit-flex-basis: 100%;
}

.sub-main-w3 label {
  font-size: 14px;
  color: #fff;
  display: inline-block;
  font-weight: 500;
  margin-bottom: 12px;
  text-transform: capitalize;
  letter-spacing: 1px;
}

.sub-main-w3 label i {
  font-size: 15px;
  margin-left: 5px;
  color: #03A9F4;
  border-radius: 50%;
  line-height: 1.9;
  text-align: center;
}

.form-style-agile input[type="text"],
.form-style-agile input[type="password"] {
  width: 100%;
  color: #000;
  outline: none;
  font-size: 14px;
  letter-spacing: 1px;
  padding: 15px 15px;
  box-sizing: border-box;
  border: none;
  border-top: 1.5px solid #000000;/*增加边框*/
  border-bottom: 1.5px solid #000000;
  border-radius: 10px 10px 10px 10px;/*我们都知道border-radius后面如果是4个值的话,依次代表的是左上角、右上角、右下角、左下角。就这样使边框有弯曲*/
  background: #fff;
}

.wrapper {
  width: 100%;
  padding-right: 15px;
  padding-left: 45px;
  margin-right: auto;
  margin-left: auto;
}

.forms-gds {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 10px;
}

.sub-main-w3 button[type="submit"] {
  background: #ffffff;
  border: none;
  padding: 13px 0;
  margin-top: 20px;
  outline: none;
  width: 130px;
  font-size: 15px;
  cursor: pointer;
  letter-spacing: 2px;
  transition: 0.5s all;
  border-left: 1.5px solid #000000;
  border-right: 1.5px solid #000000;
  border-radius: 10px 10px 10px 10px;
}

.sub-main-w3 button[type="submit"]:hover {
  background: rgb(167, 159, 159);
  -webkit-transition: 0.5s all;
  -o-transition: 0.5s all;
  -moz-transition: 0.5s all;
  -ms-transition: 0.5s all;
  transition: 0.5s all;
}
.form__title {
  /* 字体粗细 */
  font-size: 50%;
  margin: 0;
  margin-bottom: 0.12rem;/*下边距*/
  text-align:center;
}

.form__title1 {
  /* 字体粗细 */
  font-size: 30%;
  margin: 0;
  margin-bottom: 0.1rem;/*下边距*/
  text-align:center;
}

.wthree-text {
  width: 100%;
}

.wthree-text ul li:nth-child(1) {
  float: left;
}

.wthree-text ul li:nth-child(2) {
  float: right;
}

.wthree-text ul li {
  display: inline-block;
}

.wthree-text ul li a {
  color: rgb(0, 0, 0);
  font-size: 14px;
  letter-spacing: 1px;
  font-weight: 500;
}

/*--placeholder-color--*/

::-webkit-input-placeholder {
  color: #000;
}

:-moz-placeholder {
  /* Firefox 18- */
  color: #000;
}

::-moz-placeholder {
  /* Firefox 19+ */
  color: #000;
}

:-ms-input-placeholder {
  color: #000;
}

/*-- //placeholder-color --*/

/*-- //content --*/

/*-- button (switch) --*/

.switch.demo3 {
  width: 56px;
  height: 28px;
}

.switch {
  margin: 0px auto;
  position: relative;
}

.switch input {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  opacity: 0;
  z-index: 100;
  position: absolute;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.switch.demo4 label {
  display: block;
  width: 100%;
  height: 100%;
  background: #e64c65;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  -o-border-radius: 4px;
  color: #FFF;
  box-shadow: inset 0px 0px 0px #0076B3, 0px 0px 0px 0px #1B455A, 0px 2px 1px #FFF;
  -webkit-box-shadow: inset 0px 0px 0px #0076B3, 0px 0px 0px 0px #1B455A, 0px 2px 1px #FFF;
  -moz-box-shadow: inset 0px 0px 0px #0076B3, 0px 0px 0px 0px #1B455A, 0px 2px 1px #FFF;
  -o-box-shadow: inset 0px 0px 0px #0076B3, 0px 0px 0px 0px #1B455A, 0px 2px 1px #FFF;
  font-size: 1.1em;
}

.switch.demo4 label:after {
  content: "";
  position: absolute;
  z-index: -1;
  top: -8px;
  right: -8px;
  bottom: -8px;
  left: -8px;
  border-radius: inherit;
}

.switch.demo4 label:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -5px;
  right: -5px;
  bottom: -5px;
  left: -5px;
  border-radius: inherit;
  /*--background:rgba(51, 92, 140, 0.37);--*/
}

.switch.demo3 label i:before {
  content: " ";
  text-transform: uppercase;
  color: #999999;
  font-size: 0.8em;
  position: absolute;
  top: 50%;
  margin-top: -8px;
  right: -120%;
  color: #fff;
}

.switch.demo3 label {
  display: block;
  width: 100%;
  height: 100%;
  background: #03A9F4;
  border-radius: 40px;
  color: #FFF;
}

.switch.demo3 input:checked~label {
  background: #BDBDBD;
  color: #FFF;
}

.switch.demo3 label:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -5px;
  right: -5px;
  bottom: -5px;
  left: -5px;
  border-radius: inherit;
}

.switch.demo3 input:checked~label i {
  right: -1%;
}

.switch.demo3 label i {
  display: block;
  height: 80%;
  width: 41%;
  border-radius: inherit;
  position: absolute;
  z-index: 2;
  right: 58%;
  top: 3px;
  background: #fff;
  border: none;
  box-shadow: 0 0 4px rgb(46, 46, 46);
  -webkit-box-shadow: 0 0 4px rgb(46, 46, 46);
  -moz-box-shadow: 0 0 4px rgb(46, 46, 46);
  -o-box-shadow: 0 0 4px rgb(46, 46, 46);
}

.switch.demo3 input:checked~label i:before {
  content: " ";
  right: 155%;
  color: #FFF;
}

.switch.demo3 label:after {
  content: "";
  position: absolute;
  z-index: -1;
  top: -8px;
  right: -8px;
  bottom: -8px;
  left: -8px;
  border-radius: inherit;
}

.checkout-w3l a {
  color: #fff;
  letter-spacing: 1px;
  font-size: 15px;
  margin-left: 8px;
  vertical-align: bottom;
}

/*-- //button (switch) --*/

/*-- copyright --*/

.footer {
  margin: 6vw .3vw 2vw;
}

.footer p {
  font-size: 14px;
  color: #fff;
  letter-spacing: 2px;
  text-align: center;
  line-height: 1.8;
}

.footer p a {
  color: #fff;
  -webkit-transition: 0.5s all;
  -o-transition: 0.5s all;
  -moz-transition: 0.5s all;
  -ms-transition: 0.5s all;
  transition: 0.5s all;
}

.footer p a:hover {
  color: #03A9F4;
  -webkit-transition: 0.5s all;
  -o-transition: 0.5s all;
  -moz-transition: 0.5s all;
  -ms-transition: 0.5s all;
  transition: 0.5s all;
}

/*-- //copyright --*/

/*-- responsive --*/

/*--responsive--*/

@media(max-width:1920px) {
  h1 {
    font-size: 3.5vw;
  }
}

@media(max-width:1024px) {
  h1 {
    font-size: 4.5vw;
  }
}

@media(max-width:800px) {
  h1 {
    font-size: 2.6em;
  }
}

@media(max-width:480px) {
  h1 {
    font-size: 2.3em;
  }
  .sub-main-w3 form {
    padding: 7.5vw;
  }
  .footer p {
    letter-spacing: 1px;
  }
}

@media(max-width:414px) {
  .form-style-agile input[type="text"],
  .form-style-agile input[type="password"] {
    font-size: 13px;
    padding: 13px 15px;
  }
  .wthree-text ul li:nth-child(1),
  .wthree-text ul li:nth-child(2) {
    float: none;
  }
  .wthree-text ul li:nth-child(2) {
    margin-top: 10px;
  }
}

@media(max-width:320px) {
  h1 {
    font-size: 1.8em;
  }
  .sub-main-w3 form {
    padding: 25px 14px;
  }
}

/*--//responsive--*/
</style>