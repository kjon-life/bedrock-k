# CONTRIBUTING GUIDELINES

Ultimately kjon-life is a side project. Contribution is necessary, welcome, respected, and appreciated, but there is no SLA.

We do support each other to uphold our [code of conduct](CODE_OF_CONDUCT.md).

Efficiency wins in processing issues and pull requests. These guidelines sustain efficiency.

Please [search](#seek-and-ye-shall-find) to avoid duplicating issues!.

<!-- TOC updateonsave:true depthfrom:2 -->

- [Reporting Issues](#reporting-issues)
  - [You have a problem](#you-have-a-problem)
  - [You have a suggestion](#you-have-a-suggestion)
- [Submitting Pull Requests](#submitting-pull-requests)
  - [Getting started](#getting-started)
  - [You have a solution](#you-have-a-solution)
  - [You have an addition](#you-have-an-addition)
- [Use the Search](#seek-and-ye-shall-find)
- [Commit Guidelines](#commit-guidelines)
  - [Format](#format)
  - [Style](#style)
- [Credits](#credits)

<!-- /TOC -->

## Reporting Issues

### You have a problem

Please be so kind as to [search](#seek-and-ye-shall-find) for any open issue already covering
your problem.

If you find one, comment on it, so we know more people are experiencing it.

Then, you can go ahead and create an issue with as much detail as you can provide.
It should include the data gathered as indicated above, along with the following:

1. How to reproduce the problem
2. What the correct behavior should be
3. What the actual behavior is

Please copy to anyone relevant (e.g. plugin maintainers) by mentioning their GitHub handle
(starting with `@`) in your message.

We will do our very best to help you.

### You have a suggestion

Please be so kind as to [search](#seek-and-ye-shall-find) for any open issue already covering
your suggestion.

If you find one, comment on it, so we know more people are supporting it.

If not, you can go ahead and create an issue. Please copy to anyone relevant (e.g. plugin
maintainers) by mentioning their GitHub handle (starting with `@`) in your message.

## Submitting Pull Requests

### Getting started

You should be familiar with the basics of
[contributing on GitHub](https://help.github.com/articles/using-pull-requests) and have a fork properly set up.

You MUST always create PRs with _a dedicated branch_ based on the latest upstream tree.

If you create your own PR, please make sure you do it right. Also be so kind as to reference
any issue that would be solved in the PR description body,
[for instance](https://help.github.com/articles/closing-issues-via-commit-messages/)
_"Fixes #XXXX"_ for issue number XXXX.

### You have a solution

Please be so kind as to [search](#seek-and-ye-shall-find) for any open issue already covering
your [problem](#you-have-a-problem), and any pending/merged/rejected PR covering your solution.

If the solution is already reported, try it out and +1 the pull request if the
solution works ok. On the other hand, if you think your solution is better, post
it with reference to the other one so we can have both solutions to compare.

If not, then go ahead and submit a PR. Please copy to anyone relevant (e.g. plugin
maintainers) by mentioning their GitHub handle (starting with `@`) in your message.

### You have an addition

Please [do not](https://github.com/kjon-life/kjon-life/wiki/frontend#yes-it-could-be) send themes for now.

Please be so kind as to [search](#seek-and-ye-shall-find) for any pending, merged or rejected Pull Requests
covering or related to what you want to add.

If you find one, try it out and work with the author on a common solution.

If not, then go ahead and submit a PR. Please copy to anyone relevant (e.g. plugin
maintainers) by mentioning their GitHub handle (starting with `@`) in your message.

For any extensive change, such as a new CSS, or moving json into Redis, or adding a database, you will have to find testers to +1 your PR.

----

## Seek and ye shall find

_May the Force (of search) be with you_

GitHub offers [many search features](https://help.github.com/articles/searching-github/) to help you check whether a similar contribution to yours already exists. Please search before making any contribution, it avoids duplicates and eases maintenance. This covers 90% of all issues.

Take a look at the [FAQ](https://github.com/kjon-life/kjon-life/wiki/FAQ) to be sure your contribution has not already come up.

Can't find anything similar in search or FAQ? Then [create an issue](#reporting-issues) or fork the repo and [submit a PR](#submitting-pull-requests).

----

## Commit Guidelines

kjon-life uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. The automatic changelog tool uses these to automatically generate a changelog based on the commit messages. Here's a guide to writing a commit message to allow this:

### Format

```
type(scope)!: subject
```

- `type`: the type of the commit is one of the following:

  - `build`: changes to the build system
  - `chore`: for other changes that don't match previous types
  - `ci`: changes to the CI system
  - `docs`: documentation changes
  - `feat`: new features
  - `fix`: bug fixes
  - `perf`: performance improvements
  - `refactor`: refactor of a particular code section without introducing new features or bug fixes
  - `revert` : revert previous commit
  - `style`: code style improvements
  - `test`: changes to the test suite

- `scope`: section of the codebase that the commit makes changes to. If it makes changes to many sections, or if no section in particular is modified, leave blank without the parentheses.  
  Examples:

  - Commit that changes the `git` plugin:
  ```
  feat(git): add alias for `git commit`
  ```

  - Commit that changes many plugins:
  ```
  style: fix inline declaration of arrays
  ```



- `!`: this goes after the `scope` (or the `type` if scope is empty), to indicate that the commit
  introduces breaking changes.

  Optionally, you can specify a message that the changelog tool will display to the user to indicate
  what's changed and what they can do to deal with it. You can use multiple lines to type this message;
  the changelog parser will keep reading until the end of the commit message or until it finds an empty
  line.

  Example (made up):

  ```
  feat(v0.0.1)!: change from static HTML and CSS to 

  BREAKING CHANGE: the glyph to indicate when a git repository is dirty has
  changed from a Powerline character to a standard UTF-8 emoji. You can
  change it back by setting `ZSH_THEME_DIRTY_GLYPH`.

  Fixes #420

  Co-authored-by: Username <email>
  ```

- `subject`: a brief description of the changes. This will be displayed in the changelog. If you need
  to specify other details, you can use the commit body, but it won't be visible.

  Formatting tricks: the commit subject may contain:

  - Links to related issues or PRs by writing `#issue`. This will be highlighted by the changelog tool:
    ```
    feat(archlinux): add support for aura AUR helper (#9467)
    ```

  - Formatted inline code by using backticks: the text between backticks will also be highlighted by
    the changelog tool:
    ```
    feat(shell-proxy): enable unexported `DEFAULT_PROXY` setting (#9774)
    ```

### Style

The first commit line <em>must</em> be short. Think Tweet. Short: [Format](#format) the first line but use the commit body if necessary to be clear and precise enough that users will know what changed by just looking at the changelog.



## Credits

We borrowed heavily from other projects for our contribution guidelines, particularly [@ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/blob/master/CONTRIBUTING.md)