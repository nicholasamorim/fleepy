### Fleepy - A Pythonic Fleep API Client

I would like to *thank* the [University of Tartu](http://www.ut.ee/et) and the [BIIT Research Group](http://biit.cs.ut.ee/) for allowing me to publish this as an open-source library.

This is an **alpha** client for the [Fleep Api](https://fleep.io/fleepapi/).

So far, it is a non-opinionated library. It makes a request and returns to you always a Response object. In that object you can access status_code, data, headers and cookies. So any function you call we are not wrapping it in anything but a Response.

So far it has two dependencies, namely Requests and attrdict. I am planning to remove Requests in the near future.

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

More and proper documentation to come.

##### To-Do:

- Add Tests
- Implement the Info handler.
- Create proper documentation
