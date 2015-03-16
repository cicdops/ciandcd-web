Title: Bliki: SelfTestingCode
Date: 2014-05-01 13:50
Tags: bliki
Slug: bliki-selftestingcode

Self-Testing Code is the name I used in
[Refactoring](http://martinfowler.com/books/refactoring.html) to refer
to the practice

of writing comprehensive automated tests in conjunction with the

functional software. When done well this allows you to invoke a

single command that executes the tests - and you are confident that

these tests will illuminate any bugs hiding in your code.

</p>
![](http://martinfowler.com/bliki/images/selfTestingCode/sketch.png)

I first ran into the thought at an OOPSLA conference listening to

["Beddara" Dave Thomas](http://www.davethomas.net) say

that every object should be able to test itself. I suddenly had the

vision of typing a command and having my whole software system do a

self-test, much in the way that you used to see hardware memory tests
when

booting. Soon I was exploring this approach in my own projects and being

very happy with the benefits. A couple of years later I did some

work with Kent Beck and discovered he did the same thing, but in a

much more sophisticated way than I did. This was shortly before Kent

(and Erich Gamma) produced JUnit - a tool that became the

underpinning of much of thinking and practice of self-testing code

(and its sister:
[TestDrivenDevelopment](http://martinfowler.com/bliki/TestDrivenDevelopment.html)).

</p>

You have self-testing code when you can run a series of automated

tests against the code base and be confident that, should the tests

pass, your code is free of any substantial defects. One way I think

of it is that as well as building your software system, you

simultaneously build a bug detector that's able to detect any faults

inside the system. Should anyone in the team accidentally introduce

a bug, the detector goes off. By running the test suite frequently,

at least several times a day, you're able to detect such bugs soon

after they are introduced, so you can just look in the recent

changes, which makes it *much* easier to find them. No

programming episode is complete without working code and the tests

to keep it working. Our attitude is to assume that any non-trivial

code without tests is broken.

</p>

Self-testing code is a key part of [Continuous
Integration](http://martinfowler.com/articles/continuousIntegration.html),

indeed I say that you aren't really doing continuous integration

unless you have self-testing code. As a pillar of Continuous

Integration, it is also a necessary part of [Continuous
Delivery](http://martinfowler.com/delivery.html).

</p>

One obvious benefit of self-testing code is that it can

drastically reduce the number of bugs that get into production

software. At the heart of this is building up a testing culture that

where developers are naturally thinking about writing code and tests

together.

</p>

But the biggest benefit isn't about merely avoiding production

bugs, it's about the confidence that you get to make changes to the

system. Old codebases are often terrifying places, where developers

fear to change working code. Even fixing a bug can be dangerous,

because you can create more bugs than you fix. In such circumstances

not just is it horribly slow to add more features, you also end up

afraid to refactor the system, thus increasing
[TechnicalDebt](http://martinfowler.com/bliki/TechnicalDebt.html), and

getting into a steadily worsening spiral where every change makes

people more fearful of more change.

</p>

With self-testing code, it's a different picture. Here people are

confident that fixing small problems to clean the code can be done

safely, because should you make a mistake (or rather "when I make a

mistake") the bug detector will go off and you can quickly recover

and continue. With that safety net, you can spend time keeping the

code in good shape, and end up in a virtuous spiral where you get

steadily faster at adding new features.

</p>

These kinds of benefits are often talked about with respect to

[TestDrivenDevelopment](http://martinfowler.com/bliki/TestDrivenDevelopment.html)
(TDD), but it's useful to separate

the concepts of TDD and self-testing code. I think of TDD as a

particular practice whose benefits include producing self-testing

code. It's a great way to do it, and TDD is a technique I'm a big

fan of. But you can also produce self-testing code by writing tests

after writing code - although you can't consider your work to be

done until you have the tests (and they pass). The important point

of self-testing code is that you have the tests, not how you got to

them.

</p>

Increasingly these days we're seeing another dimension to

self-testing, with more emphasis put on monitoring in production.
[Continuous Delivery](http://martinfowler.com/delivery.html) allows you
to

quickly deploy new versions of software into production. In this

situation teams put more effort into spotting bugs once

in production and rapidly fixing them by either deploying a new

fixed version or rolling back to the last-known-good version.

</p>

<div class="appendix">

</p>
This entry was originally published (in a much smaller form) on

May 5th 2005.

<p>

</div>

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/SelfTestingCode.html&text=Bliki:%20SelfTestingCode "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/SelfTestingCode.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/SelfTestingCode.html "Share on Google Plus")

</p>

