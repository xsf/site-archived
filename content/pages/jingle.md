Title: XMPP Technologies: Jingle
Date: 2010-08-10 15:04:44
Author: admin
Slug: jingle
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/technology-overview/jingle/
post_id: 938


1. Overview
2. Specifications
3. Implementations
1. Clients
2. Libraries
3. Call Managers / VoIP Servers
4. Discussion Venues

### 1. Overview

In essence, Jingle provides a way for Jabber clients to set up, manage, and tear down multimedia sessions. Such sessions can support a wide range of application types (such as voice chat, video chat, and file transfer) and use a wide range of media transport methods (such as TCP, UDP, RTP, or even in-band XMPP itself). The signalling to establish a Jingle session is sent over XMPP, and typically the media is sent directly peer-to-peer or through a media relay. Jingle provides a pluggable framework for both application types and media transports; in the case of voice and video chat, a Jingle negotiation usually results in use of the Real-time Transport Protocol (RTP) as the media transport and thus is compatible with existing multimedia technologies such as the Session Initiation Protocol (SIP). Furthermore, the semantics of Jingle signalling was designed to be consistent with both SIP and the Session Description Protocol (SDP), thus making it straightforward to provide signalling gateways between XMPP networks and SIP networks.

### 2. Specifications

Jingle is defined in a number of specifications:

* [XEP-0166: Jingle](/extensions/xep-0166.html)
* [XEP-0167: Jingle RTP Sessions](/extensions/xep-0167.html)
* [XEP-0176: Jingle ICE-UDP Transport Method](/extensions/xep-0176.html)
* [XEP-0177: Jingle Raw UDP Transport Method](/extensions/xep-0177.html)
* [XEP-0181: Jingle DTMF](/extensions/xep-0181.html)
* [XEP-0234: Jingle File Transfer](/extensions/xep-0234.html)

### 3. Implementations

_Note: Many of the following implementations support the older Google Talk protocol and are being upgraded to support Jingle as it is defined in the specifications; contact the project developers for details._

#### 3.1 Clients

* [Coccinella](http://coccinella.im/)
* [Gajim](http://www.gajim.org/)
* [Jitsi (formerly named SIP Communicator)](http://jitsi.org/)
* [Pandion](http://pandion.im/)
* [Pidgin (formerly named Gaim)](http://pidgin.im/)
* [Psi](http://psi-im.org/)
* [Telepathy](http://telepathy.freedesktop.org/)
* [Yate](http://yate.null.ro/)

#### 3.2 Libraries

* [libjingle](http://code.google.com/apis/talk/) (C/C++)
* [Smack](http://www.igniterealtime.org/projects/smack/) (Java)
* [Telepathy Gabble](http://telepathy.freedesktop.org/) (C)
* [yjingle](http://yate.null.ro/) (C++)

#### 3.3 Call Managers / VoIP Servers

* [Asterisk](http://www.asterisk.org/)
* [FreeSWITCH](http://freeswitch.org/)
* [Yate](http://yate.null.ro/)

### 4. Discussion Venues

The XMPP Standards Foundation maintains [a dedicated email list ("jingle@xmpp.org") about Jingle](/participate/discuss-xmpp/), intended as a low-volume venue for discussion of MUC implementation and protocol issues. As with all XSF technology lists, the jingle@xmpp.org list is open to all interested individuals.
