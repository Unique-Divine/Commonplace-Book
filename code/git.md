# Git

Git (cookbook)

## Fundamental Concepts

### Local branch vs. remote branch

- **local branch**: a branch only the local user can see. It exists only on your local machine.
  - Ex. Create local branch named "myNewBranch": `git branch myNewBranch`

- **remote branch**: a branch on a remote location (in most cases 'origin'). Local branches can be pushed to 'origin' (a remote branch), where other users can track it.
  - Ex. Push local branch, "myNewBranch", to the remote, "origin" so that a new branch named "myNewBranch" is created on the remote machine ("origin"):  
  `git push -u origin myNewBranch`

- **remote tracking branch**: A local copy of a remote branch. When 'myNewBranch' is pushed to 'origin' using the command above, a remote tracking branch named 'origin/myNewBranch' is created on your local machine.
- **local tracking branch**: a local branch that is tracking another
branch.

source(s): [SNce & Brian Webster.stackoverflow.com](https://stackoverflow.com/questions/16408300/what-are-the-differences-between-local-branch-local-tracking-branch-remote-bra)

### HEAD, master, and origin

I highly recommend the book "Pro Git" by Scott Chacon. Take time and
really read it, while exploring an actual git repo as you do.

- **HEAD**: the current commit your repo is on. Most of the time HEAD points to the latest commit in your current branch, but that doesn't have to be the case. HEAD really just means "what is my repo currently pointing at".  
  In the event that the commit HEAD refers to is not the tip of any branch, this is called a "**detached head**".
- **master**: the name of the default branch that git creates for you when first creating a repo. In most cases, "master" means "the main branch". Most shops have everyone pushing to master, and master is considered the definitive view of the repo. But it's also common for release branches to be made off of master for releasing. Your local repo has its own master branch, that almost always follows the master of a remote repo.
- **origin**: the default name that git gives to your main remote repo. Your box has its own repo, and you most likely push out to some remote repo that you and all your coworkers push to. That remote repo is almost always called origin, but it doesn't have to be.
- `HEAD` is an official notion in git. `HEAD` always has a well-defined meaning. `master` and `origin` are common names usually used in git, but they don't have to be.

source: [HEAD, master, and origin. Matt Greer & Jacqueline P. via
stackoverflow.com](https://stackoverflow.com/questions/8196544/what-are-the-git-concepts-of-head-master-origin)

### Large File Storage

See https://git-lfs.github.com

## Git§2

### SSH keys

An SSH key is an alternative to username/password authorization on
GitHub. This will allow you to bypass entering your username and
password for future GitHub commands.

SSH keys come in pairs, a public key that gets shared with services like
GitHub, and a private key that is stored only on your computer. If the
keys match, you're granted access.

The cryptography behind SSH keys ensures that no one can reverse
engineer your private key from the public one.

[SSH Keys for GitHub [article]](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html)

Generating a new SSH key: Follow [Generating a new SSH key and adding it to the ssh-agent [article]](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Permanently removing files from commit history

WHy do this? You may have commited a password, some other sensitive
information, or a large file that you want to remove from github. If the
change is only a few commits back, you can "rebase" changes out of the
history. I actually need to do this for a much older set of files and
accidentally uploaded a textbook that takes up almost a GB of space.

`git filter-branch --force --index-filter "git rm --cached --ignore-unmatch PathToSensitiveFile" --prune-empty --tag-name-filter cat -- --all`

All you need to change is the `PathToSensitiveFile` item. Once you've used this command for all of the files you'd like to get rid of, update the origin by typing `git push origin --force --all`.

## Branching

Suppose your application is stable. Later, you discover a gigantic bug
that was passing silently. You want to write some tests, fix the bug,
and eventually have a stable, passing application once again. To do
this, you'd create a branch for the fix and push the branch to the
remote so that all of the developers on your team can collaborate and
make the fix.

Once all of the necessary changes have been made and the application is
stable, someone from the team would commit merge the commits from the
other branch into master. Since the commit history from the branch will
have been saved to master, the new branch could be deleted without loss
of information (if you no longer wanted to work on this branch).

View branches:  `git branch`

Switch branches:  `git checkout [branch-name]`

### Merging

Merge the specified branch's history into the current one.
`git merge [branch]`

### Deleting branches

Delete local branch
`git branch -d [branch-name]`

Delete remote branch
`git push origin --delete [branch-name]`

<!-- TODO: Write about git-flow and branching models  -->
<!-- https://nvie.com/posts/a-successful-git-branching-model/ -->
