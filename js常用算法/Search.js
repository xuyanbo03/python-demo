// 顺序或线性搜索：将每一个数据结构中的元素和要找的元素作比较
//二分搜索：二分法搜索

function ArrayList() {
    var array = [];

    this.insert = function (item) {
        array.push(item);
    };

    this.toString = function () {
        return array.join();
    };

    //顺序搜索
    this.sequentialSearch = function (item) {
        for (var i = 0; i < array.length; i++) {
            if (item === array[i]) {
                return i;
            }
        }
        return -1;
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
    };
    //交换数组元素
    var swapQuickStort = function (array, index1, index2) {
        var aux = array[index1];
        array[index1] = array[index2];
        array[index2] = aux;
    };

    //二分搜索
    this.binarySearch = function (item) {
        this.quickSort(); //快速排序

        var low = 0,
            high = array.length - 1,
            mid, element;

        while (low <= high) {
            mid = Math.floor((low + high) / 2);
            element = array[mid];

            if (element < item) {
                low = mid + 1;
            } else if (element > item) {
                high = mid - 1;
            } else {
                return mid;
            }
        }

        return -1;
    };
}