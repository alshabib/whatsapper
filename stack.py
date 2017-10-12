from yowsup.stacks import  YowStackBuilder
import layer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer

CREDENTIALS = ("SUBNUMBER", "password")

class YowsupEchoStack(object):
    def __init__(self, credentials = None, encryptionEnabled = True):
        stackBuilder = YowStackBuilder()

        self.stack = stackBuilder\
            .pushDefaultLayers(encryptionEnabled)\
            .push(layer.Insulter)\
            .build()

        self.stack.setCredentials(CREDENTIALS)

    def start(self):
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)

if __name__ ==  "__main__":
    YowsupEchoStack().start()   
