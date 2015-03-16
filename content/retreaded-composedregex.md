Title: Retreaded: ComposedRegex
Date: 2014-07-31 12:26
Slug: retreaded-composedregex

[Retread](http://martinfowler.com/bliki/Retread.html) of post orginally
made on 24 Jul 2009

</p>

One of the most powerful tools in writing maintainable code is

break large methods into well-named smaller methods - a technique

Kent Beck refers to as the Composed Method pattern.

</p>

<p>
> </p>
>
> People can read your programs much more quickly and accurately
>
> if they can understand them in detail, then chunk those details
>
> into higher level structures.
>
> </p>
>
> [-- Kent
> Beck](http://www.amazon.com/Smalltalk-Best-Practice-Patterns-Kent/dp/013476904X)
>
> </p>
> <p>

</p>

What works for methods often works for other things as well. One

area that I've run into a couple of times where people fail to do

this is with regular expressions.

</p>

Let's say you have a file full of rules for scoring frequent

sleeper points for a hotel chain. The rules all look rather like:

</p>

<p>
    score 400 for 2 nights at Minas Tirith Airport  

</p>

We need to pull out the points (400) the number of nights (2) and

the hotel name (Minas Tirith Airport) for each of these rows.

</p>

This is an obvious task for a regex, and I'm sure right now

you're thinking - oh yes we need:

</p>

<p>
    const string pattern =   @"^score\s+(\d+)\s+for\s+(\d+)\s+nights?\s+at\s+(.*)";

</p>

Then our three values just pop out of the groups.

</p>

I don't know whether or not you're comfortable in understanding

how that regex works and whether it's correct. If you're like me you

have to look at a regex like this and carefully figure out what it's

saying. I often find myself counting parentheses so I can see where

the groups line up (not actually that hard in this case, but I've

seen plenty of others where it's tougher).

</p>

You may have read advice to take a pattern like this and to

comment it. (Often needs a switch when you turn it into a regex.)

That way you can write it like this.

</p>

<p>
        protected override string GetPattern() {      const string pattern =        @"^score        \s+          (\d+)          # points        \s+        for        \s+        (\d+)          # number of nights        \s+        night        s?             #optional plural        \s+        at        \s+        (.*)           # hotel name        ";        return pattern;    }  }  

</p>

This is easier to follow, but comments never quite satisfy

me. Occasionally I've been accused of saying comments are bad, and

that you shouldn't use them. This is wrong, in both senses.

Comments are not bad - but there are often better options. I always

try to write code that doesn't need comments, usually by good

naming and structure. (I can't always succeed, but I feel I do more

often than not.)

</p>

People often don't try to structure regexs, but I find it

useful. Here's one way of doing this one.

</p>

<p>
        const string scoreKeyword = @"^score\s+";    const string numberOfPoints = @"(\d+)";    const string forKeyword = @"\s+for\s+";    const string numberOfNights = @"(\d+)";    const string nightsAtKeyword = @"\s+nights?\s+at\s+";    const string hotelName = @"(.*)";    const string pattern =  scoreKeyword + numberOfPoints +      forKeyword + numberOfNights + nightsAtKeyword + hotelName;  

</p>

I've broken down the pattern into logical chunks and put them

together again at the end. I can now look at that final expression

and understand the basic chunks of the expression, diving into the

regex for each one to see the details.

</p>

Here another alternative that seeks to separate the whitespace to

make the actual regexs look more like tokens.

</p>

<p>
        const string space = @"\s+";    const string start = "^";    const string numberOfPoints = @"(\d+)";    const string numberOfNights = @"(\d+)";    const string nightsAtKeyword = @"nights?\s+at";    const string hotelName = @"(.*)";    const string pattern =  start + "score" + space + numberOfPoints + space +      "for" + space + numberOfNights + space + nightsAtKeyword +        space + hotelName;  

</p>

I find this makes the individual tokens a bit clearer, but all

those space variables makes the overall structure harder to

follow. So I prefer the previous one.

</p>

But this does raise a question. All of the elements are separated

by space, and putting in lots of space variables or `\s+`

in the patterns feels wet. The nice thing about breaking out the

regexs into sub-strings is that I can now use the programming logic

to come up with abstractions that suit my particular purpose

better. I can write a method that will take sub strings and join

them up with whitespace.

</p>

<p>
        private String composePattern(params String[] arg) {      return "^" + String.Join(@"\s+", arg);    }  

</p>

Using this method, I then have.

</p>

<p>
        const string numberOfPoints = @"(\d+)";    const string numberOfNights = @"(\d+)";    const string hotelName = @"(.*)";    const string pattern =  composePattern("score", numberOfPoints,       "for", numberOfNights, "nights?", "at", hotelName);  

</p>

You may not use exactly any of these alternative yourself, but I

do urge you to think about how to make regular expressions

clearer. Code should not need to be figured out, it should be just

read.

</p>

* * * * *

<div id="Updates">

</p>

* * * * *

</p>

Updates
-------

</p>

In this discussion I've made the elements for the composed

regexs be local variables. A variation is to take commonly used

regex elements and use them more widely. This can be handy to use

common regexs that are needed in lots of places. My colleague

Carlos Villela comments that one thing to watch out for is if

these fragments are not well-formed, ie having an opening

parenthesis that's closed in another fragment. This can be tricky

to debug. I've not felt the need to do it, so haven't run into

this problem.

</p>

A few people mentioned using fluent interfaces (internal DSLs)

as an more readable
<a href="http://flimflan.com/blog/ReadableRegularExpressions.aspx">alternative

to regexs</a>. I see this as a separate thing. Regexs don't bother

me if they are small, indeed I prefer a small regex to an

equivalent fluent interface. It's the composition that counts,

which you can do with either technique.

</p>

Some others mentioned named capture groups. Like comments, I

find these are better than the raw regex, but still find a

composed structure more readable. The point of composition is that

it breaks the overall regex into small pieces that are easier to

understand.

</p>
<p>

</div>

</p>

reposted on 31 Jul 2014

</p>

<span
class="label">Share:</span>[![](http://martinfowler.com/t_mini-a.png)](https://twitter.com/intent/tweet?url=http://martinfowler.com/bliki/ComposedRegex.html&text=Bliki:%20ComposedRegex "Share on Twitter")[![](http://martinfowler.com/fb-icon-20.png)](https://facebook.com/sharer.php?u=http://martinfowler.com/bliki/ComposedRegex.html "Share on Facebook")[![](http://martinfowler.com/gplus-16.png)](https://plus.google.com/share?url=http://martinfowler.com/bliki/ComposedRegex.html "Share on Google Plus")

</p>

