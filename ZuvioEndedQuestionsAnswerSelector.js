//用來獲取zuvio已結算的問答答案
//bug待測
//請到需要獲取答案的畫面按F12，把下面的程式複製之後貼到console執行
//js解構賦值(line 12之用法)之參考 => https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

let w = document.getElementsByClassName("sub-question")
let s = []
let result = ''
let sel = { 1: 'A', 2: 'B', 3: 'C', 4: 'D' }

for (let i = 0; i < w.length; i++) {
    let p = [...w[i].children[w[i].children.length-1].children]  //答案區塊在第二層的最後一個元素
    let target = p.find(arr => arr.children.length >= 2)
    s.push(p.indexOf(target)+1)
}


//在把數字對到字母之前，記得檢查是否皆讀取成功
for (let i = 0; i < s.length; i++) {
    result += (i % 5 != 4) ? `${sel[s[i]]} ` : `${sel[s[i]]}\n`
}

console.log(result)