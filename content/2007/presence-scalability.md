Title: Presence Scalability
Date: 2007-04-11 20:27:52
Author: stpeter
Slug: presence-scalability
Category: post
Tags: 
Summary: description:
Link: http://xmpp.org/2007/04/presence-scalability/
post_id: 700


Members of the IETF's SIMPLE Working Group recently [analyzed](http://www.ietf.org/internet-drafts/draft-ietf-simple-interdomain-scaling-analysis-00.txt) the scalability of SIP/SIMPLE technologies with respect to sharing presence between domains. Because their work provides a helpful baseline for comparing presence technologies, we decided to perform a [similar analysis](http://www.xmpp.org/internet-drafts/draft-saintandre-xmpp-presence-analysis-00.html) for XMPP. The results should be of interest to any large enterprise, ISP, or carrier that is contemplating deployment of presence-based services.

Consider some of the relevant results for bandwidth usage between two presence domains:

* If the domains have 20,000 users, where each user has 4 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 30 kilobytes per second for XMPP and 830 kilobytes per second for SIMPLE.
* If the domains have 20,000 users, where each user has 20 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 150 kilobytes per second for XMPP and 1,968 kilobytes per second for SIMPLE.
* If the domains have 60,000 users, where each user has 10 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 225 kilobytes per second for XMPP and 3,683 kilobytes per second for SIMPLE.
* If the domains have 10,000,000 users, where each user has 10 contacts in the other domain and changes presence 6 times an hour, bandwidth usage is estimated to be 70,833 kilobytes per second for XMPP and 880,555 kilobytes per second for SIMPLE.

While these analyses need to be reviewed, discussed, and extended within the IETF, the preliminary results indicate that the choice of presence technology can make a significant difference with regard to bandwidth usage.

UPDATE 2007-10-02: See [here](https://stpeter.im/?p=2051) for more up-to-date analysis.

## Comments

**[Nolan Eakins](#14 "2007-04-16 05:36:38"):** I'm going to be to lazy this morning to do the actual math, but wouldn't XMPP's numbers drop signifigantly more if the servers coalesced presence stanzas? So if me and another user on my domain are both subscribed Bob's presence, Bob's server only sends out a single stanza to my server when Bob comes and goes. Simply tacking on our extended server addressing element would do the trick and would be transparent to all but the servers.

**[stpeter](#15 "2007-04-16 08:35:09"):** Yes, various optimizations would reduce the bandwidth usage. For XMPP that would include protocol extensions such as [Extended Stanza Addressing](http://www.xmpp.org/extensions/xep-0033.html) and [Stream Compression](http://www.xmpp.org/extensions/xep-0138.html). A future version of the XMPP presence scaling analysis document may discuss such optimizations.

