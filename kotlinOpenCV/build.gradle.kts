plugins {
    kotlin("jvm") version "1.9.21"
    application
}

group = "org.sohai"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))

    implementation("org.openpnp:opencv:4.6.0-0")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(11)
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


    doLast {
        println("copying static files...")
        copy {
            from(fileTree("$projectDir/static"))
            into("$buildDir/libs/static")
        }
    }
}