Fleepy - A Pythonic Fleep API Client
=====================================

Overview
---------

I would like to *thank* the [University of Tartu](http://www.ut.ee/et) and the [BIIT Research Group](http://biit.cs.ut.ee/) for allowing me to publish this as an open-source library.

This is an **alpha** client for the [Fleep API](https://fleep.io/fleepapi/).

As of now it is a non-opinionated library. It makes a request and returns to you always a Response object.

Response is simply a namedtuple. In that you can access attributes status_code, data, headers and cookies. So any method you call we are not wrapping it in anything but a Response.

Installation
-------------

#### Manual (Installation from PyPI coming soon)

    git clone https://github.com/nicholasamorim/fleepy.git
    python setup.py install

So far it has two dependencies, namely [Requests](http://docs.python-requests.org/en/latest/) and [attrdict](https://github.com/bcj/AttrDict). I am planning to remove Requests in the near future.

Goal
---------
The main goal of this client was to reflect the API as accurate as possible while keeping it Pythonic enough. The main thing to observe is that every slash that you see in the address of the resource you want to use, you translate that to a dot.

A couple examples:

```python
from fleepy import Fleepy

api = Fleepy()

# /account/login
api.account.login("one@email.com", "twopassword")

# /conversation/create
api.conversation.create(topic, emails, message)

# /account/export/start
api.account.export.start()

# /search
api.search(["A", "few", "keywords"])

# /search/prepare
api.search.prepare()

# /account/logout
api.account.logout()
```

Whenever Fleep API requests you for a "list" of something (usually space or comma delimited), just use a normal Python list, the library will do what Fleep wants behind the scenes.

Examples
--------

##### Creating a chat room with topic and an initial message.

The example below logins, creates a chat room with three people and sends
a message. The message uses some of Fleep styling features, check them out [here](https://fleep.zendesk.com/hc/en-us/articles/201526221-How-can-I-add-text-formatting-to-my-messages-).

```python
from fleepy import Fleepy

api = Fleepy()
api.account.login("your@email.com", "yourpassword")


api.conversation.create(
    topic='This is a Room Topic',
    emails=['your@email.com', 'guest1@email.com', 'guest2@email.com'],
    message="""*Hello*, everyone!

    Something has just been posted in our Issue tracker.

    http://issue.tracker.com<<Go To Issue>>
    """)

api.account.logout()
```

##### File upload

```python
from fleepy import Fleepy

api = Fleepy()
api.account.login("your@email.com", "yourpassword")

api.file.upload('/path/to/afile.jpg')
api.account.logout()
```

More and proper documentation to come.

##### To-Do:

- Add Tests
- Implement the Info handler.
- Create proper documentation
