Title: Practical Network Security
Date: 2007-02-07 17:29:59
Author: stpeter
Slug: practical-network-security
Category: post
Tags: 
Summary: description:
Link: http://xmpp.org/2007/02/practical-network-security/
post_id: 692


Two months ago we launched the XMPP Intermediate Certification Authority at [xmpp.net](https://www.xmpp.net/). It was a bit of an unusual step for a standards development organization to take -- after all, you don't see the [IETF](http://www.ietf.org/), [W3C](http://www.w3.org/), and [IMC](http://www.imc.org/) offering free digital certificates to hostmasters, webmasters, and postmasters. But we decided that we needed provide some practical leadership regarding the security of the Jabber/XMPP network, and [StartCom](http://cert.startcom.org/) (our root CA) has made that task much easier than we could have hoped. Here are the results so far:

1. We have issued around 100 active server certificates.
2. We have stabilized the certificate data format based on feedback from server admins and developers.
3. Several large XMPP-based code projects have built in support for StartCom's root certificate.
4. More widespread deployment has exposed incorrect certificate handling in several software codebases, leading to bug fixes and more secure code.

Clearly we have much farther to go. First, we'd like to see all server and client codebases support [TLS](http://www.ietf.org/rfc/rfc4346.txt) for channel security, [SASL](http://www.ietf.org/rfc/rfc4422.txt) for strong authentication, and the StartCom root certificate.

Second, we need many more server deployments to obtain digital certificates. In the past that has been an expensive proposition, but now the XSF provides no-cost ("free as in beer") digital certificates so there's no excuse! By the end of 2007 we hope that a majority of the traffic on the XMPP network will be protected by channel encryption. But to make that happen we need server admins to visit [xmpp.net](https://www.xmpp.net/), sign up for an account, and request a free certificate by following our simple [certificate process](https://www.xmpp.net/certificate-process). Remember, it's easy, it's fun, and it makes the network more secure, one server at a time!

## Comments

**[Martin](#4 "2007-02-07 15:32:48"):** The use of StartCom certificates would increase dramatically if it were possible to obtain a certificate during the installation process or in the administration console of the server instead of using the xmpp.net website. Such an integration should be possible and encouraged (or even sponsored)

**[stpeter](#5 "2007-02-08 10:07:13"):** That's an interesting suggestion, we will explore it with StartCom and some of the server vendors. Thanks!

**[Martin](#6 "2007-02-09 04:07:23"):** Btw: Integration with xmpp.net could be the first step and shouldn't be that difficult, esp. if your administration console is web based.

