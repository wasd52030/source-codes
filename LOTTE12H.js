let target = document.querySelector("#mount_0_0_rQ > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.j83agx80.buofh1pr.dp1hu0rb.l9j0dhe7.du4w35lb.ka73uehy > div.rq0escxv.l9j0dhe7.du4w35lb.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.j83agx80.dp1hu0rb > div > div > div.j83agx80.cbu4d94t.buofh1pr > div > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.hpfvmrgz.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.gile2uim.qmfd67dx > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.cwj9ozl2.tvmbv18p")
let users = [...target.children[3].children]
let LOTTERY = []

users.forEach(item => {
    let messageIndex = item.children[0].children[0].children[1].children[0].children[0].children[0].children[0].children[0].children[0].children.length - 1

    if (item.children[0].children[0].children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[messageIndex].innerText === '抽') {
        LOTTERY.push(item.children[0].children[0].children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[0].innerText)
    }
})

console.log(`獎池↓`)
LOTTERY.forEach((value, index) => console.log(`No.${index}: ${value}`))

let key = 0, rand = 0, i = 0
console.log("開獎")
while (i < 3) {
    rand = Math.round(Math.random() * (LOTTERY.length - 1))
    if (key !== rand) {
        console.log(`No.${rand} ${LOTTERY[rand]}`)
        key = rand
        i++
    }
}
