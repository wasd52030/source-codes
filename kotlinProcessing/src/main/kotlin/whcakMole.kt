import processing.core.PApplet
import kotlin.random.Random

data class Button(
    val width: Float,
    val height: Float,
    var posX: Float,
    var posY: Float,
    var color: Int,
    var text: String,
    var textSize: Float,
    var textColor: Int = 255,
)


enum class GameState {
    Start,
    Gaming,
    Done
}

class whcakMole : PApplet() {

    private var initBtn = Button(200f, 150f, 250f, 250f, color(150, 160, 170), "Start", 20f)
    private var backBtn = Button(100f, 45f, 700f, 0f, color(255, 0, 0), "Back", 20f)
    private var state = GameState.Start
    private var Timer = 0
    private var Moles = arrayOf<Int>()
    private var level = 0
    private var score = 0
    private var msgs = arrayOf("", "", "")
    private var btns = mutableListOf<Button>()

    private fun setLevelData(n: Int): Array<Int> {
        return btns.indices.shuffled().take(n).toTypedArray()
    }

    override fun mousePressed() {
        if (state == GameState.Start) {
            if (mouseX in initBtn.posX.toInt()..(initBtn.posX + initBtn.width).toInt() && mouseY > initBtn.posY.toInt() && mouseY < (initBtn.posY + initBtn.height).toInt()) {
                state = GameState.Gaming
            }
        } else if (state == GameState.Gaming) {
            if (mouseX in backBtn.posX.toInt()..(backBtn.posX + backBtn.width).toInt() && mouseY > backBtn.posY.toInt() && mouseY < (backBtn.posY + backBtn.height).toInt()) {
                state = GameState.Start
            }

            btns.forEach { button ->
                if (mouseX in button.posX.toInt()..(button.posX + button.width).toInt() && mouseY > button.posY.toInt() && mouseY < (button.posY + button.height).toInt()) {
                    if (button.text == "X") {
                        score++
                        button.text = ""
                    }
                }
            }
        } else if (state == GameState.Done) {
            if (mouseX in backBtn.posX.toInt()..(backBtn.posX + backBtn.width).toInt() && mouseY > backBtn.posY.toInt() && mouseY < (backBtn.posY + backBtn.height).toInt()) {
                state = GameState.Start
            }
        }
    }

    override fun settings() {
        size(800, 700)
    }


    override fun setup() {
        initBtn.posX = (width - initBtn.width) / 2
        initBtn.posY = (height - initBtn.height) / 2

        for (i in 0 until 10) {
            for (j in 0 until 10) {
                btns.add(Button(50f, 50f, 100f + (60 * i), 70f + (60 * j), color(150, 160, 170), "", 20f))
            }
        }

        val font = createFont("標楷體", 14f)
        textFont(font)
    }

    override fun draw() {
        when (state) {
            GameState.Start -> {
                level = 0
                Timer = 0
                score = 0

                background(0x03e8fc)
                fill(initBtn.color)
                rect(initBtn.posX, initBtn.posY, initBtn.width, initBtn.height)
                textSize(initBtn.textSize)
                fill(initBtn.textColor)
                textAlign(CENTER, CENTER)
                text(initBtn.text, initBtn.posX + (initBtn.width / 2), initBtn.posY + (initBtn.height / 2))
            }
            GameState.Gaming -> {
                background(0x198964)

                if (Timer == 60) {
                    msgs[2] = "遊戲結束！"
                    state = GameState.Done
                } else if (Timer % 20 == 0) {
                    level++
                    var temp = Random.nextInt(5, 11)
                    Moles = setLevelData(temp)
                    btns.forEach { i -> i.text = "" }
                    for (i in Moles) {
                        btns[i].text = "X"
                    }
                    msgs[2] = "共有${Moles.size}隻地鼠"
                }
                Timer++

                msgs[0] = "現在是第${level}關，共${score}分"
                msgs[1] = "${Timer / 4}秒"

                fill(backBtn.color)
                rect(backBtn.posX, backBtn.posY, backBtn.width, backBtn.height)
                textSize(backBtn.textSize)
                fill(backBtn.textColor)
                textAlign(CENTER, CENTER)
                text(backBtn.text, backBtn.posX + (backBtn.width / 2), backBtn.posY + (backBtn.height / 2))

                msgs.forEachIndexed { index, item ->
                    fill(color(255))
                    textAlign(CENTER, CENTER)
                    text(item, width / 2f, 10f + (20 * index))
                }

                btns.forEach { btn ->
                    fill(btn.color)
                    rect(btn.posX, btn.posY, btn.width, btn.height)
                    textSize(btn.textSize)
                    fill(btn.textColor)
                    textAlign(CENTER, CENTER)
                    text(btn.text, btn.posX + (btn.width / 2), btn.posY + (btn.height / 2))
                }

                delay(250)
            }
            GameState.Done -> {}
        }
    }
}