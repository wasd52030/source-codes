interface q { order: number, msg: string, name: string, value: string }

class ConversationEntity {
    state = true
    questionStep = 1
    questionAndAnswers: Array<q> = []
    responseHandler: (msg: string) => void
    resultHandler: (questions: Array<q>) => void

    start() {
        this.state = true
        this.responseHandler(this.questionAndAnswers.filter(q => q.order === this.questionStep)[0].msg)
    }

    end() { this.state = false }


    reply(msg: string) {
        if (this.state) {
            if (this.questionStep === this.questionAndAnswers.length) {
                this.questionAndAnswers.filter(q => q.order === this.questionStep)[0].value = msg

                this.end()

                this.resultHandler(this.questionAndAnswers)
            } else {
                this.questionAndAnswers.filter(q => q.order === this.questionStep)[0].value = msg
                this.questionStep++
                this.responseHandler(this.questionAndAnswers.filter(q => q.order === this.questionStep)[0].msg)
            }
        } else {
            throw "this conversation is done！"
        }
    }
}

function Question(order: number, msg: string) {

    if (order < 1) {
        throw "order must greater then 0！"
    }

    return (target: any, propertyName: string) => {
        let value: string;
        Object.defineProperty(target, propertyName, {
            get: function () {
                return value;
            },
            set: function (newVal: string) {
                let questions: Array<q> = this["questionAndAnswers"];
                if (questions.filter(item => order == item.order).length == 0) {
                    questions.push({ order, msg, name: propertyName, value: newVal })
                }
            }
        })
    }
}


class A extends ConversationEntity {

    lineid = ''

    @Question(1, "abc")
    a = "1"

    @Question(2, "def")
    b = "qwe"

    @Question(3, "rrr")
    c = "qwzxc"

    @Question(4, "asdasdqwr")
    d = "zczxczxc"

    constructor(lineid: string) {
        super()
        this.lineid = lineid
    }
}


let w = new A("qweasd")
w.responseHandler = (msg: string) => console.log(msg)
w.resultHandler = (questions: Array<q>) => {
    let res = questions.reduce((past, curr) => {
        return Object.assign(past, { [curr.name]: curr.value })
    }, {})
    console.log(res)
}

console.log(`lineid: ${w.lineid}`)
w.start()
w.reply("abc")
w.reply("tqt")
w.reply("twt")
w.reply("twtp")
