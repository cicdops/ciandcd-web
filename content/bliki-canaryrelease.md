Title: Bliki: CanaryRelease
Date: 2014-06-25 13:36
Author: Danilo Sato
Tags: bliki
Slug: bliki-canaryrelease

**Canary release** is a technique to reduce the risk of

introducing a new software version in production by slowly rolling out
the

change to a small subset of users before rolling it out to the entire

infrastructure and making it available to everybody.

</p>

Similar to a
[BlueGreenDeployment](http://martinfowler.com/bliki/BlueGreenDeployment.html),
you start by deploying the

new version of your software to a subset of your infrastructure, to
which no

users are routed.

</p>

![](http://martinfowler.com/bliki/images/canaryRelease/canary-release-1.png)

</p>

When you are happy with the new version, you can start routing a few

selected users to it. There are different strategies to choose which
users

will see the new version: a simple strategy is to use a random sample;
some

companies choose to release the new version to their internal users and

employees before releasing to the world; another more sophisticated
approach

is to choose users based on their profile and other demographics.

</p>

![](http://martinfowler.com/bliki/images/canaryRelease/canary-release-2.png)

</p>

As you gain more confidence in the new version, you can start releasing
it

to more servers in your infrastructure and routing more users to it. A
good

practice to rollout the new version is to repurpose your existing

infrastructure using
[PhoenixServers](http://martinfowler.com/bliki/PhoenixServer.html) or to
provision new

infrastructure and decommission the old one using
[ImmutableServers](http://martinfowler.com/bliki/ImmutableServer.html).

</p>

Canary release is an application of
[ParallelChange](http://martinfowler.com/bliki/ParallelChange.html),
where the

migrate phase lasts until all the users have been routed to the new
version.

At that point, you can decomission the old infrastructure. If you find
any

problems with the new version, the rollback strategy is simply to
reroute

users back to the old version until you have fixed the problem.

</p>

![](http://martinfowler.com/bliki/images/canaryRelease/canary-release-3.png)

</p>

A benefit of using canary releases is the ability to do capacity testing
of

the new version in a production environment with a safe rollback
strategy if

issues are found. By slowly ramping up the load, you can monitor and
capture

metrics about how the new version impacts the production environment.
This

is an alternative approach to creating an entirely separate capacity
testing

environment, because the environment will be as production-like as it
can be.

</p>

Although the name for this technique might not be familiar
[[1]](http://martinfowler.com/feed.atom#footnote-origin),

the practice of canary releasing has been adopted for some time.
Sometimes

it is referred to as a **phased rollout** or an <b>incremental

rollout</b>.

</p>

In large, distributed scenarios, instead of using a router to decide
which

users will be redirected to the new version, it is also common to use

different partitioning strategies. For example: if you have
geographically

distributed users, you can rollout the new version to a region or a
specific

location first; if you have multiple brands you can rollout to a single

brand first, etc. Facebook chooses to use a strategy with multiple
canaries,

the first one being visible only to their internal employees and having
all

the [FeatureToggles](http://martinfowler.com/bliki/FeatureToggle.html)
turned on so they can detect problems with new

features early.

</p>

![](http://martinfowler.com/bliki/images/canaryRelease/facebook-canary-strategy.jpg)

</p>

Canary releases can be used as a way to implement A/B testing due to

similarities in the technical implementation. However, it is preferable
to

avoid conflating these two concerns: while canary releases are a good
way

to detect problems and regressions, A/B testing is a way to test a
hypothesis

using variant implementations. If you monitor business metrics to detect

regressions with a canary
[[2]](http://martinfowler.com/feed.atom#footnote-cluster-immune-system),
also using

it for A/B testing could interfere with the results. On a more practical

note, it can take days to gather enough data to demonstrate statistical

significance from an A/B test, while you would want a canary rollout to

complete in minutes or hours.

</p>

One drawback of using canary releases is that you have to manage
multiple

versions of your software at once. You can even decide to have more than
two

versions running in production at the same time, however it is best to
keep

the number of concurrent versions to a minimum.

</p>

Another scenario where using canary releases is hard is when you
distribute

software that is installed in the users' computers or mobile devices. In

this case, you have less control over when the upgrade to the new
version

happens. If the distributed software communicates with a backend, you
can

use [ParallelChange](http://martinfowler.com/bliki/ParallelChange.html)
to support both versions and monitor which

client versions are being used. Once the usage numbers fall to a certain

level, you can then contract the backend to only support the new
version.

</p>

Managing database changes also requires attention when doing canary
releases.

Again, using
[ParallelChange](http://martinfowler.com/bliki/ParallelChange.html) is a
technique to mitigate this

problem. It allows the database to support both versions of the
application

during the rollout phase.

</p>

<div class="furtherReading">

</p>

Further Reading
---------------

</p>

Canary release is described by Jez Humble and Dave Farley in the book

[Continuous
Delivery](http://martinfowler.com/books/continuousDelivery.html).

</p>

In [this
talk](http://www.infoq.com/presentations/Facebook-Release-Process),

Chuck Rossi describes Facebook's release process and their use of canary

releases in more detail.

</p>
<p>

</div>

</p>

<div class="acknowledgements">

</p>

Acknowledgements
----------------

</p>

Thanks to many ThoughtWorks colleagues for their feedback: Jez Humble,

Rohith Rajagopal, Charles Haynes, Andrew Maddison, Mark Taylor, Sunit

Parekh, and Sam Newman.

</p>
<p>

</div>

</p>

<div class="footnote-list">

</p>

Notes
-----

</p>

<div id="footnote-origin" class="footnote-list-item">

</p>

<span class="num">1:</span>

The name for this technique originates from miners who would carry a

canary in a cage down the coal mines. If toxic gases leaked into the
mine,

it would kill the canary before killing the miners. A canary release

provides a similar form of early warning for potential problems before

impacting your entire production infrastructure or user base.

</p>
<p>

</div>

</p>

<div id="footnote-cluster-immune-system" class="footnote-list-item">

</p>

<span class="num">2:</span>

The technique of monitoring business metrics and automatically rolling

back a release on a statistically significant regression is known as

a **cluster immune system** and was pioneered by IMVU. They

describe this and other practices in their Continuous Deployment
approach

in this [blog
post](http://engineering.imvu.com/2010/04/09/imvus-approach-to-integrating-quality-assurance-with-continuous-deployment/).

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/CanaryRelease.html&text=Bliki:%20CanaryRelease "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/CanaryRelease.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/CanaryRelease.html "Share on Google Plus")

</p>

