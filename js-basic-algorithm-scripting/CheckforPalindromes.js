function palindrome(str) {
    str.replace(/[[`':;',‘；：”“'。，、？]]/gi, ""); //正则去掉空格和标点
    var newstring = str.split("").reverse().join(""); //翻转字符串
    if (newstring === str) {
        return true;
    } else if (newstring !== str) {
        return false;
    }
}

palindrome("eye");