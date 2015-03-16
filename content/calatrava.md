Title: Calatrava
Date: 2012-10-15 14:07
Slug: calatrava

<div class="img floating">

[![](http://martinfowler.com/snips/calatrava-logo.png)](http://martinfowler.com/snips/201210151007.html)

</div>

</p>

A couple of months ago I wrote an
<a href="http://martinfowler.com/articles/multiMobile">infodeck about
developing mobile

applications for multiple devices</a>. A core point of the deck is that

for the best user-experience you need several native applications, but
this

is expensive. To reduce cost a mobile web application works on all

suitable devices, but a web-app limits your user-interface. The result

is an unavoidable choice between user-experience and cost.

</p>

While we can’t make that trade-off go away, we can turn a binary

choice into a more graduated scale by developing hybrid applications

that mix web and native technologies. At ThoughtWorks we’ve been

pursuing this path on various client projects, with some success.

We’ve now developed enough understanding on how to approach a hybrid

application to make it worth sharing some code, so we recently

released Calatrava, which is a framework to enable this web-native

interoperation.

</p>

Calatrava is suitable for applications with significant client-side

domain logic and when the application a channel for your product

rather than the product itself. It is not suitable if most of your

code is UI code (such as a game) or if a web app provides a

sufficiently good user-experience. Calatrava is probably most valuable

when you want to pursue an incremental release strategy, such as

[cover-your-bases](http://martinfowler.com/articles/mobileImplStrategy.html#cover-your-bases).

</p>

For more information look at the [calatrava home page on
github](http://calatrava.github.com/), and the

[launch announcement by maintainer Giles
Alexander](http://overwatering.org/blog/2012/10/announcing-calatrava/).
There’s also an

overview on a [single infodeck
slide](http://martinfowler.com/articles/multiMobile/#calatrava).

</p>

