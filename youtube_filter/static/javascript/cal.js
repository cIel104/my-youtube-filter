// 直前の入力が四則演算か確認
let isEquLast = true;

//入力した演算子を記憶
let arithmetic = '';

// 初期表示
window.onload = function () {
    filter = document.getElementById('filter');
    word = document.getElementById("word");
    button = document.getElementById("submit-btn");
};

// Cキー押下
function onClearClick() {
    filter.value = "";
    arithmetic = '';
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
        arithmetic += val;
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
function onClearClickDemo() {
    if (isEquLast == true) {
        console.log('a')
        filter.value = filter.value.slice(0, -1);
        arithmetic = arithmetic.slice(0, -1);
        isEquLast = false;
    } else if (arithmetic == '') {
        onClearClick();
    }
    else {
        let lastarithmetic = arithmetic.slice(-1);
        console.log(lastarithmetic);
        let num = filter.value.lastIndexOf(lastarithmetic);
        filter.value = filter.value.slice(0, num + 1);
        isEquLast = true;
    }
}