Title: Git 2.3 has been released
Date: 2015-02-06 00:33
Author: mhagger
Tags: engineering
Slug: git-23-has-been-released

The Git developers have just released a major new version of the Git
command-line utility, Git 2.3.0.

</p>

As usual, this release contains many improvements, performance
enhancements, and bug fixes. Full details about what's included can be
found in the [Git 2.3.0 release
notes](https://github.com/gitster/git/blob/v2.3.0/Documentation/RelNotes/2.3.0.txt),
but here's a look at what we consider to be the coolest new features in
this release.

</p>

Push to deploy
--------------

</p>

One way to deploy a Git-based web project is to keep a checked-out
working copy on your server. When a new version is ready, you log into
the server and run `git pull` to fetch and deploy the new changes. While
this technique has some disadvantages (see below), it is very easy to
set up and use, especially if your project consists mostly of static
content.

</p>

With Git 2.3, this technique has become even more convenient. Now you
can push changes directly to the repository on your server. Provided no
local modifications have been made on the server, any changes to the
server's current branch will be checked out automatically. Instant
deploy!

</p>

To use this feature, you have to first enable it in the Git repository
on your server by running

</p>

<div class="highlight highlight-ShellSession">

    $ git config receive.denyCurrentBranch updateInstead

</div>

</p>

### When shouldn't you use push-to-deploy?

</p>

Deploying by pushing to a Git repository is quick and convenient, but it
is not for everybody. For example:

</p>

-   Your server will contain a `.git` directory containing the entire
    history of your project. You probably want to make extra sure that
    it cannot be served to users!
-   During deploys, it will be possible for users momentarily to
    encounter the site in an inconsistent state, with some files at the
    old version and others at the new version, or even half-written
    files. If this is a problem for your project, push-to-deploy is
    probably not for you.
-   If your project needs a "build" step, then you will have to set that
    up explicitly, perhaps via
    [githooks](http://git-scm.com/docs/githooks).

</p>

[See how this feature was
implemented](https://github.com/gitster/git/commit/72ecc6ef53cb2906f5efab11fa6ab26c1729f233)

</p>

Faster cloning by borrowing objects from existing clones
--------------------------------------------------------

</p>

Cloning a remote repository can involve transferring a lot of data over
the network. But if you already have another local clone of the same
repository, it probably already has most of the history that the new
clone will need. Now it is easy to use those local objects rather than
transferring them again:

</p>

<div class="highlight highlight-ShellSession">

    $ git clone --reference ../oldclone --dissociate https://github.com/gitster/git.git

</div>

</p>

The new `--dissociate` option tells Git to copy any objects it can from
local repository `../oldclone`, retrieving the remainder from the remote
repository. Afterwards, the two clones remain independent; either one
can be deleted without impacting the other (unlike when `--reference` is
used without `--dissociate`).

</p>

[See how this feature was
implemented](https://github.com/gitster/git/commit/d35c8027937546e6b22a2f28123f731c84e3b380)

</p>

<h2>
More conservative default behavior for `git push`

</p>
<p>
</h2>
</p>

If you run `git push` without arguments, Git now uses the more
conservative `simple` behavior as the default. This means that Git
refuses to push anything unless you have defined an "upstream" branch
for your current branch *and* the upstream branch has the same name as
your current branch. For example:

</p>

<div class="highlight highlight-ShellSession">

    $ git config branch.autosetupmerge true$ git checkout -b experimental origin/masterBranch experimental set up to track remote branch master from origin.Switched to a new branch 'experimental'$ git commit -a -m 'Experimental changes'[experimental 43ca356] Experimental changes$ git pushfatal: The upstream branch of your current branch does not matchthe name of your current branch.  To push to the upstream branchon the remote, use    git push origin HEAD:masterTo push to the branch of the same name on the remote, use    git push origin experimental$

</div>

</p>

The new default behavior is meant to help users avoid pushing changes to
the wrong branch by accident. In the case above, the `experimental`
branch started out tracking `master`, but the user probably wanted to
push the `experimental` branch to a new remote branch called
`experimental`. So the correct command would be
`git push origin experimental`.

</p>

The default behavior can be changed by configuring `push.default`. If
you want to go back to the version 1.x behavior, set it to `matching`:

</p>

<div class="highlight highlight-ShellSession">

    $ git config --global push.default matching

</div>

</p>

[See how this feature was
implemented](https://github.com/gitster/git/commit/23c0956441a101b2e8eca7e063e71bdc69a0c415)

</p>

More flexible `ssh` invocation
------------------------------

</p>

Git knows how to connect to a remote host via the SSH protocol, but
sometimes you need to tweak exactly how it makes the connection. If so,
you can now use a new shell variable, `GIT_SSH_COMMAND`, to specify the
command (including arguments) or even an arbitrary snippet of Shell code
that Git should use to connect to the remote host. For example, if you
need to use a different SSH identity file when connecting to a Git
server, you could enter

</p>

<div class="highlight highlight-ShellSession">

    $ GIT_SSH_COMMAND='ssh -i git_id' git clone host:repo.git

</div>

</p>

[See how this feature was
implemented](https://github.com/gitster/git/commit/09d60d785c68c8fa65094ecbe46fbc2a38d0fc1f)

</p>

The credential subsystem is now friendlier to scripting
-------------------------------------------------------

</p>

When Git needs a password (e.g., to connect to a remote repository over
http), it uses the [credential](http://git-scm.com/docs/gitcredentials)
subsystem to query any helpers (like the OS X Keychain helper), and then
finally prompts the user on the terminal. When Git is run from an
automated process like a `cron` job, there is usually no terminal
available and Git will skip the prompt. However, if there *is* a
terminal available, Git may hang forever, waiting for the user to type
something. Scripts which do not expect user input can now set
`GIT_TERMINAL_PROMPT=0` in the environment to avoid this behavior.

</p>

[See how this feature was
implemented](https://github.com/gitster/git/commit/86362f7205a31188846de0aed94620c1f0776931)

</p>

Other
-----

</p>

Some other useful tidbits:

</p>

-   Now Git is cleverer about not rewriting paths in the working tree
    unnecessarily when checking out particular commits. This will help
    reduce the amount of redundant work done during software builds and
    reduce the time that incomplete files are present on the filesystem
    (especially helpful if you are using push-to-deploy). [See how this
    feature was
    implemented](https://github.com/gitster/git/commit/c21df07886bb07a893609ff242e29b1493da1fd8)
    </p>
    <p>
-   Now `git branch -d` supports a `--force/-f` option, which can be
    used to delete a branch even if it hasn't been merged yet.
    Similarly, `git branch -m` supports `--force/-f`, which allows a
    branch to be renamed even if the new name is already in use. This
    change makes these commands more consistent with the many other Git
    commands that support `--force/-f`. [See how these features were
    implemented](https://github.com/gitster/git/commit/15a171f6eb436f9a31986f78bbb115ed4540ad5b)
    </p>
    <p>

</p>

Additional resources
--------------------

</p>

-   [The main Git website](http://git-scm.com/)
-   The book **Pro Git** ([available
    online](http://git-scm.com/book/en/v2)); including its [chapter
    about installing
    Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    </p>
    <p>
-   GitHub's [Guide to setting up
    Git](https://help.github.com/articles/set-up-git/) and [other help
    articles](https://help.github.com/)
    </p>
    <p>

</p>

Don't forget: an important Git security vulnerability was [fixed last
December](https://github.com/blog/1938-vulnerability-announced-update-your-git-clients).
If you haven't upgraded your Git client since then, we recommend that
you do so as soon as possible. The new release, 2.3.0, includes the
security fix, as do the maintenance releases 1.8.5.6, 1.9.5, 2.0.5, and
2.1.4, which were released in December.

</p>

