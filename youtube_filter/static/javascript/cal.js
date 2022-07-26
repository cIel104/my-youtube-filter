// 直前の入力が四則演算か確認
let isEquLast = true;

// 初期表示
window.onload = function () {
    filter = document.getElementById('filter');
    word = document.getElementById("word");
    button = document.getElementById("submit-btn");
};

// Cキー押下
function onClearClick() {
    filter.value = "";
    isEquLast = true;
    checkInput(word.value, filter.value)
}

// フィルターキー押下
function onNumClick(className) {

    let val = document.querySelector(className).dataset["value"]
    if (isEquLast == true) {
        filter.value += val;
        isEquLast = false;
        checkInput(word.value, filter.value)
    }

}

// 演算子キー押下
function onOpeClick(className) {

    let val = document.querySelector(className).dataset["value"]
    if (isEquLast == false) {
        filter.value += val;
        isEquLast = true;
    }

}

// 検索ワードとフィルターが入力されている場合、検索ボタンを活性化させる
function checkInput(word, filter) {
    if (word != '' && filter != '') {
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}

// デモ
