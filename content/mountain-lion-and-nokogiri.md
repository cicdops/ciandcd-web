Title: Mountain Lion and Nokogiri
Date: 2012-08-15 00:12
Slug: mountain-lion-and-nokogiri

Today was the day I attempted the upgrade to Mountain Lion. Upgrading

all the way from Snow Leopard (long story). The tedious first step is

making sure I have backups, usually multiple backups, in addition to

the ones I keep by default. Computers hate me, so I’ve learned to be

paranoid.

</p>

My first serious hitch was with Aperture. I’d bought a download ages

ago, when the route was to download a trial version and buy a product

key. I still have the key, but there’s no place to download the trial

version from. Fortunately there was a very helpful man on Apple’s

telephone support who solved that one. +1 to him for being so helpful,

but -2 for Apple for making it hard in the first place.

</p>

My more serious trouble was with Nokogiri, ruby’s XML processing

library. Since almost all my website is XML transformed to HTML via

Nokogiri and Ruby, this is rather crucial to me. But I had no end of

trouble finding some way to get Nokogiri to install and work. Looking

out on the web there are several pages of advice, with different

combinations of animals to sacrifice in various orders.

</p>

In the end I got it working, but not in such a way that I have a

confident trail for others to follow. I installed XCode command line

tools, later the full XCode itself (don’t know if that was a factor).

I initially used homebrew for supporting libraries but without success.
I tried using

rvm, but it failed (and I backed it out). In the end I installed libxml2

and libxslt using Macports and got it all working on the installed

ruby 1.8.7.

</p>

I can only hope that this is just early days of Mountain Lion, but the

situation is really too messy. It’s very troubling that the default

install of ruby is still the elderly 1.8.7. I do need to share my

scripts from time to time with others who are not active rubyists. It

would be nice if there was a simpler installation process for them

than my worry-ridden afternoon. I find myself pining for

the days of the one-click windows install.

</p>

