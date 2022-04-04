Contributing
============

All contributions are welcome! Just make sure you follow these guidelines and your change/fix/improvement should be
accepted without any problems.

## TL;DR

* **File an issue** if you've found a bug, want to request an improvement, or want to implement new functionality
yourself. Make sure to check no one else has created a similar ticket!
* **Create a pull request** and make sure your commit includes the issue number

## The Long Version

### Step 1: Create an Issue

Before writing any code, make sure to create an issue that describes what you'd like to add, improve or fix. Doing so
allows us to give you any feedback before starting, as it may already be something we've started, also would be good if you check our discord channel (especially if it is a big contribution).

### Step 2: Fork the Repository

This will allow you to branch off and write your change against a separate codebase.

### Step 3: Add an Upstream Remote

To add the upstream remote:

```bash
$ git remote add upstream git@github.com:JaimeObregon/subvenciones.git 
```

### Step 4: Create a Feature Branch

Make sure to give your branch a descriptive name that starts with `feature` and includes the issue number, 
e.g. `feature/123-add-contact-type`.

### Step 5: Push to your Fork

While you're writing code, make sure to push atomic commits to your fork. Also, be sure to include your issue number 
and a description of your change in the commit message, e.g. `#123: Added a new Contact type` or `#234: Fixed a null
pointer when loading single items from the API`.

Remember that different issues go on separate feature branches!

### Step 6: Rebase Against Upstream

Before creating your pull request, rebase your fork against the upstream remote to get the latest changes which will help
minimise merge issues:

```bash
$ git fetch upstream
$ git rebase upstream/develop
```

### Step 7: Run Tests

Run your tests (if you have any)


### Step 8: Create the Pull Request

Create a pull request from your feature branch, that includes a description of your change. There should only be one
issue per pull request.