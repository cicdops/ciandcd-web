Title: Retreaded: StranglerApplication
Date: 2014-06-30 13:19
Slug: retreaded-stranglerapplication

[Retread](http://martinfowler.com/bliki/Retread.html) of post orginally
made on 29 Jun 2004

</p>

When Cindy and I went to Australia, we spent some time in the

rain forests on the Queensland coast. One of the natural wonders of

this area are the huge strangler vines. They seed in the upper

branches of a fig tree and gradually work their way down the tree

until they root in the soil. Over many years they grow into fantastic

and beautiful shapes, meanwhile strangling and killing the tree that

was their host.

</p>

This metaphor struck me as a way of describing a way of doing a

rewrite of an important system. Much of my career has involved

rewrites of critical systems. You would think such a thing as easy -

just make the new one do what the old one did. Yet they are always

much more complex than they seem, and overflowing with risk. The big

cut-over date looms, the pressure is on. While new features (there are

always new features) are liked, old stuff has to remain. Even old bugs

often need to be added to the rewritten system.

</p>

An alternative route is to gradually create a new system around

the edges of the old, letting it grow slowly over several years until

the old system is strangled. Doing this sounds hard, but increasingly

I think it's one of those things that isn't tried enough. In

particular I've noticed a couple of basic strategies that work well.

The fundamental strategy is
[EventInterception](http://martinfowler.com/bliki/EventInterception.html),
which

can be used to gradually move functionality to the strangler and to

enable [AssetCapture](http://martinfowler.com/bliki/AssetCapture.html).

</p>

My colleague [Chris
Stevenson](https://twitter.com/#!/search/%22chris%20stevenson%22z/)

was involved in a project that did this recently with a great deal of

success. They published a
<a href="http://cdn.pols.co.uk/papers/agile-approach-to-legacy-systems.pdf">first

paper</a> on this at [XP 2004](http://www.xp2004.org/), and

I'm hoping for more that describe more aspects of this project. They

aren't yet at the point where the old application is strangled - but

they've delivered valuable functionality to the business that gives

the team the credibility to go further. And even if they stop now,

they have a huge return on investment - which is more than many

cut-over rewrites achieve.

</p>

The most important reason to consider a strangler application

over a cut-over rewrite is reduced risk. A strangler can give value

steadily and the frequent releases allow you to monitor its progress
more carefully. Many people still

don't consider a strangler since they think it will cost more - I'm

not convinced about that. Since you can use shorter release cycles

with a strangler you can avoid a lot of the unnecessary features that

cut over rewrites often generate.

</p>

There's another important idea here - when designing a new

application you should design it in such a way as to make it easier

for it to be strangled in the future. Let's face it, all we are doing

is writing tomorrow's legacy software today. By making it easy to be

strangled in the future, you are enabling the graceful fading away of

today's work.

</p>

<div class="furtherReading">

</p>

Further Reading
---------------

</p>

Paul Hammant has a [good summary of case
studies](http://paulhammant.com/2013/07/14/legacy-application-strangulation-case-studies/)
using this approach.

</p>
<p>

</div>

</p>

reposted on 30 Jun 2014

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/StranglerApplication.html&text=Bliki:%20StranglerApplication "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/StranglerApplication.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/StranglerApplication.html "Share on Google Plus")

</p>

