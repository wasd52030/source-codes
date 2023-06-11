import SimpleOpenNI.SimpleOpenNI
import processing.core.PApplet
import processing.core.PImage
import processing.core.PVector





class openNI : PApplet() {

    private lateinit var kinect: SimpleOpenNI

    override fun settings() {
        size(1280, 480)
    }

    override fun setup() {
        kinect = SimpleOpenNI(this)

        kinect.enableDepth()
        kinect.enableRGB()
        kinect.enableUser()
        kinect.enableHand()
    }

    override fun draw() {
        kinect.update()
        image(kinect.depthImage(), 0f, 0f)
        image(kinect.rgbImage(), 640f, 0f)

        // 獲取手的位置
        val userList = kinect.getUsers()
        println(userList.size)
        if (userList.isNotEmpty()) {
            val userId = userList[0]

            // 獲取手部的關節座標
            val leftHandPos = PVector()
            val rightHandPos = PVector()
            kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_HAND, leftHandPos)
            kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_HAND, rightHandPos)

            // 將關節座標轉換為彩色影像座標
            val leftHandPosColor = PVector()
            val rightHandPosColor = PVector()
            kinect.convertRealWorldToProjective(leftHandPos, leftHandPosColor)
            kinect.convertRealWorldToProjective(rightHandPos, rightHandPosColor)

            // 將手的位置轉換為數字並讀取出來
            val leftHandX = leftHandPosColor.x.toInt()
            val leftHandY = leftHandPosColor.y.toInt()
            val rightHandX = rightHandPosColor.x.toInt()
            val rightHandY = rightHandPosColor.y.toInt()
            println("Left Hand Position: ($leftHandX, $leftHandY)")
            println("Right Hand Position: ($rightHandX, $rightHandY)")
        }
    }
}