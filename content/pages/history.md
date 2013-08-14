Title: History
Date: 2010-01-27 15:22:48
Author: admin
Slug: history
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/history/
post_id: 192


The Extensible Messaging and Presence Protocol (XMPP) is the IETF's formalization of the base XML streaming protocols for instant messaging and presence developed within the Jabber community starting in 1999. This page provides a brief chronology of Jabber/XMPP technologies from the perspective of standardization.

### 1999

In January 1999, Jeremie Miller announced the existence of Jabber, an open technology for instant messaging and presence. Throughout 1999, development proceeded rapidly on an open-source server (jabberd), several open-source clients and code libraries, and open wire protocols for real-time XML streaming as well as basic instant messaging and presence extensions. These same base protocols have been in use (with various improvements and extensions) since 1999.

In August 1999, Jeremie submitted a [statement](/about-xmpp/history/the-jabber-project/) pledging the Jabber community's support for the IETF standards process. This statement was consistent with the founding mission of the Jabber project: to foster freedom of conversation and support open standards and interoperability in the real-time communications.

### 2000

In February 2000, the IETF published the results of work by the Instant Messaging and Presence Protocol (IMPP) Working Group: a model for instant messaging and presence systems ([RFC 2778](http://www.ietf.org/rfc/rfc2778.txt)) and a set of requirements for such systems ([RFC 2779](http://www.ietf.org/rfc/rfc2779.txt)). However, because of a lack of consensus, the IMPP WG never produced any protocols, instead deferring to other working groups that might develop protocols to meet the requirements defined in RFC 2779.

In May 2000, version 1.0 of the jabberd server was released and the base Jabber protocols (XML streaming, messaging, presence, contact lists, etc.) were stabilized.

In June 2000, Jeremie and other members of the Jabber project submitted an Internet-Draft ([text](/internet-drafts/attic/draft-jabber-00.txt) | [HTML](http://xmpp.org/internet-drafts/attic/draft-jabber-00.html)) to the Instant Messaging and Presence Protocol (IMPP) Working Group documenting the base Jabber protocols. Unfortunately, the Jabber community was not well organized at that time nor was it strongly focused on protocol development per se. Thus the initial Internet-Draft expired without the Jabber community following up or working closely with the IMPP WG.

In October 2000, jabberd 1.2 was released and the server dialback protocol was introduced to prevent address spoofing on the growing network of Jabber servers.

### 2001

In August 2001, the Jabber Software Foundation (JSF) was formed to coordinate among the growing number of open-source projects and commercial entities building or using Jabber technologies. (Note: As described below, in January 2007 the Jabber Software Foundation changed its name to the XMPP Standards Foundation or XSF.) The primary mandate of the Foundation is to manage the XML protocols used within the Jabber/XMPP community by documenting existing protocols and developing protocol extensions through an open standards process (see [XEP-0001](/extensions/xep-0001.html)).

### 2002

In late 2001 and early 2002, prominent members of the Jabber community decided to once again submit the base Jabber protocols to the IETF, this time as an official submission by the JSF. The first submission was made in February 2002 as an informational Internet-Draft ([text](/internet-drafts/attic/draft-miller-jabber-00.txt) | [HTML](http://xmpp.org/internet-drafts/attic/draft-miller-jabber-00.html)). Following on the success of this submission, it was decided to explore the possibility of forming an IETF Working Group devoted to formalization of the base Jabber protocols, under the neutral name of Extensible Messaging and Presence Protocol (XMPP). As a result, three interrelated Internet-Drafts were submitted on 2002-06-21.

On 2002-07-15, an XMPP Birds of a Feather session (BOF) was held at the 54th IETF meeting in Yokohama, Japan. Given the overall favorable reaction (captured in the [minutes](/about/bof-minutes.txt)), it was decided to proceed further by submitting a proposed working group [charter](http://xmpp.org/about/wg-charter.txt) to the IESG.

On 2002-10-31, the formation of the XMPP Working Group was approved bythe Internet Engineering Steering Group (IESG). As a result, the Foundation formally contributed the base Jabber protocols to the Internet Standards Process (see [RFC 2026](http://www.ietf.org/rfc/rfc2026.txt)) and ceded change control over those protocols to the IETF under the name Extensible Messaging and Presence Protocol (XMPP). On 2002-11-03, updated Internet-Drafts were submitted for "XMPP Core" and "XMPP IM". On 2002-11-19, the first meeting of the XMPP WG was held at IETF 55 including presentations by Jeremie Miller, Joe Hildebrand, and Peter Saint-Andre.

### 2003

In 2003, the XMPP WG essentially completed its work on formalizing the base Jabber protocols for adaptation as IETF-approved instant messaging and presence protocols that would fully meet the requirements of [RFC 2779](http://www.ietf.org/rfc/rfc2779.txt). Meetings of the XMPP WG were held on 2003-03-17 at IETF 56 and on 2003-07-18 at IETF 57 .

The revisions made to the base protocols mainly centered on improved security and internationalization. In the area of security, the XMPP Core document specifies:

* The use of standard Simple Authentication and Security Layer ([RFC 4422](http://www.ietf.org/rfc/rfc4422.txt)) for authentication (as earlier proposed in [XEP-0034](/extensions/xep-0034.html)) rather than the old protocol of hashed passwords (as described informationally in [XEP-0078](http://xmpp.org/extensions/xep-0078.html)).
* The use of standard Transport Layer Security ([RFC 4346](http://www.ietf.org/rfc/rfc4346.txt)) for channel encryption (as earlier proposed in [XEP-0035](/extensions/xep-0035.html)) rather than the older method of using SSL on separate ports.

(In addition, the XMPP WG defined as an XMPP extension a protocol for end-to-end encryption using S/MIME and CPIM.)

In the area of internationalization, the XMPP Core document specifies profiles of stringprep ([RFC 3454](http://www.ietf.org/rfc/rfc3454.txt)) for XMPP addresses (a.k.a. JIDs). In particular, XMPP uses Internationalized Domain Names ([RFC 3490](http://www.ietf.org/rfc/rfc3490.txt)) for the domain portion of a JID and the XMPP-specific nodeprep and resourceprep profiles for the remaining portions of a JID. In addition, the XMPP Core document specifies the use of the 'xml:lang' attribute for proper localization of XMPP communications (as earlier proposed in [XEP-0026](/extensions/xep-0026.html)).

In the area of user privacy, a protocol extension for block and allow lists was added to the XMPP IM specification, following up on the earlier proposal documented in [XEP-0016](/extensions/xep-0016.html).

The XMPP WG also defined a mapping of XMPP to the Common Profile for Instant Messaging ([RFC 3860](http://www.ietf.org/rfc/rfc3860.txt)) and Common Profile for Presence ([RFC 3859](http://www.ietf.org/rfc/rfc3859.txt)) produced by the IMPP WG for gateway interoperability.

Finally, the Foundation and [Jabber, Inc.](http://www.jabber.com/) jointly submitted an [IPR Notice](/about/ipr-notice.txt) to the IETF regarding the JABBER trademark.

### 2004
