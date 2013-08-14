Title: XMPP Technologies: MUC
Date: 2010-08-10 15:09:24
Author: admin
Slug: muc
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/technology-overview/muc/
post_id: 942


1. Overview
2. Specifications
3. Implementations
1. Servers
2. Server Components
3. Clients
4. Libraries
4. Discussion Venues

### 1. Overview

MUC is Multi-User Chat, an XMPP extension for multi-party information exchange similar to Internet Relay Chat (IRC), whereby multiple XMPP users can exchange messages in the context of a room or channel. In addition to standard chatroom features such as room topics and invitations, the protocol defines a strong room control model, including the ability to kick and ban users, to name room moderators and administrators, to require membership or passwords in order to join the room, etc. Because MUC rooms are based on XMPP, they can be used to exchange not only plaintext message bodies but a wide variety of XML payloads.

### 2. Specifications

MUC is defined in one primary specification (XEP-0045) and several ancillary specifications:

* [XEP-0045: Multi-User Chat](http://www.xmpp.org/extensions/xep-0045.html)
* [XEP-0249: Direct MUC Invitations](http://www.xmpp.org/extensions/xep-0249.html)
* [XEP-0272: Multiparty Jingle](http://www.xmpp.org/extensions/xep-0272.html)

### 3. Implementations

#### 3.1 Servers

The following XMPP servers include built-in support for MUC:

* [ejabberd](http://www.ejabberd.im/)
* [Jabber XCP](http://www.jabber.com/)
* [M-Link](http://www.isode.com/products/m-link.html)
* [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
* [Prosody](http://prosody.im/)
* [Tigase](http://www.tigase.org/)

#### 3.2 External Components

The following standalone components can be used with a wide variety of XMPP servers:

* [mu-conference](https://gna.org/projects/mu-conference/)
* [palaver](http://code.stanziq.com/palaver)

#### 3.3 Clients

* [Adium](http://adiumx.com/)
* [Gajim](http://gajim.org/)
* [JWChat](http://blog.jwchat.org/jwchat/)
* [mcabber](http://mcabber.com/)
* [Pidgin](http://pidgin.im/)
* [Psi](http://www.psi-im.org/)

#### 3.4 Libraries

* [AnyEvent:XMPP](http://www.ta-sa.org/projects/anyevent_xmpp.html) (Perl)
* [gloox](http://camaya.net/gloox) (C++)
* [jabber-net](http://code.google.com/p/jabber-net/) (.Net)
* [libpurple](http://developer.pidgin.im/wiki/WhatIsLibpurple) (C)
* [Smack](http://www.igniterealtime.org/projects/smack/index.jsp) (Java)
* [XMPP4R](http://home.gna.org/xmpp4r/) (Ruby)

### 4. Discussion Venues

The XMPP Standards Foundation maintains [a dedicated email list ("muc@xmpp.org") about MUC](/participate/discuss-xmpp/), intended as a low-volume venue for discussion of MUC implementation and protocol issues. As with all XSF technology lists, the muc@xmpp.org list is open to all interested individuals.
