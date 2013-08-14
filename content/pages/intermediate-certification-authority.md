Title: Intermediate Certification Authority
Date: 2010-08-11 15:42:55
Author: admin
Slug: intermediate-certification-authority
Category: page
Tags: 
Summary: description:
Link: http://xmpp.org/about-xmpp/xsf/xsf-organizational-documents/intermediate-certification-authority/
post_id: 1018


Author:
Peter Saint-Andre

Version:
1.0

Date:
2006-11-28

Status:
Approved
Table of Contents

1. Introduction
2. Background
3. Choice of Provider
4. Proposal
5. Projected Costs
6. Oversight and Reporting

### 1.0 Introduction

The Jabber/XMPP community has always cared about privacy and security. In particular, when the XML wire protocols used by Jabber technologies were formalized within the IETF (under the name XMPP), they were subject to rigorous security review, resulting in the use of Transport Layer Security (TLS) for channel encryption. Unfortunately, it can be both difficult and expensive for administrators of XMPP servers to obtain proper X.509 certificates for use in securing communications with TLS. This proposal addresses that problem by establishing an intermediate certification authority (ICA) for the network of XMPP servers.

### 2.0 Background

Currently, server administrators who care about securing communications tend to create self-signed certificates. Unfortunately, self-signed certificates do not engender strong trust in the network, since anyone can create a self-signed certificate. The traditional approach to securing communication channels in a high-trust manner is to ensure that server certificates are issued by a certification authority (CA) that completes some level of due diligence regarding the identity of the server administrator before issuing the certificate. The resulting certificate can be issued by a root CA (which is at the "root" of the trust chain or "tree"), or by an intermediate CA (which depends on the root CA but administers a specialized branch of the trust chain). Eventually, we hope that all providers of X.509 certificates will issue certificates for XMPP servers. However, XMPP server certificates that conform to the format specified in Section 5.1 of RFC 3920 include information that is not yet standard in certificates for, say, HTTP servers. For this reason, CAs must complete some development work in order to issue fully conforming certificates for XMPP servers. Because major CAs such as Verisign and Thawte probably do not have an interest in completing such work without a demonstrated market need, it makes sense for XMPP server administrators to work on the necessary processes and procedures with some of the smaller, more flexible CAs first. (Another approach would be for XMPP server administrators to form their own certification authority, probably under the auspices of the Jabber Software Foundation (JSF); however, running a CA is far outside the core competency of the JSF.) Therefore, the initial goal of this proposal is for the Jabber Software Foundation to work with one or two CAs who already issue free or low-cost certificates while still adhering to industry standards regarding identity verification. Research into certification authorities indicates that the most likely candidates are [CAcert](http://www.cacert.org/) and [StartCom](http://cert.startcom.org/). CAcert is a loosely-knit volunteer organization built on something akin to the open-source model, which issues server certificates based on acquisition of sufficient points in its web of trust. StartCom is a commercial entity whose main business is offering a Linux distribution, but which issues server certificates in the more traditional manner based on presentation and validation of individual credentials (e.g., government-issued identification) and association with the relevant domain (e.g., whois lookups).

### 3.0 Choice of Provider

The author of this proposal has been involved with CAcert since late 2004 and with StartCom since early 2006. Both are well-intentioned organizations in which honest, hard-working, security-minded individuals are working to make the Internet a more high-trust environment. The JSF's choice of one CA with which to work initially should be driven by the JSF's requirements at this stage in the evolution of the Jabber/XMPP network. For the purposes of this proposal, the JSF's requirements regarding the choice of an initial CA are:

1. Must conform to industry practices regarding identity verification and certificate issuance.
2. Must already issue free or low-cost server certificates.
3. Must support the XMPP object identifier specified in Section 5.1 of RFC 3920, or be willing and able to add such support (including the ability to specify multiple XMPP OIDs, e.g., for virtual domains and XMPP server components).
4. Must be organizationally viable, such that the JSF can form a long-term relationship with the CA.
5. Should have its root certificate included in well-known operating systems (e.g., various Unices, MacOS, Windows) and certificate "bundles" (e.g., Mozilla), or be well on the way to such inclusion.
6. Should enable the JSF to function as an intermediate certification authority (ICA) for the Jabber/XMPP network.
CAcert issues free server certificates (upon gaining sufficient points in its web of trust) and StartCom issues low-cost server certificates. Through work with the author of this proposal and several XMPP server administrators, CAcert supports the XMPP object identifer, and StartCom has stated that it is willing and able to add such support. Although CAcert offers "organizational assurance", it does not presently enable organizations to function as ICAs, whereas StartCom has an [ICA program](http://cert.startcom.org/?app=128) in place. Regarding organizational viability, commercial entities can go out of business and community projects can wither away, so there is no guarantee of continued viability in either case. The major differentiating factor between the two CAs is conformance with industry practices, in large measure as indicated by inclusion of the CA's root certificate in operating systems and certificate bundles (because the JSF has not performed an audit of either CA and is not in a position to do so, we must trust that other organizations have performed appropriate due diligence). To our knowledge, CAcert has not passed an independent audit and CAcert's root certificate has not gained inclusion in any operating system or certificate bundle. By contrast, StartCom has passed an independent audit (performed by WE Consulting Group of Israel, see [report](http://cert.startcom.org/audit.pdf)) and has been included [various web browsers](http://cert.startcom.org/?app=140), in the[Mozilla](http://www.hecker.org/mozilla/ca-certificate-list#startcom) certificate bundle (including [Firefox 2](http://www.startcom.org/?lang=en&app=14&rel=22)), in KDE, in OpenSSL, and in Mac OS X 10.5 (Leopard). Because of the wider acceptance of the StartCom root certificate and the ability of the JSF to run an ICA under StartCom's auspices, it seems appropriate to choose StartCom as the initial provider of certificates for the Jabber/XMPP network, while continuing to monitor the progress of CAcert and other CAs with an eye to working with them in the future. Note well that the JSF's choice of an initial CA is decidedly not exclusive. That is, the JSF could (and very well might) form relationships with other CAs. In part, the purpose of this proposal is to gain experience with the issuance of X.509 certificates to XMPP server administrators. That experience will help the JSF understand the requirements for discussions with other CAs in the future.

### 4.0 Proposal
