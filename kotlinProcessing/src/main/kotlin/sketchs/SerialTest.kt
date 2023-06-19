package sketchs

import processing.core.PApplet
import processing.serial.*

class serialTest : PApplet() {
    private lateinit var serialClient: Serial

    // size必須在settings裡面設定
    override fun settings() {
        size(200, 200)
    }

    override fun setup() {
        fill(120f, 50f, 240f)
        serialClient = Serial(this, "com1", 9600)
    }

    override fun draw() {
        if (serialClient.available() > 0) {
            val msg = serialClient.readString()

            background(255)

            if (msg.trim() == "0") {
                fill(0)
            } else {
                fill(240)
            }

            rect(10f,10f,100f,100f)
        }
    }
}