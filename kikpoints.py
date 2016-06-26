import random_gen
def points():
	request.post({
	    url: "https://engine.apikik.com/api/v1/message",
	    auth: {
	        user: "smsbot",
	        pass: "<Redacted>"
	    },
	    json: {
	    	"messages":[{
	    		"to":message['from'],
	    		"type":"link",
	    		"url":"https://points.kik.com"
	    		"data":{
	    			"transaction":{
				      "id":random_gen.randomgen(),
				      "sku":"KikPointsforSMS"
				      "points":10,
				      #"url":"points.kik.com",
				      #"callback_url":"https://sms-chat-bot.herokuapp.com/kikpoints",
				      #"data":{
				       #   //Any other arbitrary data you may need
				      #}
				   }
	    		},
	    		"noForward":true
	    		}]
	    }
	}, callback);
	return
