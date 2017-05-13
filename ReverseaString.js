function reverseString(str) {
    var arrayOfStrings = str.split(""); //把字符串转化成数组
    arrayOfStrings.reverse(); //翻转数组顺序
    str = arrayOfStrings.join(""); //把数组转化成字符串
    return str;
}

reverseString("hello");