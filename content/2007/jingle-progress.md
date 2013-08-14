Title: Jingle Progress
Date: 2007-04-17 23:52:34
Author: stpeter
Slug: jingle-progress
Category: post
Tags: 
Summary: description:
Link: http://xmpp.org/2007/04/jingle-progress/
post_id: 703


One of the high-priority items on our [roadmap](http://www.xmpp.org/xsf/roadmap.shtml) for 2007 is completing work on [Jingle](http://www.xmpp.org/extensions/xep-0166.html), the set of XMPP extensions for voice and video that we first published in late 2005. Although it's taken us about 16 months, we are getting [quite close](http://mail.jabber.org/pipermail/standards/2007-April/014927.html) to advancing the Jingle specifications to Draft status within our standards process. Jingle, originally based on the technology defined by [Google Talk](http://www.google.com/talk/) team, is now widely used in the [One Laptop Per Child](http://www.laptop.org/) project as well as in the Nokia 770 and the Nokia 800. Today we updated five of the main Jingle specs:[Jingle core](http://www.xmpp.org/extensions/xep-0166.html), [Jingle Audio via RTP](http://www.xmpp.org/extensions/xep-0167.html), [Jingle Video via RTP](http://www.xmpp.org/extensions/xep-0180.html), [Jingle ICE Transport](http://www.xmpp.org/extensions/xep-0176.html), and [Jingle Raw UDP Transport](http://www.xmpp.org/extensions/xep-0177.html). These specs should be ready for Last Call very soon now, so stay tuned for further updates.

## Comments

**[Dhana](#18 "2007-05-01 00:34:06"):** Is it good idea to wait for Jingle spec to be stanardized or go ahead with Google's implementation and expect only minor changes and backward compatability? I ask this coz we are thinking of a SIP - XMPP gateway. Please put your thoughts. Thanks in advance.

**[stpeter](#19 "2007-05-01 11:16:52"):** The Jingle specs are very close to advancing to Draft in our standards process. We don't know when Google will update their service to support the specs ("Jingle 1.0") as opposed to their current protocol ("Jingle 0.9"), but the differences are small enough that you probably can use one codebase for the translation with compile-time options for Jingle 1.0 vs. Jingle 0.9. For details, feel free to ping me directly via IM (I'm [stpeter@jabber.org](xmpp:stpeter@jabber.org)) or ask on the [JDEV discussion list](http://mail.jabber.org/mailman/listinfo/jdev).

