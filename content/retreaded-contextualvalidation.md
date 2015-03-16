Title: Retreaded: ContextualValidation
Date: 2011-11-03 15:00
Slug: retreaded-contextualvalidation

[Retread](http://martinfowler.com/bliki/Retread.html) of post orginally
made on 07 Dec 2005

</p>

In my writing endeavors, I've long intended to write a chunk of

material on validation. It's an area that leads to a lot of

confusion and it would be good to get some solid description of some

of the techniques that work well. However life is full of things to

write about, rather more than time allows.

</p>

Some recent readings made me think about saying a few

preliminary things on the topic. One common thing I see people do

is to develop validation routines for objects. These routines come

in various ways, they may be in the object or external, they may

return a boolean or throw an exception to indicate failure. But one

thing that I think constantly trips people up is when they think

object validity on a context independent way such as an `isValid`

method implies.

</p>

I think it's much more useful to think of validation as something

that's bound to a context - typically an action that you want to do.

Is this order valid to be filled, is this customer valid to check in

to the hotel. So rather than have methods like `isValid`

have methods like `isValidForCheckIn`.

</p>

One of the consequences of this is that saving an object to a

database is itself an action. Thinking about it that way raises some

important questions. Often when people talk about a context-free

validity, they mean it in terms of saving to a database. But the

various validity checks that make this up should be interrogated

with the question "should failing this test prevent saving?"

</p>

In [About
Face](http://www.amazon.com/gp/product/1568843224?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=1568843224)![](http://www.assoc-amazon.com/e/ir?t=martinfowlerc-20&l=as2&o=1&a=0321601912)
Alan Cooper advocated that we shouldn't let

our ideas of valid states prevent a user from entering (and saving)

incomplete information. I was reminded by this a few days ago when

reading a draft of a book that [Jimmy
Nilsson](http://www.jnsk.se/weblog/rss.xml) is working

on. He stated a principle that you should always be able to save an

object, even if it has errors in it. While I'm not convinced that this

should be an absolute rule, I do think people tend to prevent saving

more than they ought. Thinking about the context for validation may

help prevent that.

</p>

reposted on 03 Nov 2011

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/ContextualValidation.html&text=Bliki:%20ContextualValidation "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/ContextualValidation.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/ContextualValidation.html "Share on Google Plus")

</p>

