// データ
var result = "";
// =で計算したかどうか
var isCalc = false;

// 初期表示
window.onload = function () {
    result = document.getElementById('result');
};

// Cキー押下
function onClearClick() {
    result.value = "0";
    isCalc = false;
}

// 数字キー押下
function onNumClick(val) {

    if (isCalc) result.value = "0";
    isCalc = false;

    if (result.value == "0" && val == "0") {
        result.value = "0";
    } else if (result.value == "0" && val == ".") {
        result.value = "0.";
    } else if (result.value == "0") {
        result.value = val;
    } else {

        result.value += val;
    }
}

// 演算子キー押下
function onOpeClick(val) {
    if (isCalc) isCalc = false;

    if (isOpeLast()) {
        result.value = result.value.slice(0, -1) + val;
    } else {
        result.value += val;
    }
}

// =キークリック
function onEqualClick() {
    if (isOpeLast()) result.value = result.value.slice(0, -1);

    let temp = new Function("return " + result.value.replaceAll("×", "*").replaceAll("÷", "/"))();
    if (temp == Infinity || Number.isNaN(temp)) {
        result.value = "Error";
    } else {
        result.value = temp;
        isCalc = true;
    }
}

// 入力されている値が演算子かどうか
function isOpeLast() {
    return ["+", "-", "×", "÷"].includes(result.value.toString().slice(-1));
}
/*
document.getElementById('btn').onclick = function get_calc(btn) {
    if (btn.value == "=") {
        document.dentaku.display.value = eval(document.dentaku.display.value);
    } else if (btn.value == "C") {
        document.dentaku.display.value = "";
    } else {
        if (btn.value == "×") {
            btn.value = "*";
        } else if (btn.value == "÷") {
            btn.value = "/";
        }
        document.dentaku.display.value += btn.value;
        document.dentaku.multi_btn.value = "×";
        document.dentaku.div_btn.value = "÷";
    }
}*/