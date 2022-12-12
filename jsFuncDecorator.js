function funcTimer(func) {
    return async function () {
        const t1 = new Date()
        let result = await func.apply(this, arguments)
        const t2 = new Date();
        console.log(`cost ${t2.getUTCMilliseconds() - t1.getUTCMilliseconds()}ms`)
        return result
    }
}


//reference -> https://blog.darkthread.net/blog/find-repeated-item-group/
function* FindRepeatItemGroups(list, areEqual) {
    if (list !== undefined && list !== null) {
        f = [list[0]]
        for (let item of list.slice(1)) {
            if (areEqual(f.slice(-1)[0], item)) {
                f.push(item)
            } else {
                if (f.length > 1) {
                    yield f
                }
                f = [item]
            }
        }
        if (f.length > 1) {
            yield f
        }
    }
}

function main() {
    let raw = "A,B,B,C,X,C,C,B,B,D,D,D".split(",")
    let items = raw.map((item, index) => ({ 'id': index + 1, 'code': item }))
    console.log(items.map((item, index) => '\033[37m' + `${item.id}.` + '\033[33m' + `${item.code}`).join(' '))
    for (let grp of FindRepeatItemGroups(items, (a, b) => a.code === b.code)) {
        console.log(`Group of ${grp[0]['code']}：${grp.map(item => item.id).join(',')}`)
    }
    console.log('\033[1;37m')
}

funcTimer(main)()

