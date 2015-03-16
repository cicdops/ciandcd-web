Title: GitLab 7.7.2 and GitLab CI 5.4.2 Released
Date: 2015-01-30 00:00
Slug: gitlab-772-and-gitlab-ci-542-released

Today we release GitLab 7.7.2 (CE and EE) and GitLab CI 5.4.2.

</p>

This release contains two security fixes. We recommend everyone that

uses protected branches, GitLab CI or LDAP to upgrade.

</p>

GitLab 7.7.2 fixes:

</p>

-   Security fix: Fix a bug where developers can push to a protected
    branch
-   Fix an issue where a LDAP user can't login with an existing GitLab
    account

</p>

GitLab CI 5.4.2 contains a single security fix:

</p>

-   Security fix: Fix a bug where a CI user can get the CI project token
    </p>
    <p>
    even if the user does not have access to the project

</p>

