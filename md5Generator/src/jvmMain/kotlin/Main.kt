import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalClipboardManager
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import com.google.common.hash.Hashing
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch


@Composable
@Preview
fun App() {
    var u by remember { mutableStateOf("") }
    var md5 by remember { mutableStateOf("") }

    val clipboardManager = LocalClipboardManager.current

    val snackScaffoldState = rememberScaffoldState()

    Scaffold(scaffoldState = snackScaffoldState) {
        Column(modifier = Modifier.padding(10.dp).fillMaxSize()) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("enter some word")
                TextField(u, {
                    u = it
                }, modifier = Modifier.padding(2.dp))
            }
            Text(
                if (u == "") {
                    val text = "TextField is empty"
                    md5 = text
                    text
                } else {
                    val res = Hashing.md5().hashString(u, Charsets.UTF_8).toString()
                    md5 = res
                    "md5 result -> $res"
                }, modifier = Modifier.padding(0.dp, 10.dp)
            )
            Button({
                clipboardManager.setText(AnnotatedString(md5))

                GlobalScope.launch {
                    snackScaffoldState.snackbarHostState.showSnackbar(
                        "已複製",
                        "",
                        SnackbarDuration.Short
                    )
                }
            }, modifier = Modifier.padding(0.dp, 15.dp)) {
                Text("copy MD5")
            }
        }
    }
}

fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "MD5 Generator",
    ) {
        App()
    }
}
