import 'dart:math';

import 'package:webview_flutter/webview_flutter.dart';
import 'package:flutter/material.dart';


class RandGnum extends StatefulWidget {
  @override
  _RandGnumState createState() => _RandGnumState();
}

class _RandGnumState extends State<RandGnum> {

  var n=0;
  void GetGnum()
  {
    setState((){
      n=Random().nextInt(999999);
    });
  }

  @override
  void initState() 
  {
    super.initState();
    GetGnum();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Gnum ===> $n')),
      body: WebView(
        initialUrl: 'https://nhentai.net/g/$n',
      )
    );
  }
}