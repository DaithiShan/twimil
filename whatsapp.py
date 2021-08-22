import os
import env
from twilio.rest import Client

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
NOTIFY_SERVICE_SID = os.getenv('TWILIO_NOTIFY_SERVICE_SID')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+353851686169' 
                          ) 
 
print(message.sid)
