Title: XMPP Technologies: PubSub
Date: 2010-08-10 15:14:09
Author: admin
Slug: pubsub
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/technology-overview/pubsub/
post_id: 946


1. Overview
2. Specifications
3. Implementations
1. Servers
2. Server Components
3. Clients
4. Libraries
4. Discussion Venues

### 1. Overview

XMPP PubSub is a protocol extension for generic publish-subscribe functionality, specified in XEP-0060. The protocol enables XMPP entities to create nodes (topics) at a pubsub service and publish information at those nodes; an event notification (with or without payload) is then broadcasted to all entities that have subscribed to the node. Pubsub therefore adheres to the classic Observer design pattern and can serve as the foundation for a wide variety of applications, including news feeds, content syndication, rich presence, geolocation, workflow systems, network management systems, and any other application that requires event notifications. The personal eventing protocol (PEP), specified in XEP-0163, provides a presence-aware profile of PubSub that enables every user's JabberID to function as a virtual pubsub service for rich presence, microblogging, social networking, and real-time interactions.

### 2. Specifications

PubSub is defined in several specifications:

* [XEP-0060: Publish-Subscribe](http://www.xmpp.org/extensions/xep-0060.html)
* [XEP-0163: Personal Eventing Protocol](http://www.xmpp.org/extensions/xep-0163.html)
* [XEP-0248: PubSub Collection Nodes](http://www.xmpp.org/extensions/xep-0248.html)

#### 2.1 Payloads

PubSub and PEP are "payload-agnostic" -- you can use them as neutral transports for a wide variety of data formats. Some of the more popular payloads are listed below, especially for rich presence related to IM users:

* [Activities](/extensions/xep-0108.html)
* [Atom / RSS Notifications](/internet-drafts/draft-saintandre-atompub-notify-07.html)
[](/internet-drafts/draft-saintandre-atompub-notify-07.html)
* [Avatars](/extensions/xep-0084.html)
* [Chatroom Visits](/extensions/xep-0194.html)
* [Gaming Activities](/extensions/xep-0196.html)
* [Geolocation](/extensions/xep-0080.html)
* [Moods](/extensions/xep-0107.html)
* [Music Tunes](/extensions/xep-0118.html)
* [TV/Video Activities](/extensions/xep-0197.html)
* [Website Visits](/extensions/xep-0195.html)

### 3. Implementations

#### 3.1 Servers

The following XMPP servers include built-in support for PubSub or PEP:

* [ejabberd](http://www.ejabberd.im/)
* [Jabber XCP](http://www.jabber.com/)
* [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
* [Tigase](http://www.tigase.org/)

#### 3.2 Server Components

* [Idavoll](http://idavoll.ik.nu/)

#### 3.3 Clients

* [Gajim](http://gajim.org/)
* [Psi](http://psi-im.org/)

#### 3.4 Libraries

* [strophe](http://code.stanziq.com/strophe/) (C or JavaScript)
* [XMPP4R](http://home.gna.org/xmpp4r/) (Ruby)

### 4. Discussion Venues

The XMPP Standards Foundation maintains [a dedicated email list ("pubsub@xmpp.org") about PubSub](/participate/discuss-xmpp/), intended as a low-volume venue for discussion of PubSub implementation and protocol issues. As with all XSF technology lists, the pubsub@xmpp.org list is open to all interested individuals.
