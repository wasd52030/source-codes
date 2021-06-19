import "dart:convert";
import "package:flutter/material.dart";
import "package:dio/dio.dart";
import "package:sprintf/sprintf.dart";

void main() {
  runApp(App());
}

class App extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Exchange Rate Converter",
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ExchangeRateConverter(title: "簡易匯率換算器"),
      debugShowCheckedModeBanner: false,
    );
  }
}

class ExchangeRateConverter extends StatefulWidget {
  ExchangeRateConverter({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _ExchangeRateConverterState createState() => _ExchangeRateConverterState();
}

class _ExchangeRateConverterState extends State<ExchangeRateConverter> {
  List<DropdownMenuItem<String>> ratelist;
  String comb1Value, comb2Value, changeResult = "";
  TextEditingController textbox1 = TextEditingController();

  @override
  void initState() {
    super.initState();
    setcombolst();
    textbox1.text = "0";
  }

  List<DropdownMenuItem<String>> setcomboItems(List<String> data) {
    List<DropdownMenuItem<String>> items = [];
    for (String rate in data) {
      items.add(new DropdownMenuItem(
          value: rate, child: new Text(rate, style: TextStyle(fontSize: 20))));
    }
    return items;
  }

  Future<Map> _getdata() async {
    final res = await Dio().get("https://tw.rter.info/capi.php");
    Map datajson = json.decode(res.data);
    return datajson;
  }

  void setcombolst() async {
    List<String> combolst = [];
    final d = await _getdata();
    d.forEach((k, v) {
      String x = k;
      RegExp reg = RegExp("USD.*");
      if (reg.hasMatch(x)) {
        final n = x.substring(3, x.length);
        if (n != "") {
          combolst.add(n);
        }
      }
    });
    combolst.sort();
    ratelist = setcomboItems(combolst);
    comb1Value = ratelist[0].value;
    comb2Value = ratelist[1].value;
    setState(() {});
  }

  void exchange(String text) async {
    double a = double.parse(textbox1.text);
    final d = await _getdata();

    if (comb2Value == "USD") {
      a /= d["USD$comb1Value"]["Exrate"];
    } else {
      a /= d["USD$comb1Value"]["Exrate"];
      a *= d["USD$comb2Value"]["Exrate"];
    }

    setState(() {
      changeResult = textbox1.text != ""
          ? sprintf("${textbox1.text} $comb1Value = %0.4f $comb2Value", [a])
          : sprintf("1 $comb1Value = %0.4f $comb2Value", [a]);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: [
          IconButton(
              icon: Icon(Icons.info_outlined),
              onPressed: () => showDialog(
                  context: context,
                  builder: (context) => AlertDialog(
                          title: Row(
                            children: [
                              Icon(Icons.info_outline),
                              Text("關於此app")
                            ],
                          ),
                          content: Text("資料來源：https://tw.rter.info/capi.php"),
                          actions: [
                            ElevatedButton(
                                child: Text('ok'),
                                onPressed: () {
                                  Navigator.of(context, rootNavigator: true)
                                      .pop();
                                })
                          ])))
        ],
      ),
      body: Center(
        child: Column(
          children: [
            TextField(
              decoration: InputDecoration(labelText: "將"),
              keyboardType: TextInputType.number,
              controller: textbox1,
              onChanged: exchange,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text("自", style: TextStyle(fontSize: 20)),
                Padding(
                  padding: const EdgeInsets.all(25.0),
                  child: DropdownButton(
                    items: ratelist,
                    value: comb1Value,
                    onChanged: (String selected) {
                      setState(() {
                        comb1Value = selected;
                      });
                      exchange("");
                    },
                  ),
                )
              ],
            ),
            ElevatedButton(
                onPressed: () {
                  setState(() {
                    String temp = comb1Value;
                    comb1Value = comb2Value;
                    comb2Value = temp;
                  });
                  exchange("");
                },
                child: Text("⇅", style: TextStyle(fontSize: 20))),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text("轉換成", style: TextStyle(fontSize: 20)),
                Padding(
                  padding: const EdgeInsets.all(25.0),
                  child: DropdownButton(
                    items: ratelist,
                    value: comb2Value,
                    onChanged: (String selected) {
                      setState(() {
                        comb2Value = selected;
                      });
                      exchange("");
                    },
                  ),
                )
              ],
            ),
            Text(changeResult, style: TextStyle(fontSize: 20))
          ],
        ),
      ),
    );
  }
}
