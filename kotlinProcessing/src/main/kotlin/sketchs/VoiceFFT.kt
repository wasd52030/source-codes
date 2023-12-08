package sketchs

import processing.core.PApplet
import processing.sound.FFT
import processing.sound.SoundFile

class VoiceFFT : PApplet() {

    private val bands = 128
    private var sum = FloatArray(bands)
    private var smoothingFactor = 0.2f
    private var barWidth = 0f
    private val scale = 5
    private val w = 6

    private val IskraSvobody = SoundFile(this, "static/Искра свободы.aif")
    private val FFT = FFT(this, bands)

    override fun settings() {
        size(300, 300)
    }

    override fun setup() {
        barWidth = width / bands.toFloat();

        IskraSvobody.loop()

        FFT.input(IskraSvobody)
    }

    override fun draw() {

        background(0f, 0f, 0f)
        noStroke()

        FFT.analyze()

        for (i in 0 until FFT.spectrum.size) {
            // Smooth the FFT spectrum data by smoothing factor
            sum[i] += (FFT.spectrum[i] - sum[i]) * smoothingFactor

            val amplitude = (sum[i] * height * scale) * 10
            fill(255f, 255 - amplitude, amplitude)
            // kotlin.io.println(amplitude)

            val x = map(i.toFloat(), 0f, FFT.spectrum.size.toFloat(), 0f, width.toFloat())
            val y = height * 0.85 - map(amplitude, 0f, 255f, 0f, height / 2f)
            rect(x, y.toFloat(), w.toFloat(), w / 2f)
        }
    }
}