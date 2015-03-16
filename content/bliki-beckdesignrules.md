Title: Bliki: BeckDesignRules
Date: 2015-03-02 14:20
Tags: bliki
Slug: bliki-beckdesignrules

Kent Beck came up with his four rules of simple design while he

was developing
[ExtremeProgramming](http://martinfowler.com/bliki/ExtremeProgramming.html)
in the late 1990's. I express

them like this.
[[1]](http://martinfowler.com/feed.atom#footnote-xp-formulation)

</p>

-   Passes the tests
-   Reveals intention
-   No duplication
-   Fewest elements

The rules are in priority order, so "passes the tests" takes

priority over "reveals intention"

</p>

<div class="photo right" style="width: 200px;">

</p>
![](http://martinfowler.com/bliki/images/beckDesignRules/kent.jpg)

<i>

Kent Beck developed Extreme Programming, Test Driven Development,

and can always be relied on for good Victorian facial hair for his

local ballet.

</i>

</p>
<p>

</div>

</p>

The most important of the rules is "passes the tests". XP was

revolutionary in how it raised testing to a first-class activity in

software development, so it's natural that testing should play a

prominent role in these rules. The point is that whatever else you

do with the software, the primary aim is that it works as

intended and tests are there to ensure that happens.

</p>

"Reveals intention" is Kent's way of saying the code

should be easy to understand. Communication is a core value of

Extreme Programing, and many programmers like to stress that

programs are there to be read by people. Kent's form of expressing

this rule implies that the key to enabling understanding is to express
your

intention in the code, so that your readers can understand what your

purpose was when writing it.

</p>

The "no duplication" is perhaps the most powerfully subtle of

these rules. It's a notion expressed elsewhere as DRY or SPOT
[[2]](http://martinfowler.com/feed.atom#footnote-dry), Kent

expressed it as saying everything should be said "Once and only Once."

Many programmers have observed that the exercise of eliminating

duplication is a powerful way to drive out good designs.
[[3]](http://martinfowler.com/feed.atom#footnote-dup-column)

</p>

The last rule tells us that anything that doesn't serve the three

prior rules should be removed. At the time these rules were

formulated there was a lot of design advice around adding elements to

an architecture in order to increase flexibility for future
requirements.

Ironically the extra complexity of all of these elements usually

made the system harder to modify and thus less flexible in practice.

</p>

People often find there is some tension between "no duplication"

and "reveals intention", leading to arguments about which order

those rules should appear. I've always seen their order as

unimportant, since they feed off each other in refining the code. Such
things

as adding duplication to increase clarity is often papering over a
problem,

when it would be better to solve it.
[[4]](http://martinfowler.com/feed.atom#footnote-kent-empathy)

</p>

<div class="photo" style="width: 500px;">

</p>
![](http://martinfowler.com/bliki/images/beckDesignRules/sketch.png)

</p>
<p>

</div>

</p>

What I like about these rules is that they are very simple to

remember, yet following them improves code in any language or

programming paradigm that I've worked with. They are an example of

Kent's skill in finding principles that are generally applicable and

yet concrete enough to shape my actions.

</p>

<p>
> </p>
>
> At the time there was a lot of “design is subjective”, “design is
>
> a matter of taste” bullshit going around. I disagreed. There are
>
> better and worse designs. These criteria aren’t perfect, but they
>
> serve to sort out some of the obvious crap and (importantly) you can
>
> evaluate them right now. The real criteria for quality of design,
>
> “minimizes cost (including the cost of delay) and maximizes benefit
>
> over the lifetime of the software,” can only be evaluated post hoc,
>
> and even then any evaluation will be subject to a large bag full of
>
> cognitive biases. The four rules are generally predictive.
>
> </p>
>
> -- Kent Beck
>
> </p>
> <p>

</p>

<div class="furtherReading">

</p>

Further Reading
---------------

</p>

There are many expressions of these rules out there, here are a

few that I think are worth exploring:

</p>

-   </p>
    <a href="http://www.jbrains.ca/permalink/the-four-elements-of-simple-design">J.B.

    Rainsberger's summary</a>. He also has a good discussion of
    <a href="http://blog.thecodewhisperer.com/2013/12/07/putting-an-age-old-battle-to-rest/">the

    interplay between the rules 2&3.</a>

    <p>
-   [Ron Jeffries](http://xprogramming.com/classics/expemergentdesign/)
-   These rules, like much else of Extreme Programming, were
    </p>
    <p>
    originally discussed and refined [on Ward's
    Wiki](http://c2.com/cgi/wiki?XpSimplicityRules).

</p>
<p>

</div>

</p>

<div class="acknowledgements">

</p>

Acknowledgements
----------------

</p>

Kent reviewed this post and sent me some very helpful feedback,

much of which I appropriated into the text.

</p>
<p>

</div>

</p>

<div class="footnote-list">

</p>

Notes
-----

</p>

<div id="footnote-xp-formulation" class="footnote-list-item">

</p>

### 1: Authoritative Formulation {.head-text}

</p>

There are many expressions of the four rules out there,

Kent stated them in lots of media, and plenty of other people

have liked them and phrased them their own way. So you'll see

plenty of descriptions of the rules, but each author has their

own twist - as do I.

</p>

If you want an authoritative formulation from the man

himself, probably your best bet is from the first edition of

<a href="http://www.amazon.com/gp/product/0201616416?ie=UTF8&amp;tag=martinfowlerc-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0201616416">The

White
Book</a>![](http://www.assoc-amazon.com/e/ir?t=martinfowlerc-20&l=as2&o=1&a=0321601912)
(p 57) in the section that outlines the XP practice

of Simple Design.

</p>

-   Runs all the tests
-   Has no duplicated logic. Be wary of hidden duplication like
    </p>
    <p>
    parallel class hierarchies
-   States every intention important to the programmer
-   Has the fewest possible classes and methods

</p>

(Just to be confusing, there's another formulation on page

109 that omits "runs all the tests" and splits "fewest classes"

and "fewest methods" over the last two rules. I recall this was

an earlier formulation that Kent improved on while writing the

White Book.)

</p>
<p>

</div>

</p>

<div id="footnote-dry" class="footnote-list-item">

</p>

<span class="num">2:</span>

DRY stands for Don't Repeat Yourself, and comes from [The Pragmatic
Programmer](http://www.amazon.com/gp/product/020161622X?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=020161622X)![](http://www.assoc-amazon.com/e/ir?t=martinfowlerc-20&l=as2&o=1&a=0321601912).
SPOT stands

for
<a href="http://www.catb.org/~esr/writings/taoup/html/ch04s02.html#spot_rule">Single

Point Of Truth</a>.

</p>
<p>

</div>

</p>

<div id="footnote-dup-column" class="footnote-list-item">

</p>

<span class="num">3:</span>

This principle was the basis of my [first design column for IEEE
Software](http://martinfowler.com/ieeeSoftware/repetition.pdf).

</p>
<p>

</div>

</p>

<div id="footnote-kent-empathy" class="footnote-list-item">

</p>

<span class="num">4:</span>

When reviewing this post, Kent said "In the rare case they are

in conflict (in tests are the only examples I can recall),

empathy wins over some strictly technical metric." I like his

point about empathy - it reminds us that when writing code we

should always be thinking of the reader.

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/BeckDesignRules.html&text=Bliki:%20BeckDesignRules "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/BeckDesignRules.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/BeckDesignRules.html "Share on Google Plus")

</p>

