Title: APIs should not be copyrightable
Date: 2014-12-16 16:00
Slug: apis-should-not-be-copyrightable

<div class="paperBody">

</p>

Last month, the Electronic Frontier Foundation (EFF)

<a href="https://www.eff.org/press/releases/computer-scientists-ask-supreme-court-rule-apis-cant-be-copyrighted">filed

an amicus brief with the Supreme Court of the United States</a>, asking
the

justices to review an earlier lower court decision that allows

APIs (Application Programming Interfaces) to be copyrightable. I'm

one of the 77 software professionals who signed the brief,

although rather intimidated by a group that includes Abelson &

Sussman, Aho & Ullman, Josh Bloch, Fred Brooks, Vint Cerf,

Peter Deutsch, Mitch Kapor, Alan Kay, Brian Kernighan, Barbara

Liskov, Guido van Rossum, Bruce Schneier, and Ken Thompson.

</p>

<div class="fullPhoto" style="width: 400px;">

</p>
![](http://martinfowler.com/articles/./images/copyright-api/sketch.png)

</p>
<p>

</div>

</p>

The original lawsuit was brought by Oracle against Google,

claiming that Oracle held a copyright on the Java APIs, and that

Google infringed these APIs when they built Android. My support in

this brief has nothing to do with the details of the dispute

between these two tech giants, but everything to do with the

question of how intellectual property law should apply to

software, particularly software interfaces.

</p>

I'm not part of the thinking that asserts that nothing in

software should be intellectual property. While I do think that

<a href="http://martinfowler.com/articles/bliki/SoftwarePatent.html">software
patents are inherently

broken</a>, copyright is a good mechanism to allow software

authors to have some degree of control over of what happens with their
hard work.

</p>

Software has always been a tricky source of income, because

it's trivial to copy. Copyright provides a legal basis to control at
least

some copying. Without something like this, it

becomes very hard for someone to work on creating things and still

be able to pay the mortgage. While we all like free stuff, I think

it's only fair to give people the chance to earn a living from the

work they do.

</p>

But any intellectual property mechanism has to balance this

benefit with the danger that excessive intellectual property

restrictions can impede further innovation, whether that be

extending an invention, or reimagining a creative work. As a

result, patent and copyright regimes have some form of limitation

built in. One limitation is one of time: patents and copyrights

expire (although the
<a href="http://artlawjournal.com/mickey-mouse-keeps-changing-copyright-law//">Mickey
Mouse

discontinuity</a> is threatening that).

</p>

Interfaces are how things plug together. An example from the

physical world is cameras with interchangeable lenses. Many camera

makers don't encourage other companies to make lenses for their

cameras, but such third-party companies can reverse-engineer how

the interface works and build a lens that will mount on a camera.

We regularly see this happen with third-party parts providers -

and these third parties do a great deal to provide lower costs and

features that the main company doesn't support. I used a Sigma

lens with my Canon camera because Canon didn't (at the time)

make an 18-200mm lens. I've bought third party batteries for

cameras because they're cheaper. Similarly I've repaired my car with
third party

parts again to lower costs or get an audio system that better

matched my needs.

</p>

Software interfaces are much the same, and the ability to

extend open interfaces, or reverse-engineer interfaces, has played

a big role in advancing software systems. Open interfaces were a

vital part of allowing the growth of the internet, nobody has to

pay a copyright licence to build a HTTP server, nor to connect to

one. The growth of Unix-style operating systems relied greatly on

the fact that although much of the source code for AT&T's Unix

was copyrighted, the interfaces were not. This allowed offshoots

such as BSD and Linux to follow Unix's interfaces, which helped

these open-source systems to get traction by making it easier for

programs built on top of Unix to interact with new

implementations.

</p>

<p>
> A picture is worth a 1000 words, so here's a picture of some books
> written by signatories of the EFF amicus brief [-- Josh
> Bloch](https://twitter.com/joshbloch/status/531937881703452673)
> </p>
> <p>

</p>

The story of SMB and Samba is a good example of how

non-copyrightable APIs spurred competition. When Windows became a

dominent desktop operating system, its SMB protocol dominated

simple networks. If non-windows computers wanted to communicate

effectively with the dominant windows platform, they needed to

talk to SMB. Microsoft didn't provide any documentation to help

competitors do this, since an inability to communicate with SMB

was a barrier to their competitors. However, Andrew Tridgell was

able to deduce the specification for SMB and build an

implementation for Unix, called Samba. By using Samba non-windows

computers could collaborate on a network, thus encouraging the

competition from Mac and Linux based systems. A similar story

happened years before with the IBM BIOS, which was

reverse-engineered by competitors.

</p>

The power of a free-market system comes from competition, the

notion that if I can find a way to bake bread that's either

cheaper or tastier than my local bakers, I can start a bakery and

compete with them. Over time my small bakery can grow and compete

with the largest bakers. For this to work, it's vital that we

construct the market so that existing players that dominate the

market cannot build barriers to prevent new people coming in with

innovations to reduce cost or improve quality.

</p>

Software interfaces are critical points for this with software.

By keeping interfaces open, we encourage a competitive

marketplace of software systems that encourage innovation to

provide more features and reduce costs. Closing this off will

lead to incompatible islands of computer systems, unable to

communicate.

</p>

Such islands of incompatibility present a considerable barrier

to new competitors, and are bad for that reason alone. But it's

they are bad for users too. Users value software

that can work together, and even if the various vendors of

software aren't interested in communication, we should encourage

other providers to step in and fill the gaps. Tying systems

together requires open interfaces, so that integrators can safely

implement an interface in order to create communication links. We

value standard connectors in the physical world, and while

software connections are often too varied for everything to be

standardized, we shouldn't use copyright law to add further hurdles.

</p>

The need to implement interfaces also goes much deeper than

this. As programmers we often have to implement interfaces defined

outside our code base in order to do our jobs. It's common to have

to modify software that was written with one library in mind to

work with another - a useful way to do this is to write
[adapters](http://www.amazon.com/gp/product/0201634988?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0201634988)![](http://www.assoc-amazon.com/e/ir?t=martinfowlerc-20&l=as2&o=1&a=0321601912)
that implement the interface of the

first library by forwarding the second. Implementing interfaces is

also vital in testing, as it allows you to create [Test
Doubles](http://martinfowler.com/bliki/TestDouble.html).

</p>

So for the sake of our ability to write programs properly, our

users' desire to have software work together, and for society's

desire for free markets that spur competition — copyright should

not be used for APIs.

</p>

* * * * *

</p>
<p>

</div>

</p>

<div class="appendix">

</p>

<div id="Acknowledgements">

</p>

* * * * *

</p>

Acknowledgements
----------------

</p>

Derek Hammer raised the point that implementing interfaces

for adapters and testing is a regular part of programming.

Andy Slocum, Jason Pfetcher, Jonathan Reyes, Josh Bloch, and

Michael Barclay

commented on drafts of this article. Extra thanks to Josh Bloch for

helping to organize the 77 of us who signed the brief.

</p>
<p>

</div>

</p>
<p>

</div>

</p>

