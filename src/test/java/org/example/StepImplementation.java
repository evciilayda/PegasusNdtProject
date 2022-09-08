package org.example;

import com.thoughtworks.gauge.Step;
import io.restassured.path.xml.XmlPath;
import io.restassured.specification.RequestSpecification;
import okhttp3.*;
import org.apache.commons.io.FileUtils;
import org.junit.jupiter.api.Assertions;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

import static io.restassured.RestAssured.given;


public class StepImplementation {

    StringBuilder sb=null;
    Response response;
    Request request=null;
    RequestSpecification httpRequest= given();
    OkHttpClient client=null;
    HashMap<String, Object> hashMap = new HashMap<String, Object>();
    HashMap<String, String> headers = new HashMap<>();


    @Step("xml olustur")
    public void xml(){
        sb=new StringBuilder();
    }

    @Step("<element> elementini xml'e ekle")
    public void xmlAddElement(String element){
        sb.append(element);
        System.out.println(element+" elementi xml'e eklendi");
    }

    @Step("<element> elementini <param> parametresiyle xml'e ekle")
    public void xmlAddElementParam(String element,String param){
        sb.append("<" + element + ">" + param + "</" + element + ">" );
        System.out.println(element+" elementi "+param+" parametresi ile xml'e eklendi");
    }

    @Step("<element> elementini hashmap'deki <param> key ile xml'e ekle")
    public void xmlAddElementHashmapToXml(String element,String param){
        sb.append("<" + element + ">" + hashMap.get(param).toString() + "</" + element + ">");
        System.out.println(element+" elementi "+param+" hashmapden xml'e eklendi");
    }

    @Step("<key> keyli <value> degeri hashmap'e ekle")
    public void addHashmapManuel(String key, String value)
    {
        hashMap.put(key, value);
        System.out.println(key + " keyli " + value + " degeri manuel olarak hashmap'e eklendi");
    }


    @Step("<url> servisine istek at")
    public void sendRequest(String url) throws Exception {
        client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("text/xml;charset=UTF-8;");
        RequestBody body = RequestBody.create(mediaType, hashMap.get("data").toString());
        request = new Request.Builder()
                .url(url)
                .method("POST", body)
                .headers(Headers.of(headers))
                .build();
        response = client.newCall(request).execute();
        System.out.println("RequestBody: "+hashMap.get("data").toString());
        System.out.println("Response: "+response.peekBody(Long.MAX_VALUE).string());
        System.out.println("-------------------------------------------------------");

    }


    @Step("Hashmapin icindeki <hashmapKey> keyinin degeri <hashmapKey2> keyinin degeri ile <type> mı kontrol et")
    public void checkDifferenceHashmap(String hashmapKey, String hashmapKey1, String type)
    {
        if ("aynı".equals(type))
        {
            Assertions.assertEquals(hashMap.get(hashmapKey).toString(), hashMap.get(hashmapKey1).toString(), "hashmapteki degerler eslesiyor...");
            System.out.println(hashMap.get(hashmapKey).toString()+" , "+ hashMap.get(hashmapKey1).toString() + " ile " + type + "mi kontrol edildi");
        }
        else if ("farklı".equals(type))
        {
            Assertions.assertNotEquals(hashMap.get(hashmapKey).toString(), hashMap.get(hashmapKey1).toString(), "hashmapteki degerler eslesmiyor...");
            System.out.println(hashMap.get(hashmapKey).toString()+" , "+ hashMap.get(hashmapKey1).toString() + " ile " + type + " mi kontrol edildi");
        }
        else
        {
            Assertions.fail("Lütfen Gecerli bir tip giriniz");
        }
    }

    @Step("xml <yol> xpathinindeki elementi <element> keyiyle hashmape ekle")
    public void xpath(String yol,String element) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
       // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> hashMap.put(element,o.toString()));
        System.out.println("HASHMAPE EKLENDİ : " +hashMap.get(element));
    }

    @Step("hashmapteki <offerId> offerId ve <responseId> responseId elementlerini xml'e ekle")
    public void xmlAddElementHashmapToOffer(String offerId,String responseId){
        sb.append("<Offer OfferID="+ hashMap.get(offerId).toString() + "Owner=\"PC\" ResponseID=" +  hashMap.get(offerId).toString() + ">");
        System.out.println("OfferID: "+hashMap.get(offerId).toString()+" ve"+" ResponseID: "+ hashMap.get(responseId).toString()+" hashmapten xml'e eklendi");
    }


    @Step("<key> key <value> value degerini headera ekle")
    public void addHeader(String key, String value)
    {
        headers.put(key,value);
        System.out.println("Header'a " +key+ "," +value+ " degeri eklendi");
    }


    @Step("<text> requesti olustur")
    public void requestCreate(String text){
        try {
            File myObj = new File("src/main/resources/"+text+".text");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                hashMap.put("data",data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }


    @Step("<text> requestine hashmapdeki <offerId> ve <responseId> degerlerini ekle")
    public void addParamRequest(String text,String offerId,String responseId) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            String data = FileUtils.readFileToString(textFile);
            data = data.replace("replaceOffer",hashMap.get(offerId).toString());
            data = data.replace("replaceResponse",hashMap.get(responseId).toString());
            hashMap.put("data",data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine hashmapdeki <orderId> ve <simpleCurrencyPrice> degerlerini eklee")
    public void addOrderIdprice(String text,String orderId, String simpleCurrencyPrice) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
           // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace("replaceOrder",hashMap.get(orderId).toString());
            data = data.replace("replaceAmount",hashMap.get(simpleCurrencyPrice).toString());
            hashMap.put("data",data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Step("xml <yol> xpathinindeki elementi <value> degeriyle karsilastir")
    public void xpathResponseKarsilastir(String yol,String value) throws IOException {
        StringBuilder gelenEleman = new StringBuilder();
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
        // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> gelenEleman.append(o.toString()));

        System.out.println("Gelen Eleman: "+gelenEleman);

        Assertions.assertEquals(value,gelenEleman.toString(),"Degerler eslesmiyor!..");
        System.out.println(value +" degeri " + gelenEleman.toString() + " ile ayni mi kontrol edildi....");
    }

    @Step("xml <yol> xpathinindeki elementi <key> keyli deger ile karsilastir")
    public void xpathResponseHashmapKarsilastir(String yol,String key) throws IOException {
        StringBuilder gelenEleman = new StringBuilder();
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
        // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> gelenEleman.append(o.toString()));

        System.out.println("Gelen Eleman: "+gelenEleman);

        Assertions.assertEquals(hashMap.get(key),gelenEleman.toString(),"Degerler eslesmiyor!..");
        System.out.println(hashMap.get(key) +" hashmapden gelen degeri " + gelenEleman + " ile ayni mi kontrol edildi....");
    }






}

