import random

import rick
import dave

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

DAVE = 'NUMBERHERE'
ALI = 'NUMBERHERE'

class Insulter(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self, messageProtocolEntity):
        author = messageProtocolEntity.getAuthor(full=False)
        text = messageProtocolEntity.getBody()
        if author == ALI and 'who is your master?' in text.lower():
            resp = TextMessageProtocolEntity("Ali is my master", to=messageProtocolEntity.getFrom(), notify=True)
            self.toLower(resp)
        if author == DAVE and "email material" in text.lower():
            resp = TextMessageProtocolEntity(dave.argh[random.randint(0, len(dave.argh) - 1)], to=messageProtocolEntity.getFrom(), notify=True)
            self.toLower(resp)
        if 'rick' in text.lower():
            quote = rick.rick[random.randint(0, len(rick.rick) - 1)]
            resp = TextMessageProtocolEntity(quote, to=messageProtocolEntity.getFrom(), notify=True)
            self.toLower(resp)

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
