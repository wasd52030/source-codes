import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
import org.jetbrains.kotlin.ir.backend.js.compile

plugins {
    kotlin("jvm") version "1.8.10"
    application
}

group = "me.user"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    mavenLocal()
    maven {
        url = uri("https://repo.clojars.org")
        name = "Clojars"
    }
}

dependencies {
    testImplementation(kotlin("test"))

    // https://mvnrepository.com/artifact/org.processing/core
    implementation("org.processing:core:3.3.7")

    // https://mvnrepository.com/artifact/org.processing/serial
    implementation("org.processing:serial:3.3.7")

    // https://mvnrepository.com/artifact/ddf.minim/ddf.minim
//    implementation("ddf.minim:ddf.minim:2.2.0")


    //required for processing.serial
    implementation("io.github.java-native:jssc:2.9.4")
    implementation(kotlin("stdlib-jdk8"))

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.1")

    // reference: https://stackoverflow.com/questions/54166069/how-do-you-add-local-jar-file-dependency-to-build-gradle-kt-file
    implementation(fileTree(mapOf("dir" to "lib/SimpleOpenNI/library", "include" to listOf("*.jar"))))
}

application {
    mainClass.set("MainKt")
}

// reference https://www.jetbrains.com/help/idea/create-your-first-kotlin-app.html#run-the-jar
tasks.jar {
    manifest {
        attributes["Main-Class"] = "MainKt"
    }
    configurations["compileClasspath"].forEach { file: File ->
        from(zipTree(file.absoluteFile))
    }
    duplicatesStrategy = DuplicatesStrategy.INCLUDE
}

tasks.test {
    useJUnitPlatform()
}

tasks.withType<KotlinCompile> {
//    kotlinOptions.jvmTarget = "1.8"
    kotlinOptions.jvmTarget = "11"
}