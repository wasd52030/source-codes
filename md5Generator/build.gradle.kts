import org.jetbrains.compose.desktop.application.dsl.TargetFormat

plugins {
    kotlin("multiplatform")
    id("org.jetbrains.compose")
}

group = "ltd.haiyaa"
version = "1.0-SNAPSHOT"

repositories {
    google()
    mavenCentral()
    maven("https://maven.pkg.jetbrains.space/public/p/compose/dev")
}

kotlin {
    jvm {
        jvmToolchain(17)
        withJava()


    }
    sourceSets {
        val jvmMain by getting {
            dependencies {
                implementation(compose.desktop.currentOs)
                implementation("com.google.guava:guava:32.1.2-jre")
            }
        }
        val jvmTest by getting
    }
}



compose.desktop {
    application {
        mainClass = "MainKt"
        nativeDistributions {
            targetFormats(TargetFormat.Dmg, TargetFormat.Msi, TargetFormat.Deb)
            packageName = "md5Generator"
            packageVersion = "1.0.0"

            windows {
                // a version for all Windows distributables
                packageVersion
                // a version only for the msi package
                msiPackageVersion = "1.0.0"
                // a version only for the exe package
                exePackageVersion = "1.0.0"
            }
        }
    }
}
