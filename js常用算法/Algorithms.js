//斐波那契数列:递归
function fibonacci(num) {
    if (num === 1 || num === 2) {
        return 1;
    }

    return fibonacci(num - 1) + fibonacci(num - 2);
}

//斐波那契数列:非递归
function fib(num) {
    var n1 = 1,
        n2 = 1,
        n = 1;
    for (var i = 3; i <= num; i++) {
        n = n1 + n2;
        n1 = n2;
        n2 = n;
    }
    return n;
}

//动态规划：将大问题转化成小问题
//最少硬币找零问题:找到n所需的最小硬币数
function dpMinCoinChange(coins) {
    var coins = coins;
    var cache = {};

    this.makeChange = function (amount) {
        var me = this;
        if (!amount) { //判断为正
            return [];
        }
        if (cache[amount]) { //判断是否有缓存
            return cache[amount];
        }

        var min = [],
            newMin, newAmount;
        for (var i = 0; i < coins.length; i++) { //对每个面额计算
            var coin = coins[i];
            newAmount = amount - coin;
            if (newAmount >= 0) {
                newMin = me.makeChange(newAmount);
            }
            if (newAmount >= 0 && (newMin.length < min.length - 1 || !min.length) && (newMin.length || !newAmount)) { //判断newAmount是否有效，最小硬币数是否最优，newMin和newAmount是否合理
                min = [coin].concat(newMin);
                console.log('new Min ' + min + ' for ' + amount);
            }
        }

        return (cache[amount] = min);
    }
}

//贪心算法：近似求解，通过局部最优达到全局最优
//最少硬币找零问题:找到n所需的最小硬币数
function txMinCoinChange(coins) {
    var coins = coins;

    this.makeChange = function (amount) {
        var change = [],
            total = 0;

        for (var i = coins.length; i >= 0; i--) { //对每个面额从大面额开始，从大到小依次
            var coin = coins[i];
            while (total + coin <= amount) {
                change.push(coin);
                total += coin;
            }
        }

        return change;
    }
}