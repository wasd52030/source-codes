import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: homepage(),
      routes: <String,WidgetBuilder>{
        '/s2':(context)=>second_widget()
      }
    );
  }
}

class homepage extends StatefulWidget {
  @override
  _homepageState createState() => _homepageState();
}

class _homepageState extends State<homepage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          children: [
            Text('aaaa'),
                ElevatedButton(
                  child: Text('dsad'),
                  onPressed: (){
                    Navigator.of(context).pushNamed('/s2');
                  })
          ],
        )
      ),
    );
  }
}

class second_widget extends StatefulWidget {
  const second_widget({
    Key key,
  }) : super(key: key);

  @override
  _second_widgetState createState() => _second_widgetState();
}

class _second_widgetState extends State<second_widget> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          children: [
            Text('bbbb'),
                ElevatedButton(
                  child: Text('bbcd'),
                  onPressed: (){
                    Navigator.pop(context);
                  } )
          ],
        ),
      )
    );
  }
}