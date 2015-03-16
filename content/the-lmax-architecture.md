Title: The LMAX Architecture
Date: 2011-07-12 13:43
Slug: the-lmax-architecture

When I was at QCon London last year, there was much buzz around a talk

about a new retail trading system. The thing that got people’s

attention was its approach to achieving its high performance needs -

reaching 6 million TPS. It does this by running all its business logic

on a single JVM thread, getting high speed without all the

complications of concurrent programming. This article describes the

architecture they use to pull this off.

</p>

