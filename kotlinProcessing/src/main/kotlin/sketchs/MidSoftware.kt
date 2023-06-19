package sketchs

import processing.core.PApplet
import processing.core.PImage
import processing.serial.Serial
import kotlin.random.Random


class midSoftware : PApplet() {
    private lateinit var serialClient: Serial

    private lateinit var hand: PImage
    private lateinit var bg: PImage

    private var gameMode = 0
    private var timer = 60
    private var score = 0

    private val dotX = listOf(75, 215, 305, 385, 445, 565, 630, 735, 795, 925).map { i -> i.toFloat() }
    private val dotY = listOf(380, 100, 70, 80, 130, 160, 100, 80, 130, 345).map { i -> i.toFloat() }

    private var dotColors = Array(10) { 0xffffff }
    private var redDotIndex = -1

    private var sensorValue = ""

    private var answers = arrayOf<Int>()
    private var display = -1


    private fun getAnswers(): Array<Int> {
        return (0 until 10).toList().shuffled().take(3).toTypedArray()
    }

    override fun mousePressed() {
        println(mouseX, mouseY)
        if (gameMode == 0) {
            // 用户在主页，检查用户是否点击了按钮
            if (mouseX in 401..599 && mouseY > 150 && mouseY < 250) {
                //記憶模式
                gameMode = 1
                display = -1
                answers = getAnswers()
                println(answers)
            } else if (mouseX in 401..599 && mouseY > 350 && mouseY < 450) {
                println("mode2！")
                // 用户点击了计时模式按钮，进入计时模式
                gameMode = 2
            }
        } else if (gameMode == 2) {
            // 用户在计时模式下，检查是否点击了返回按钮
            if (mouseX > width - 100 && mouseY < 50) {
                // 用户点击了返回按钮，切换回主页
                gameMode = 0
                timer = 60 // 重置计时器和分数
                score = 0
            }
        } else if (gameMode == 1) {
            if (mouseX > width - 100 && mouseY < 50) {
                // 用户点击了返回按钮，切换回主页
                gameMode = 0
                timer = 60 // 重置计时器和分数
                score = 0
            }
        }
    }

    // size必須在settings裡面設定
    override fun settings() {
        hand = loadImage("static/hand.jpeg")
        bg = loadImage("static/bg.jpg")
        size(bg.width, bg.height)
    }

    override fun setup() {
        val portName = Serial.list()[0]
        println(portName)
        serialClient = Serial(this, portName, 9600)
    }

    override fun draw() {
        when (gameMode) {
            0 -> {
                background(255)  // 设置背景为白色
                image(bg, 0f, 0f)  // 顯示選單背景
                // 記憶模式按鈕
                fill(0f, 200f, 0f)  // 設置按鈕顏色
                rect(400f, 150f, 200f, 100f)  // 繪製按鈕
                textSize(25f)  // 設置文字大小
                fill(255)  // 設置文字顏色
                textAlign(CENTER, CENTER)  // 設置文字對齊方式
                text("Memory MODE", (width - 20) / 2f, 195f)  // 繪製按鈕文字
                // 計時模式按鈕
                fill(200f, 0f, 0f)  // 設置按鈕顏色
                rect(400f, 350f, 200f, 100f)  // 繪製按鈕
                textSize(30f)  // 設置文字大小
                fill(255)  // 設置文字顏色
                textAlign(CENTER, CENTER)  // 設置文字對齊方式
                text("TIme MODE", (width - 20) / 2f, 402.5f)  // 繪製按鈕文字
            }
            1 -> {
                background(255)
                image(hand, 0f, 0f, bg.width.toFloat(), bg.height.toFloat())
                fill(255f, 255f, 255f)
                textSize(30f)
                textAlign(RIGHT, TOP)

                if (score == answers.size) {
                    gameMode = 0
                }

                if (redDotIndex >= 0) {
                    dotColors.map { color(255) }
                }

                for (i in dotX.indices) {
                    ellipse(dotX[i], dotY[i], 30f, 30f)
                }

                if (display != answers.size - 1) {
                    if (display > 0) {
                        fill(color(255))
                        ellipse(dotX[answers[display - 1]], dotY[answers[display - 1]], 30f, 30f)
                    }

                    display++
                    fill(color(255, 0, 0))
                    ellipse(dotX[answers[display]], dotY[answers[display]], 30f, 30f)
//                    println(display)

                    delay(3000)
                }else{
                    delay(3000)
                }


                if (serialClient.available() > 0) {
                    val ans = answers[score]
                    if (serialClient.readString().trim().toInt() - 1 == ans) {
                        dotColors[redDotIndex] = color(255, 255, 255)
                        score++
                    }

                    for (i in dotX.indices) {
                        fill(dotColors[i])
                        ellipse(dotX[i], dotY[i], 30f, 30f)
                    }
                }


                fill(255f, 0f, 0f)
                rect(width - 100f, 0f, 100f, 50f)
                fill(255)
                textAlign(CENTER, CENTER)
                text("Back", width - 50f, 25f)
            }
            2 -> {
                background(255)
                image(hand, 0f, 0f, bg.width.toFloat(), bg.height.toFloat())
                fill(255f, 255f, 255f)
                textSize(30f)
                textAlign(RIGHT, TOP)
                text("Score: $score", width - 30f, 50f)
                text("Time: $timer", width - 30f, 80f)
                if (timer == 0) {
                    gameMode = 0
                } else {
                    if (redDotIndex >= 0) {
                        dotColors.map { color(255) }
                    }

                    if (frameCount % 2 == 0) {
                        if (redDotIndex >= 0) {
                            dotColors[redDotIndex] = color(255)
                        }

                        redDotIndex = Random.nextInt(0, dotColors.size)

                        dotColors[redDotIndex] = color(255, 255, 255)
                    }

                    for (i in dotX.indices) {
                        fill(dotColors[i])
                        ellipse(dotX[i], dotY[i], 30f, 30f)
                    }

                    timer--
                    delay(1000)
                }

                fill(255f, 0f, 0f)
                rect(width - 100f, 0f, 100f, 50f)
                fill(255)
                textAlign(CENTER, CENTER)
                text("Back", width - 50f, 25f)
            }
        }
    }
}