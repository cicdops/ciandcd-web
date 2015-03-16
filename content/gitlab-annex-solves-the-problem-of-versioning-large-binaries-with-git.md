Title: GitLab Annex Solves the Problem of Versioning Large Binaries With Git
Date: 2015-02-17 00:00
Slug: gitlab-annex-solves-the-problem-of-versioning-large-binaries-with-git

The biggest limitation of git compared to some older centralized version
control systems has been the maximum size of the repositories.

The general recommendation is to not have git repositories larger than
1GB to preserve performance.

Although GitLab has no limit (some repositories in GitLab are over
50GB!) we subscribe to the advice to keep repositories as small as you
can.

</p>

Not being able to version control large binaries is a big problem for
many larger organizations.

Video, photo's, audio, compiled binaries and many other types of files
are too large.

As a workaround, people keep artwork-in-progress in a Dropbox folder and
only check in the final result.

This results in using outdated files, not having a complete history and
the risk of losing work.

</p>

In GitLab 7.8 Enterprise Edition this problem is solved by integrating
the awesome [git-annex](https://git-annex.branchable.com/).

Git-annex allows managing large binaries with git, without checking the
contents into git.

You check in only a symlink that contains the SHA-1 of the large binary.

If you need the large binary you can sync it from the GitLab server over
rsync, a very fast file copying tool.

</p>

<div class="download-partial hidden-xs">

</p>
Install GitLab on your own server in 2 minutes

[Let’s do it!](https://about.gitlab.com/downloads)

<p>

</div>

</p>

<a class="btn btn-block btn-lg btn-purple visible-xs" href="https://about.gitlab.com/downloads" id="dl-partial-sm">

Install GitLab on your own server in 2 minutes

</a>

</p>

