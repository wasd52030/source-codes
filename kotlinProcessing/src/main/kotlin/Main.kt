// Processing要求使用弧度表示一個角
// 如果計算時用的是角度，最後畫圖時需用「radians」函數轉成弧度

import processing.core.PApplet
import processing.core.PVector

class processingPlayground : PApplet() {

    private val Width = 300
    private val Height = 300

    private val r = 25f

    private val halfW = Width / 2
    private val halfH = Height / 2

    private lateinit var center: PVector   // 圓心
    private lateinit var velocity: PVector // 速度

    override fun settings() {
        size(Width, Height)
    }

    override fun setup() {
        center = PVector(1f, 3f)
        velocity = PVector(4f, 3f)
    }

    override fun draw() {
        background(255f, 0f, 0f)

        val next = PVector.add(center, velocity)

        if (next.x + r > halfW || next.x - r < -halfW) {
            velocity.x *= -1  // 調換速度向量的 x 方向
        }

        if (next.y + r > halfH || next.y - r < -halfH) {
            velocity.y *= -1  // 調換速度向量的 y 方向
        }

        center.add(velocity.x, velocity.y)

        translate(width / 2f, height / 2f)
        ellipse(center.x, center.y, r * 2, r * 2)
    }
}

//YourClass::class.java.name
fun main() {
    PApplet.main(processingPlayground::class.java.name)
}