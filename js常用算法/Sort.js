function ArrayList() {
    var array = [];

    this.insert = function (item) {
        array.push(item);
    };

    this.toString = function () {
        return array.join();
    };

    //交换两个数
    var swap = function (index1, index2) {
        var aux = array[index1];
        array[index1] = array[index2];
        array[index2] = aux;
    };

    //改进冒泡排序
    this.modifiedBubbleSort = function () {
        var length = array.length;

        for (var i = 0; i < length; i++) { //控制数组经过多少轮排序
            for (var j = 0; j < length - 1 - i; i++) { //从第一位迭代至倒数第二位
                if (array[j] > array[j + 1]) { //当前项和下一项比较
                    swap(j, j + 1);
                }
            }
        }
    };

    //选择排序：原址比较
    this.selectionSort = function () {
        var length = array.length,
            indexMin;

        for (var i = 0; i < length - 1; i++) { //迭代数组
            indexMin = i; //数组第一个为最小值
            for (var j = i; j < length; j++) { //从当前i至数组结束
                if (array[indexMin] > array[j]) {
                    indexMin = j;
                }
            }
            if (i !== indexMin) {
                swap(i, indexMin);
            }
        }
    };

    //插入排序
    this.insertionSort = function () {
        var length = array.length,
            j, temp;

        for (var i = 1; i < length; i++) { //迭代数组，默认第一项排序
            j = i; //初始化一个辅助变量
            temp = array[i];
            while (j > 0 && array[j - 1] > temp) { //找到位置，前面的值比此值大
                array[j] = array[j - 1]; //交换
                j--; //j减少
            }
            array[j] = temp; //赋值
        }
    };

    //归并排序:分治递归算法
    this.mergeSort = function () {
        array = mergeSortRec(array);
    };
    //将大数组分成小数组
    var mergeSortRec = function (array) {
        var length = array.length;

        if (length === 1) {
            return array;
        }

        var mid = Math.floor(length / 2),
            left = array.slice(0, mmid),
            right = array.slice(mid, length);

        return merge(mergeSortRec(left), mergeSortRec(right));
    };
    //合并小数组
    var merge = function (left, right) {
        var result = [],
            il = 0,
            ir = 0;

        while (il < left.length && ir < right.length) {
            if (left[il] < right[ir]) {
                result.push(left[il++]);
            } else {
                result.push(right[ir++]);
            }
        }

        while (il < left.length) {
            result.push(left[il++]);
        }
        while (il < right.length) {
            result.push(right[ir++]);
        }

        return result;
    };

    //快速排序:分治递归
    this.quickSort = function () {
        quick(array, 0, array.length - 1);
    };
    //快排
    var quick = function (array, left, right) {
        var index;

        if (array.length > 1) {
            index = partition(array, left, right);
            if (left < index - 1) {
                quick(array, left, index - 1);
            }
            if (index < right) {
                quick(array, index, right);
            }
        }
    };
    //划分过程
    var partition = function (array, left, right) {
        var pivot = array[Math.floor((right + left) / 2)],
            i = left,
            j = right; //选主元

        while (i <= j) {
            while (array[i] < pivot) {
                i++;
            }
            while (array[j] > pivot) {
                j--;
            }
            if (i <= j) {
                swapQuickStort(array, i, j);
                i++;
                j--;
            }
        }
        return i;
    }；
    //交换数组元素
    var swapQuickStort = function (array, index1, index2) {
        var aux = array[index1];
        array[index1] = array[index2];
        array[index2] = aux;
    };
}