pygcm
=====

pygcm is a python wrapper for [Google Cloud Messaging](http://developer.android.com/guide/google/gcm/index.html)

*This project is in an ALPHA state*

Installation
------------

Getting Started
---------------

    from pygcm.client import GcmClient
    
    # Create client
    API_KEY = '1234'
    c = GcmClient(API_KEY)
    
    # Set registration ids
    reg_ids = ['12', '23', '34']
    
    # Set data to send
    data = { 'score' : 100 }

    # Send data
    r = c.send(reg_ids, data)

*TBF*

