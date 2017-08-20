from TransitFeeds import getTransistate

import threading
# todo make timer run forever - call at beginning of function
# threading.Timer(15, getTransistate).start()
getTransistate()
