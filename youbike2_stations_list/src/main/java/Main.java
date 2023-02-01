import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.FileWriter;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        final OkHttpClient client = new OkHttpClient();
        Request req = new Request.Builder()
                .url("https://www.youbike.com.tw/region/main/stations/list/")
                .build();


        try (Response res = client.newCall(req).execute()) {
            String html = res.body().string();
            Document website = Jsoup.parse(html);
            Elements JsonSource = website.select("#__NEXT_DATA__");
            Elements cityOption = website.select("#stations-select-area");
            Map<String, String> citys = new HashMap<>();
            for (Element city : cityOption.get(0).children()) {
                if (!city.val().equals("")) {
                    citys.put(city.val(), city.html());
                }
            }

            JsonObject data = JsonParser.parseString(JsonSource.html()).getAsJsonObject();
            JsonObject pageProps = data.get("props").getAsJsonObject().get("pageProps").getAsJsonObject();
            JsonArray yb2 = pageProps.get("jsonYb2").getAsJsonArray();
            try (FileWriter file = new FileWriter("YouBike2.0_站點列表.txt")) {
                for (JsonElement item : yb2) {
                    JsonObject station = item.getAsJsonObject();
                    JsonObject available = station.get("available_spaces_detail").getAsJsonObject();

                    String city = citys.get(station.get("area_code").getAsString());
                    String district = station.get("district_tw").getAsString();
                    String address = station.get("address_tw").getAsString();

                    file.write(String.format("地區: %s\n", city));
                    file.write(String.format("站名: %s\n", station.get("name_tw").getAsString()));
                    file.write(String.format("所在地: %s\n", district + address));
                    file.write(String.format("可借數量: %s\n", available.get("yb2").getAsString()));
                    file.write(String.format("空位: %s\n", station.get("empty_spaces").getAsString()));
                    file.write("\n");
                    file.flush();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            System.out.println("Task Success!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}