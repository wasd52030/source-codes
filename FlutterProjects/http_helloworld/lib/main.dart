import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      routes: <String,WidgetBuilder>{
        Navigator.defaultRouteName: (context)=>MainPage(),
        '/a':(context)=>HttpResultPage()
      },
    );
  }
}


class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('http demo'),
      ),
      body: Center(
        child: ElevatedButton(
            child:Text('a'),
          onPressed: (){
            Navigator.of(context).pushNamed('/a');
          }
        ),
      )
    );
  }
}


class HttpResultPage extends StatefulWidget {
  @override
  _HttpResultPageState createState() => _HttpResultPageState();
}

class _HttpResultPageState extends State<HttpResultPage> {

  var k='';

  void getdata() async
  {
    var url=Uri.parse('https://google.com');
    var repsone=await http.get(url);
    setState(() {
          k=repsone.body;
      }
    );
  }

  @override
  void initState() 
  {
    super.initState();
    getdata();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('result'),
      ),
      body: Center(
        child: Text('$k')
      ),
    );
  }
}


