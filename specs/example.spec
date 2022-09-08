Deneme Gauge
=====================

Deneme soap
---------------------------
* xml olustur
* "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:tem=\"http://tempuri.org/\">" elementini xml'e ekle
* "<soap:Header/>" elementini xml'e ekle
* "<soap:Body>" elementini xml'e ekle
* "<tem:Add>" elementini xml'e ekle
* "tem:intA" elementini "13" parametresiyle xml'e ekle
* "tem:intB" elementini "20" parametresiyle xml'e ekle
* "</tem:Add>" elementini xml'e ekle
* "</soap:Body>" elementini xml'e ekle
* "</soap:Envelope>" elementini xml'e ekle
* "http://www.dneonline.com/calculator.asmx" servisine istek at
* XMl response'da "AddResult" elementi "33" ile ayni mi kontrol et

deneme1
------------------------
* "http://www.dneonline.com/calculator.asmx" servisine istek at


Pegasus Deneme
------------------------
tags: pegasusfirst
* "StatusCode" keyli "OP" degeri hashmap'e ekle
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "doAirOWT1" requesti olustur
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.AirShoppingRS.ShoppingResponseID.ResponseID.text()" xpathinindeki elementi "responseId" keyiyle hashmape ekle
* xml "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[0].@OfferID.text()" xpathinindeki elementi "offerId" keyiyle hashmape ekle
* xml "Envelope.Body.AirShoppingRS.Document.Name.text()" xpathinindeki elementi "PC NDC GATEWAY" degeriyle karsilastir
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "doOrderCreateOWT1" requestine hashmapdeki "offerId" ve "responseId" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.Status.StatusCode.text()" xpathinindeki elementi "StatusCode" keyli deger ile karsilastir



deneme2
------------------------
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "doAirOWT1" requesti olustur
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.AirShoppingRS.ShoppingResponseID.ResponseID.text()" xpathinindeki elementi "responseId" keyiyle hashmape ekle
* xml "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[0].@OfferID.text()" xpathinindeki elementi "offerId" keyiyle hashmape ekle
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "doOrderCreateOWT1" requestine hashmapdeki "offerId" ve "responseId" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at




Deneme Text
---------------------------
* xml olustur
* "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:hel=\"http://learnwebservices.com/services/hello\">" elementini xml'e ekle
* "<soapenv:Header/>" elementini xml'e ekle
* "<soapenv:Body>" elementini xml'e ekle
* "<hel:SayHello>" elementini xml'e ekle
* "<hel:HelloRequest>" elementini xml'e ekle
* "hel:Name" elementini "Emre Karadeniz" parametresiyle xml'e ekle
* "</hel:HelloRequest>" elementini xml'e ekle
* "</hel:SayHello>" elementini xml'e ekle
* "</soapenv:Body>" elementini xml'e ekle
* "</soapenv:Envelope>" elementini xml'e ekle
* "http://www.learnwebservices.com/services/hello" servisine istek at
* XMl response'da "Message" elementi "Hello Emre Karadeniz!" ile ayni mi kontrol et


Deneme Hashmap
---------------------------
* "emre" keyli "36" degeri hashmap'e ekle
* xml olustur
* "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:tem=\"http://tempuri.org/\">" elementini xml'e ekle
* "<soap:Header/>" elementini xml'e ekle
* "<soap:Body>" elementini xml'e ekle
* "<tem:Add>" elementini xml'e ekle
* "tem:intA" elementini "13" parametresiyle xml'e ekle
* "tem:intB" elementini hashmap'deki "emre" key ile xml'e ekle
* "</tem:Add>" elementini xml'e ekle
* "</soap:Body>" elementini xml'e ekle
* "</soap:Envelope>" elementini xml'e ekle
* "http://www.dneonline.com/calculator.asmx" servisine istek at
* XMl response'da "AddResult" elementi "49" ile ayni mi kontrol et

Deneme Response Hashmap
---------------------------
* "emre" keyli "36" degeri hashmap'e ekle
* xml olustur
* "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:tem=\"http://tempuri.org/\">" elementini xml'e ekle
* "<soap:Header/>" elementini xml'e ekle
* "<soap:Body>" elementini xml'e ekle
* "<tem:Add>" elementini xml'e ekle
* "tem:intA" elementini "13" parametresiyle xml'e ekle
* "tem:intB" elementini hashmap'deki "emre" key ile xml'e ekle
* "</tem:Add>" elementini xml'e ekle
* "</soap:Body>" elementini xml'e ekle
* "</soap:Envelope>" elementini xml'e ekle
* "http://www.dneonline.com/calculator.asmx" servisine istek at
* XMl response'da "AddResult" elementi "49" ile ayni mi kontrol et
* XMl response'da "AddResult" elementini "emreResponse" keyi ile hashmap'e ekle
* xml olustur
* "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:tem=\"http://tempuri.org/\">" elementini xml'e ekle
* "<soap:Header/>" elementini xml'e ekle
* "<soap:Body>" elementini xml'e ekle
* "<tem:Add>" elementini xml'e ekle
* "tem:intA" elementini "11" parametresiyle xml'e ekle
* "tem:intB" elementini hashmap'deki "emreResponse" key ile xml'e ekle
* "</tem:Add>" elementini xml'e ekle
* "</soap:Body>" elementini xml'e ekle
* "</soap:Envelope>" elementini xml'e ekle
* "http://www.dneonline.com/calculator.asmx" servisine istek at
* XMl response'da "AddResult" elementi "60" ile ayni mi kontrol et


Hashmap Karsilastirma
-----------------------
* "emre" keyli "36" degeri hashmap'e ekle
* "karadeniz" keyli "36" degeri hashmap'e ekle
* Hashmapin icindeki "emre" keyinin degeri "karadeniz" keyinin degeri ile "aynı" mı kontrol et
* "batuhan" keyli "10" degeri hashmap'e ekle
* "zafer" keyli "34" degeri hashmap'e ekle
* Hashmapin icindeki "batuhan" keyinin degeri "zafer" keyinin degeri ile "farklı" mı kontrol et


Pegasus First Deneme
-----------------------
* xml olustur
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"http://www.iata.org/IATA/EDIST/2017.2\">" elementini xml'e ekle
* "<soapenv:Header/>" elementini xml'e ekle
* "<soapenv:Body>" elementini xml'e ekle
* "<AirShoppingRQ Version=\"IATA2017.2\" xsi:schemaLocation=\"xmldsig-core-schema.xsd\" xmlns=\"http://www.iata.org/IATA/EDIST/2017.2\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">" elementini xml'e ekle
* "<Document>" elementini xml'e ekle
* "Name" elementini "HITIT NDC GATEWAY" parametresiyle xml'e ekle
* "ReferenceVersion" elementini "1.0" parametresiyle xml'e ekle
* "</Document>" elementini xml'e ekle
* "<Party>" elementini xml'e ekle
* "<Sender>" elementini xml'e ekle
* "<TravelAgencySender>" elementini xml'e ekle
* "<Contacts>" elementini xml'e ekle
* "<Contact>" elementini xml'e ekle
* "<EmailContact>" elementini xml'e ekle
* "Address" elementini "craneNDC@flypgs.com" parametresiyle xml'e ekle
* "</EmailContact>" elementini xml'e ekle
* "</Contact>" elementini xml'e ekle
* "</Contacts>" elementini xml'e ekle
* "AgencyID" elementini "PC NDC" parametresiyle xml'e ekle
* "<AgentUser>" elementini xml'e ekle
* "Name" elementini "HITITADMIN" parametresiyle xml'e ekle
* "AgentUserID" elementini "A156FG69" parametresiyle xml'e ekle
* "UserRole" elementini "ADMIN" parametresiyle xml'e ekle
* "</AgentUser>" elementini xml'e ekle
* "</TravelAgencySender>" elementini xml'e ekle
* "</Sender>" elementini xml'e ekle
* "</Party>" elementini xml'e ekle
* "<Parameters>" elementini xml'e ekle
* "<Languages>" elementini xml'e ekle
* "LanguageCode" elementini "TR" parametresiyle xml'e ekle
* "</Languages>" elementini xml'e ekle
* "<CurrCodes>" elementini xml'e ekle
* "<FiledInCurrency>" elementini xml'e ekle
* "CurrCode" elementini "TRY" parametresiyle xml'e ekle
* "</FiledInCurrency>" elementini xml'e ekle
* "</CurrCodes>" elementini xml'e ekle
* "</Parameters>" elementini xml'e ekle
* "<CoreQuery>" elementini xml'e ekle
* "<OriginDestinations>" elementini xml'e ekle
* "<OriginDestination>" elementini xml'e ekle
* "<Departure>" elementini xml'e ekle
* "AirportCode" elementini "SAW" parametresiyle xml'e ekle
* "Date" elementini "2022-08-26" parametresiyle xml'e ekle
* "</Departure>" elementini xml'e ekle
* "<Arrival>" elementini xml'e ekle
* "AirportCode" elementini "DOH" parametresiyle xml'e ekle
* "</Arrival>" elementini xml'e ekle
* "</OriginDestination>" elementini xml'e ekle
* "</OriginDestinations>" elementini xml'e ekle
* "</CoreQuery>" elementini xml'e ekle
* "<Preference>" elementini xml'e ekle
* "<CabinPreferences>" elementini xml'e ekle
* "<CabinType>" elementini xml'e ekle
* "Code" elementini "Eco" parametresiyle xml'e ekle
* "</CabinType>" elementini xml'e ekle
* "</CabinPreferences>" elementini xml'e ekle
* "</Preference>" elementini xml'e ekle
* "<DataLists>" elementini xml'e ekle
* "<PassengerList>" elementini xml'e ekle
* "<Passenger PassengerID=\"SH1\">" elementini xml'e ekle
* "PTC" elementini "ADT" parametresiyle xml'e ekle
* "</Passenger>" elementini xml'e ekle
* "<Passenger PassengerID=\"SH2\">" elementini xml'e ekle
* "PTC" elementini "CHD" parametresiyle xml'e ekle
* "</Passenger>" elementini xml'e ekle
* "<Passenger PassengerID=\"SH3\">" elementini xml'e ekle
* "PTC" elementini "INF" parametresiyle xml'e ekle
* "</Passenger>" elementini xml'e ekle
* "</PassengerList>" elementini xml'e ekle
* "</DataLists>" elementini xml'e ekle
* "</AirShoppingRQ>" elementini xml'e ekle
* "</soapenv:Body>" elementini xml'e ekle
* "</soapenv:Envelope>" elementini xml'e ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* XMl response'da "ResponseID" elementini "responseId" keyi ile hashmap'e ekle
* xml "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[0].@OfferID.text()" xpathinindeki elementi "offerId" keyiyle hashmape ekle
* xml olustur
* hashmapteki "offerId" offerId ve "responseId" responseId elementlerini xml'e ekle