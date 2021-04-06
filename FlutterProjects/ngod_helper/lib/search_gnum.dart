import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class SearchGnum extends StatefulWidget {
  @override
  _SearchGnumState createState() => _SearchGnumState();
}

class _SearchGnumState extends State<SearchGnum> {

  TextEditingController Textbox1=TextEditingController();
  var numstr='';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Search Gnum')),
      body: Center(
        child: Column(
          children: [
            Row(
              children: [
                Text("輸入欲查詢之車號: ",style: TextStyle(fontSize: 20)),
                Expanded(
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: Textbox1
                  )
                )
              ],
            ),
            ElevatedButton(
              child: Text("查詢"),
              onPressed:(){
                setState(() {
                  numstr=Textbox1.text;
                });
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context)=>Result(num: numstr))
                );
              }
            )
          ]
        )

      )
    );
  }
}


class Result extends StatelessWidget {
  Result({Key key,this.num}):super(key: key);
  final String num;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('result of $num')),
      body: WebView(
        initialUrl: 'https://nhentai.net/g/$num',
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}