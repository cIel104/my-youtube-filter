// データ
var result = "";

// 直前の入力が四則演算か確認
let isEquLast = true;

// 初期表示
window.onload = function () {
    filter = document.getElementById('filter');
};

// Cキー押下
function onClearClick() {
    filter.value = "";
    isEquLast = true;
}

// フィルターキー押下
function onNumClick(val) {

    if (isEquLast == true) {
        filter.value += val;
        isEquLast = false;
    }

}

// 演算子キー押下
function onOpeClick(val) {

    if (isEquLast == false) {
        filter.value += val;
        isEquLast = true;
    }

}