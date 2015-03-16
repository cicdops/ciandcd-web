Title: Retreaded: FaultyTechniqueDichotomy
Date: 2014-08-06 13:34
Slug: retreaded-faultytechniquedichotomy

[Retread](http://martinfowler.com/bliki/Retread.html) of post orginally
made on 05 Aug 2004

</p>

My main inspiration in life is trying to capture and improve the

way in which we do software development. So I spend a lot of time

talking to people about various techniques they've used, which ones

work well and which ones suck.

</p>

As I do this, I often hear about faulty techniques: "FIT wasn't

worth the effort", "never put any logic in stored procedures", "test

driven design led to a chaotic mess". The problem with any report of a

faulty technique is to figure out if the technique itself is faulty,

or whether the application of the technique was faulty.

</p>

Let's take a couple of examples. Several friends of mine

commented how stored procedures were a disaster because they weren't

kept in version control (instead they had names like GetCust01,

GetCust02, GetCust02B etc). That's not a problem with stored

procedures, that's a problem with people not using them properly.

Similar a criticism that TDD led to a brittle design on further

questioning led to the discovery that the team in question hadn't done

any refactoring - and refactoring is a critical step in TDD.

</p>

Of course if you take all this too far, you get the opposite

effect. I often say "no methodology has ever failed". My reason for

this is that given any failure (assuming you can know

[WhatIsFailure](http://martinfowler.com/bliki/WhatIsFailure.html)) you
can find some variation from the

methodology. Hence the methodology wasn't followed and therefore

didn't fail. This issue is compounded even further with self-adaptive

agile methods.

</p>

So when you hear of techniques failing, you need to ask a lot

more questions.

</p>

-   Was it the technique itself that had problems, or was some

    </p>
    other thing being missed out. Does the technique have an influence
    on

    this? (Version control is a separate thing to stored procedures, but

    it can be harder to use version control with stored procedures due
    to

    <p>
    nature of tools involved.)

-   Was the technique used in a context that wasn't suitable for

    </p>
    it? (Don't use wide-scale manual refactoring when you don't have

    tests.) Remember that software development is a very human activity,

    often techniques aren't suitable for a context because of culture
    and

    <p>
    personality.

-   Were important pieces missed out of the technique?
-   Were people focused on outward signs that didn't correspond to

    </p>
    the reality? This kind of thing is what Steve McConnell called
    <a href="http://www.stevemcconnell.com/ieeesoftware/eic10.htm">Cargo
    Cult

    <p>
    Software Engineering</a>..

An interesting aspect of this is whether certain techniques are

fragile; that is they are hard to apply correctly and thus more prone

to a faulty application. If it's hard to use a technique properly,

that's a reasonable limitation on the technique, reducing the context

when it can be used.

</p>

There's no simple answer to this problem, since with these

techniques we are as unable to measure compliance as we are unable to

measure their successfulness. The important thing to do is whenever

you hear of a technique failing - always remember the dichotomy.

</p>

reposted on 06 Aug 2014

</p>

<div class="translations">

</p>
<p>
**Translations:**[French](http://www.autoteiledirekt.de/science/faultytechniquedichotomy)

</div>

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/FaultyTechniqueDichotomy.html&text=Bliki:%20FaultyTechniqueDichotomy "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/FaultyTechniqueDichotomy.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/FaultyTechniqueDichotomy.html "Share on Google Plus")

</p>

