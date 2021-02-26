$(function() {
var SHARED_SECRET = "FPz2kSn9RRupiTqrBKGrgQzeyUJuz9To2zYgD7xrmshg";

var DU_CONTRACT = "0xfa09daf905532e1300481c0c136d49994db3239b";

var STREAM_ID = "0x1225b0bd0dd4feee32fc6febfb0862ef3bc6d938/harvestdata";


var ethobj = StreamrClient.generateEthereumAccount();

console.log(ethobj.privateKey);

var client = new StreamrClient({
  auth: {
    privateKey: ethobj.privateKey,
  },
url: "wss://hack.streamr.network/api/v1/ws",
restUrl: "https://hack.streamr.network/api/v1"
});

console.log(client);

client.joinDataUnion(DU_CONTRACT, SHARED_SECRET)
  .then(memberdetails  => {
    console.log(memberdetails);
});
	const log = (msg) => {
			var elem = document.createElement('p')
			elem.innerHTML = msg
			document.body.appendChild(elem)
		}

		// register and get from https://streamr.network/signup
		//const STREAM_ID = '0x1225b0bd0dd4feee32fc6febfb0862ef3bc6d938/harvestdata'
		//const PRIVATE_KEY = '0x1225B0Bd0dD4feee32Fc6FeBFB0862Ef3bC6D938'

		// Create the client and give the API key to use by default
    
    

	       $("#btn").click(function() {
      // Here is the event we'll be sending
      			var ap = $("#aplanted").val() + " " +  $("#aunit").val();	
      			var prod = $("#production").val() + " " +  $("#punit").val();	
                        var hprice = $("#hprice").val() + " " + $("#currency").val();
			$.get({
			    url: 'http://api.positionstack.com/v1/forward',
			    data: {
			      access_key: '5cda553a6dca6af4067728fd97b29d31',
			      query: $("#location_search").val(),
			      limit: 1
			    }
			  }).done(function(data) {
			    var obj = JSON.stringify(data);
			    var obj1 = JSON.parse(obj);
			    const msg = {
					Farmer_Name : $("#fname").val(),
					Major_Crop : $("#mcrop").val(),
					Minor_Crop : $("#microp").val(),
					Area_Planted :ap,
					Production :prod,
					Harvest_Price :hprice ,
					Location_Address: $("#location_search").val(),
					Latitude: obj1.data[0].latitude,
					Longitude:obj1.data[0].longitude 
				}

				// Publish the event to the Stream
				client.publish(STREAM_ID, msg)
					.then(() => console.log('Sent successfully: ', msg))
					.catch((err) => log(err))
			  });

		});

});
