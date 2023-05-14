import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.8.10"
    application
}

group = "me.user"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))

    // https://mvnrepository.com/artifact/org.processing/core
    implementation("org.processing:core:3.3.7")

    // https://mvnrepository.com/artifact/org.processing/serial
    implementation("org.processing:serial:3.3.7")

    //required for processing.serial
    implementation("io.github.java-native:jssc:2.9.4")
    implementation(kotlin("stdlib-jdk8"))
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

application {
    mainClass.set("MainKt")
}