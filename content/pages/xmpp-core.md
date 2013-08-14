Title: Protocol Stack
Date: 2010-02-23 08:53:11
Author: admin
Slug: xmpp-core
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/xmpp-protocols/xmpp-core/
post_id: 238


The XMPP Standards Foundation (XSF) recognizes the following protocols either as comprising the Extensible Messaging and Presence Protocol (XMPP) published by the [Internet Engineering Task Force](http://www.ietf.org/) (IETF) or as being official XMPP extensions published by the XSF.

1. [Base XMPP Protocols](#base)
1. [XMPP Extensions](/pages/protocol-namespaces)
    1. [Final XMPP Extensions](#final)
    1. [Draft XMPP Extensions](#draft)

### <a name="base">1.0 Base XMPP Protocols</a>

The following are the base protocols that define the Extensible Messaging and Presence Protocol as specified in [RFC 6120](http://tools.ietf.org/html/rfc6120) and [RFC 6121](http://tools.ietf.org/html/rfc6121). These protocols were originally developed within the Jabber developer community in 1999 ("XMPP 0.9"), formalized by the IETF's XMPP Working Group in 2003 and 2004, and updated by the XMPP WG in 2009 and 2010, resulting in definition of XMPP 1.0.

* [Jabber Client](/protocols/jabber:client)
* [Jabber Server](/protocols/jabber:server)
* [Presence and IM Session Establishment](/protocols/urn:ietf:params:xml:ns:xmpp-session)
* [Resource Binding](/protocols/urn:ietf:params:xml:ns:xmpp-bind)
* [Simple Authentication and Security Layer](/protocols/urn:ietf:params:xml:ns:xmpp-sasl)
* [S/MIME Encryption](/protocols/urn:ietf:params:xml:ns:xmpp-e2e)
* [Stanza Errors](/protocols/urn:ietf:params:xml:ns:xmpp-stanzas)
* [Stream Errors](/protocols/urn:ietf:params:xml:ns:xmpp-streams)
* [Transport Layer Security](/protocols/urn:ietf:params:xml:ns:xmpp-tls)
* [XML Streams](/protocols/streams)

### 2.0 XMPP Extensions

Since mid-2001, the XMPP Standards Foundation (formerly the Jabber Software Foundation) has documented and managed the Jabber/XMPP protocols through an open standards process focused on the discussion and advancement of XMPP Extension Protocols (XEPs). Such specifications define XMPP extensions and must not be considered part of XMPP, which is all and only the core specifications produced by the IETF. Note: The following lists do not include standards-track XEPs that are Deferred, Deprecated, Experimental, Obsolete, Rejected, or Retracted, nor XEPs that are Historical or Informational.

#### <a name="final">2.1 Final XMPP Extensions</a>

The following XEPs have advanced to a status of Final within the XSF's standards process. The protocols defined in these specifications may be considered stable technologies for the purposes of implementation and deployment.

* [Chat State Notifications](/protocols/chatstates)
* [Data Forms](/protocols/jabber_x_data)
* [Delayed Delivery](/protocols/urn_xmpp_delay)
* [Entity Time](/protocols/urn_xmpp_time)
* [In-Band Registration](/protocols/jabber_iq_register)
* [Jabber-RPC](/protocols/jabber_iq_rpc)
* [Last Activity](/protocols/jabber_iq_last)
* [Serverless Messaging](/protocols/linklocal)
* [Service Discovery](/protocols/disco)
* [Stream Compression](/protocols/compress)
* [XMPP Ping](/protocols/urn_xmpp_ping)

#### <a name="draft">2.2 Draft XMPP Extensions</a>

The following XEPs have advanced to a status of Draft within the XSF's standards process. Implementations are encouraged and the protocols are appropriate for deployment in production systems, but it is possible that some changes to the protocols will be made before they become Final Standards.

* [Ad-Hoc Commands](/protocols/commands)
* [Advanced Message Processing](/protocols/amp)
* [Bidirectional-streams Over Synchronous HTTP (BOSH)](/protocols/httpbind)
* [Bookmarks](/protocols/bookmarks)
* [Data Forms Layout](/protocols/xdata-layout)
* [Data Forms Validation](/protocols/xdata-validate)
* [Entity Capabilities](/protocols/caps)
* [Feature Negotiation](/protocols/feature-neg)
* [File Transfer](/protocols/file-transfer)
* [Flexible Offline Message Retrieval](/protocols/offline)
* [In-Band Bytestreams](/protocols/ibb)
* [JID Escaping](/protocols/jidescaping)
* [Message Receipts](/protocols/urn_xmpp_receipts)
* [Multi-User Chat](/protocols/muc)
* [Out of Band Data](/protocols/jabber_x_oob)
* [Personal Eventing via Pubsub](/protocols/pep)
* [Privacy Lists](/protocols/jabber_iq_privacy)
* [Publish-Subscribe](/protocols/pubsub)
* [Publishing Stream Initiation Requests](/protocols/sipub)
* [Result Set Management](/protocols/rsm)
* [Roster Item Exchange](/protocols/rosterx)
* [Service Discovery](/protocols/disco)
* [Stanza Headers and Internet Metadata](/protocols/shim)
* [SOAP Over XMPP](/protocols/soap)
* [Software Version](/protocols/jabber_iq_version)
* [Stanza Session Negotiation](/protocols/urn_xmpp_ssn)
* [Stream Initiation](/protocols/si)
* [User Activity](/protocols/activity)
* [User Location](/protocols/geoloc)
* [User Mood](/protocols/mood)
* [User Nickname](/protocols/nick)
* [User Tune](/protocols/tune)
* [Verifying HTTP Requests via XMPP](/protocols/http-auth)
* [XHTML-IM](/protocols/xhtml-im)
* [XMPP Over BOSH](/protocols/urn_xmpp_xbosh)
In addition to the foregoing protocols, the XMPP Standards Foundation has informationally defined various best practices related to XMPP, has historically documented several protocols that are in wide use within the Jabber/XMPP community, and regularly considers numerous experimental technologies for advancement to Draft and then Final. However, such informational, historical, and experimental specifications are not officially recognized by the XSF as part of the XMPP protocol stack.
