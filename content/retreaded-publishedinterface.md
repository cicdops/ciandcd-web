Title: Retreaded: PublishedInterface
Date: 2012-05-03 14:18
Slug: retreaded-publishedinterface

[Retread](http://martinfowler.com/bliki/Retread.html) of post orginally
made on 26 Dec 2003

</p>

*Published Interface* is a term I used (first in
[Refactoring](http://martinfowler.com/books/refactoring.html))

to refer to a class interface that's used outside the code base that

it's defined in. As such it means more than public in Java and indeed

even more than a non-internal public in C\#. In my column for IEEE

Software I argued

that <a href="http://martinfowler.com/ieeeSoftware/published.pdf">the
distinction between published and public is actually more

important than that between public and private.</a>

</p>

The reason is that with a non-published interface you can change

it and update the calling code since it is all within a single code

base. Such things as renames can be done, and done easily with modern

refactoring tools. But anything published so you can't reach the

calling code needs more complicated treatment.

</p>

reposted on 03 May 2012

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/PublishedInterface.html&text=Bliki:%20PublishedInterface "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/PublishedInterface.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/PublishedInterface.html "Share on Google Plus")

</p>

