Title: Vulnerability in XMPP Server Dialback Implementations
Date: 2012-08-21 16:04:23
Author: stpeter
Slug: server-dialback
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/resources/security-notices/server-dialback/
post_id: 2627


_Original Release Date: 2012-08-21_

_Last Updated: 2012-08-21_

## Overview

Some implementations of the XMPP Server Dialback protocol ([RFC 3920](http://rfcs/rfc3920.html) / [XEP-0220](/extensions/xep-0220.html)) have not been checking dialback responses to ensure that validated results are correlated with requests.

## Description

The Server Dialback protocol is a proof-of-possession technology used between XMPP servers to provide identity verification based on the Domain Name System (DNS); the basic approach is that when a receiving server accepts a server-to-server connection from an initiating server, it does not process traffic over the connection until it has verified the initiating server's key with an authoritative DNS entry for the initiating server. Additionally, the protocol is used to negotiate whether the receiving server is accepting stanzas for the target domain. The goal of the protocol is to help prevent address spoofing on the XMPP network, which it has effectively done since deployed on the XMPP network in October 2000.

There are four steps to the protocol:

1. Authorization Request: The initiating server sends a dialback key to the receiving server for a given domain pair consisting of a source domain and a target domain.
2. Verify Request: the receiving server forwards the key to the authoritative server for the domain asserted by the initiating server.
3. Verify Response: the authoritative server informs the receiving server whether the key is valid or invalid.
4. Authorization Response: the receiving server reports the result of the negotiation to the initiating server.

Some XMPP server implementations have not been checking the Verify Response to ensure that the receiving server previously received an Authorization Request for the domain pair included in the Verify Response. Thus an attacking server has been able to send a Verify Response for domains that were never asserted by an initiating server, and some receiving servers would accept such domain pairs as validated.

In addition, some XMPP server implementations have not been checking the Authorization Response to ensure that the initiating server previously sent an Authorization Request for the domain pair included in the Authorization Response. Thus an attacking server has been able to send an Authorization Response for domains that were never asserted by an initiating server, and some initiating servers would accept such domain pairs as validated.

## Impact

An attacking server could spoof one or more domains in communicating with a vulnerable server implementation, thereby avoiding the protections built into the Server Dialback protocol.

## Solution

Upgrade to corrected server code.

## Vendor Information

<table class="table table-bordered table-condensed">
	<tr><th>Vendor</th><th>Product</th><th>Status</th><th>Notified</th><th>Updated</th></tr>
<tr>
<td>Apache</td>
<td>Vysper</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-14</td>
</tr>
<tr>
<td>Apple Inc.</td>
<td>iChat Server</td>
<td>Affected</td>
<td>2012-08-07</td>
<td>2012-08-09</td>
</tr>
<tr>
<td>Cisco Systems, Inc.</td>
<td>Jabber XCP</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Citadel</td>
<td>Citadel</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>CommuniGate</td>
<td>CommuniGate Pro</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-14</td>
</tr>
<tr>
<td>Coversant</td>
<td>SoapBox Server</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-09</td>
</tr>
<tr>
<td>djabberd</td>
<td>djabberd</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-12</td>
</tr>
<tr>
<td>Google</td>
<td>Google Talk</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-03</td>
</tr>
<tr>
<td>IBM</td>
<td>Lotus Sametime Gateway</td>
<td>Unaffected</td>
<td>2012-08-09</td>
<td>2012-08-09</td>
</tr>
<tr>
<td>IceWarp</td>
<td>IceWarp Instant Messaging Server</td>
<td>Unknown</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>igniterealtime.org</td>
<td>Openfire</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>inetdextra</td>
<td>in.jabberd</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Isode Ltd.</td>
<td>M-Link</td>
<td>Fixed</td>
<td>2012-08-02</td>
<td>2012-08-07</td>
</tr>
<tr>
<td>jabberd 1.x</td>
<td>jabberd 1.x</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-07</td>
</tr>
<tr>
<td>jabberd 2.x</td>
<td>jabberd 2.x</td>
<td>Fixed</td>
<td>2012-08-02</td>
<td>2012-08-08</td>
</tr>
<tr>
<td>j-livesupport</td>
<td>Jerry Messenger</td>
<td>Unknown</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Kwickserver</td>
<td>Kwickserver</td>
<td>Unknown</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>ProcessOne</td>
<td>ejabberd</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-14</td>
</tr>
<tr>
<td>Prosody</td>
<td>Prosody</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>psyced</td>
<td>psyced</td>
<td>Fixed</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Siemens</td>
<td>Siemens OpenScape</td>
<td>Unknown</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Tigase</td>
<td>Tigase</td>
<td>Fixed</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Vines</td>
<td>Vines</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-02</td>
</tr>
<tr>
<td>Wokkel</td>
<td>Wokkel</td>
<td>Unaffected</td>
<td>2012-08-02</td>
<td>2012-08-15</td>
</tr>
</table>

## References

* [https://datatracker.ietf.org/doc/rfc3920/](https://datatracker.ietf.org/doc/rfc3920/)
* [http://xmpp.org/extensions/xep-0220.html](/extensions/xep-0220.html)

## Credits

The vulnerability has been separately discovered by multiple teams in the past. Thanks to Philipp Hancke for recently reporting it in a more public fashion. Thanks also to Dave Cridland, Tomasz Sterna, and Matthew Wild for their feedback. This report was written by Peter Saint-Andre.

## Feedback

If you have feedback, comments, or additional information about this vulnerability, please send email to the [security@xmpp.org discussion list](http://mail.jabber.org/mailman/listinfo/security).
