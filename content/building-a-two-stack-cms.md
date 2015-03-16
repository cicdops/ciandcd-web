Title: Building a two-stack CMS
Date: 2014-10-06 14:18
Slug: building-a-two-stack-cms

<div class="img floating">

[![](http://martinfowler.com/articles/two-stack-cms/ccs-n-cds.png)](http://martinfowler.com/articles/two-stack-cms)

</div>

Our Pune office recently did a project with a large manufacturer to
build its global marketing website. The site involved complex content,
lots of traffic (two million page views a day), localization to nearly a
hundred locales, and high availability. [In this
infodeck](http://martinfowler.com/articles/two-stack-cms) my colleague
[Sunit Parekh](http://www.sunitparekh.in/home) and I dig into a key
feature of the system - taking on the principle of [Editing-Publishing
Separation](http://martinfowler.com/bliki/EditingPublishingSeparation.html)
by building a two-stack architecture. This allowed the client to
continue to use a wide range of software for their complex content
editing needs, but at the same time providing a content delivery
platform that supported a global site with high traffic and
availability.

</p>

