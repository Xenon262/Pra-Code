// 获取场次的文本框 --- 处理完成之后的网页要返回给当前网页的时间区域
var timeText = document.getElementById("timeText");
// 小时显示框
var hNum = document.getElementById("hNum")
// 分钟显示框
var mNum = document.getElementById("mNum")
// 秒钟显示框
var sNum = document.getElementById("sNum")

// 获取当前系统时间
// 调用函数
// getTime();


// 设置计时器，不断获取时间刷新网页
// setInterval()调用的函数，间隔的时间（单位是毫秒）
setInterval(getTime,1000)


// 封装函数，获取当前时间
function getTime() {
    // 获取系统当前时间
    var odate = new Date();
    // 获取小时
    var hours = odate.getHours();
    // 获取分钟
    var minutes = odate.getMinutes();
    // 获取秒
    var seconds = odate.getSeconds();


    // 判断当前小时是奇数还是偶数
    if (hours%2==0) {
        //偶数
        timeText.innerHTML = hours + ":00";
        // 小时位置的显示数字01
        hNum.innerHTML = "01";
    }
    else{
        //奇数
        timeText.innerHTML = (hours - 1) + ":00";
        // 小时位置的显示数字00
        hNum.innerHTML = "00";
    }

    // 分钟
    // 判断是否小于10
    if ((59-minutes) < 10) {
        mNum.innerHTML = "0" + (59 - minutes);
    }
    else{
        mNum.innerHTML = 59 - minutes;
    }
    // 秒钟
    if ((59 - seconds) < 10) {
        sNum.innerHTML = "0" + (59 - seconds);
    }
    else{
        sNum.innerHTML = 59 - seconds;
    }
}