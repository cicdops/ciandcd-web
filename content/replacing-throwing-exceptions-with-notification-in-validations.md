Title: Replacing Throwing Exceptions with Notification in Validations
Date: 2014-12-09 14:41
Slug: replacing-throwing-exceptions-with-notification-in-validations

<div class="img">

[![](http://martinfowler.com/articles/replaceThrowWithNotification/sketch.png)](http://martinfowler.com/articles/replaceThrowWithNotification.html)

</div>

If you’re validating some data, you usually shouldn’t be using
exceptions to signal validation failures. Here I describe how I’d
refactor such code into using the Notification pattern.

</p>

