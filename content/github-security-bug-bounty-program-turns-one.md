Title: GitHub Security Bug Bounty program turns one
Date: 2015-01-28 19:43
Author: mastahyeti
Tags: engineering
Slug: github-security-bug-bounty-program-turns-one

It's already been a year since [we
launched](https://github.com/blog/1770-github-security-bug-bounty) the
[GitHub Security Bug Bounty](https://bounty.github.com/), and, thanks to
bug reports from researchers across the globe, 73 previously unknown
security vulnerabilities in our applications have been identified and
fixed.

</p>

Bugs squashed
-------------

</p>

Of **1,920** submissions in the past year, **869** warranted further
review, helping us to identify and fix vulnerabilities fitting nine of
the [OWASP top
10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)
vulnerability classifications. **33** unique researchers earned a
cumulative **\$50,100** for the **57** medium to high risk
vulnerabilities they reported.

</p>

[![Bounty submissions per
week](https://cloud.githubusercontent.com/assets/1144197/5862026/090d8d40-a234-11e4-8e9a-3aa64f0a0e0a.png)](https://cloud.githubusercontent.com/assets/1144197/5862026/090d8d40-a234-11e4-8e9a-3aa64f0a0e0a.png)

</p>

We also saw some incredibly involved and creative vulnerabilities
reported.

</p>

Our top submitter,
[@adob](https://bounty.github.com/researchers/adob.html),
[reported](https://bounty.github.com/researchers/adob.html#2014-02-10-xss-csp-bypass)
a persistent [DOM based cross-site scripting
vulnerability](https://www.owasp.org/index.php/DOM_Based_XSS), relying
on a previously unknown [Chrome browser
bug](https://code.google.com/p/chromium/issues/detail?id=240058) that
allowed our [Content Security
Policy](https://www.owasp.org/index.php/Content_Security_Policy) to be
bypassed.

</p>

Our second most prolific submitter,
[@joernchen](https://bounty.github.com/researchers/joernchen.html),
[reported](https://bounty.github.com/researchers/joernchen.html#2014-02-10-profile-name-rce)
a complex vulnerability in the communication between two of our backend
services that could allow an attacker to set arbitrary environment
variables. He followed that up by finding a way to achieve arbitrary
remote command execution by setting the right environment variables.

</p>

New year, higher payouts
------------------------

</p>

To kick off our Bug Bounty Program's second year, we're doubling the
maximum bounty payout, from \$5000 to \$10000. If you've found a
vulnerability that you'd like to submit to the GitHub security team for
review, [send us the
details](https://bounty.github.com/submit-a-vulnerability.html),
including the steps required to reproduce the bug. You can also follow
[@GitHubSecurity](https://twitter.com/githubsecurity) for ongoing
updates about the program.

</p>

Thanks to everyone who made the first year of our Bug Bounty a success.
Happy hunting in 2015!

</p>

