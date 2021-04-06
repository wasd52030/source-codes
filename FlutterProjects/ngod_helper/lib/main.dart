import 'package:flutter/material.dart';
import 'package:ngod_helper/random_Gnum.dart';
import 'package:ngod_helper/search_gnum.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ngod_helper', //web_title
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      routes: <String,WidgetBuilder>{
        Navigator.defaultRouteName: (context)=>MyHomePage(),
        '/rand_gnum':(context)=>RandGnum(),
        '/search_gnum':(context)=>SearchGnum()
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: AppBar( title: Text('Ngod_helper')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('random Gnum'),
              onPressed: (){
                Navigator.of(context).pushNamed('/rand_gnum');
              }
            ),
            ElevatedButton(
              child: Text('Search Gnum'),
              onPressed: (){
                Navigator.of(context).pushNamed('/search_gnum');
              }
            )
          ]
        ),
      ) 
    );
  }
}
