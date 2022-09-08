Pegasus NDC
=====================
Created by testinium on 7.09.2022

AirShopping_OrderCreate_AirDocIssue
------------------------------------
// Request1
* "Username" key "A156FG69" value degerini headera ekle
* "Password" key "SA1234" value degerini headera ekle
* "doAirOWT1" requesti olustur
* "https://prepndc.flypgs.com:443/CraneNDC/CraneNDCService" servisine istek at

//Response1
* xml "Envelope.Body.AirShoppingRS.ShoppingResponseID.ResponseID.text()" xpathinindeki elementi "responseId" keyiyle hashmape ekle
* xml "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[0].@OfferID.text()" xpathinindeki elementi "offerId" keyiyle hashmape ekle

// Request 2
* "doOrderCreateOWT1" requestine hashmapdeki "offerId" ve "responseId" degerlerini ekle
* "https://prepndc.flypgs.com:443/CraneNDC/CraneNDCService" servisine istek at

// Response 2
* xml "Envelope.Body.OrderViewRS.Response.Order.@OrderID.text()" xpathinindeki elementi "orderId" keyiyle hashmape ekle
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "simpleCurrencyPrice" keyiyle hashmape ekle

// Request 3
* "doAirDocIssueOWT1" requestine hashmapdeki "orderId" ve "simpleCurrencyPrice" degerlerini eklee
* "https://prepndc.flypgs.com:443/CraneNDC/CraneNDCService" servisine istek at

// Response 3
* "StatusCode" keyli "TK" degeri hashmap'e ekle
* xml "Envelope.Body.OrderViewRS.Response.Order.Status[0].StatusCode.text()" xpathinindeki elementi "StatusCode" keyli deger ile karsilastir