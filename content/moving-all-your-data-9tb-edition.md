Title: Moving All Your Data, 9TB Edition
Date: 2015-03-09 00:00
Slug: moving-all-your-data-9tb-edition

At GitLab B.V. we are working on an infrastructure upgrade to give more
CPU

power and storage space to GitLab.com. (We are currently still running
on a

[single
server](https://about.gitlab.com/2015/01/03/the-hardware-that-powers-100k-git-repos/).)
As a

part of this upgrade we wanted to move gitlab.com from our own dedicated

hardware servers to an AWS data center 400 kilometers away. In this blog
post

I will tell you how I did that and what challenges I had to overcome. An
epic

adventure of hand-rolled network tunnels, advanced DRBD features and
streaming

9TB of data through SSH pipes!

</p>

