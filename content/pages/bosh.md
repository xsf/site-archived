Title: XMPP Technologies: BOSH
Date: 2010-08-10 15:00:00
Author: admin
Slug: bosh
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/technology-overview/bosh/
post_id: 934


1. Overview
2. Specifications
3. Implementations
1. Servers
2. Connection Managers
3. Clients
4. Libraries
4. Discussion Venues

### 1. Overview

BOSH is "Bidirectional-streams Over Synchronous HTTP", a technology for two-way communication over the Hypertext Transfer Protocol (HTTP). BOSH emulates many of the transport primitives that are familiar from the Transmission Control Protocol (TCP). For applications that require both "push" and "pull" communications, BOSH is significantly more bandwidth-efficient and responsive than most other bidirectional HTTP-based transport protocols and the techniques known as AJAX. BOSH achieves this efficiency and low latency by avoiding HTTP polling, yet it does so without resorting to chunked HTTP responses as is done in the technique known as Comet. To date, BOSH has been used mainly as a transport for traffic exchanged between Jabber/XMPP clients and servers (e.g., to facilitate connections from web clients and from mobile clients on intermittent networks). However, BOSH is not tied solely to XMPP and can be used for other kinds of traffic, as well.

### 2. Specifications

BOSH is defined in two specifications:

* [XEP-0124: Bidirectional-streams Over Synchronous HTTP](http://www.xmpp.org/extensions/xep-0124.html)
* [XEP-0206: XMPP Over BOSH](http://www.xmpp.org/extensions/xep-0206.html)

### 3. Implementations

#### 3.1 Servers

The following XMPP servers include built-in support for BOSH:

* [ejabberd](http://www.ejabberd.im/)
* [Jabber XCP](http://www.jabber.com/)
* [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
* [Prosody](http://prosody.im/)
* [Tigase](http://www.tigase.org/)

#### 3.2 Connection Managers

The following standalone XMPP connection managers can be used with a wide variety of XMPP servers:

* [Araneo](http://blog.bluendo.com/ff/bosh-connection-manager-update)
* [JabberHTTPBind](http://blog.jwchat.org/jhb/)
* [Punjab](http://code.stanziq.com/punjab)
* [rhb](http://rubyforge.org/projects/rhb/)

#### 3.3 Clients

* [Adium](http://adium.im/)
* [Gajim](http://gajim.org/)
* [JWChat](http://blog.jwchat.org/jwchat/)
* [Pidgin](http://pidgin.im/)
* [Soashable](http://www.soashable.com/)
* [SparkWeb](http://www.igniterealtime.org/projects/sparkweb/)
* [Tigase Messenger](http://www.tigase.org/project/messenger)
* [Tigase Minichat](http://www.tigase.org/project/minichat)

#### 3.4 Libraries

* [emite](http://code.google.com/p/emite/) (gwt)
* [gloox](http://camaya.net/gloox) (C++)
* [JSJaC](http://blog.jwchat.org/jsjac/) (JavaScript)
* [strophe](http://code.stanziq.com/strophe/) (C or JavaScript)
* [XIFF](http://www.igniterealtime.org/projects/xiff/) (Flash)
* [XMPP4GWT](http://www.tigase.org/project/xmpp4gwt) (gwt)
* [xmpp4js](http://xmpp4js.sourceforge.net/index.html) (JavaScript)
* [XMPP4R](http://home.gna.org/xmpp4r/) (Ruby)

### 4. Discussion Venues

The XMPP Standards Foundation maintains [a dedicated email list ("bosh@xmpp.org") about BOSH](/participate/discuss-xmpp/), intended as a low-volume venue for discussion of BOSH implementation and protocol issues. As with all XSF technology lists, the bosh@xmpp.org list is open to all interested individuals.
