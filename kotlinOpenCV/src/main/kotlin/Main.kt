import nu.pattern.OpenCV
import org.opencv.core.CvType
import org.opencv.core.Mat
import org.opencv.core.Size
import org.opencv.highgui.HighGui.*
import org.opencv.imgcodecs.Imgcodecs.*
import org.opencv.imgproc.Imgproc.*

fun main(args: Array<String>) {
    println("Hello World!")

    // reference -> https://stackoverflow.com/questions/18625948/opencv-java-unsatisfiedlinkerror
    OpenCV.loadLocally()

    val image = imread("static/frenZoltraak.jpeg")

    // scale image
    var scaledImage = Mat()
    resize(image, scaledImage, Size(500.toDouble(), 400.toDouble()))

    // get gray scale image with scaled image
    var grayImage = Mat(image.rows(), image.cols(),CvType.CV_8SC1)
    cvtColor(image,grayImage, COLOR_RGB2GRAY)

    imwrite("static/frenZoltraak_Gray.jpeg",grayImage)
}