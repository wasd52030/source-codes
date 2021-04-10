import 'sunset_sunrise_data_response.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiRepsone{
  Future<Map> getData() async{
    final res=await http.get(
      Uri.parse('https://api.sunrise-sunset.org/json?lat=22.62624&lng=120.2813142&date=today&formatted=0')
    );
    final dataJson=jsonDecode(res.body);
    //對從API取得的json做第一次解析
    final a=SunsetSunriseDataResponse(dataJson);
    return a.toJson();
  }
}