function factorialize(num) {
    var n = 1;
    for (var i = 1; i <= num; i++) { //计算阶乘
        n = n * i;
    }
    return n;
}

factorialize(5);