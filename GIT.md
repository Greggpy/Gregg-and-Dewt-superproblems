# Git Cheat Sheet

## Table of Contents

0. [Git File Lifecycle Flowchart](#git-file-lifecycle-flowchart)
1. [Setting Up and Cloning Repositories](#setting-up-and-cloning-repositories)
2. [Basic Local Changes](#basic-local-changes)
3. [Branching and Merging](#branching-and-merging)
4. [Updating and Publishing](#updating-and-publishing)
5. [Inspection and Comparison](#inspection-and-comparison)
6. [Undoing Changes](#undoing-changes)
7. [Working with Remotes](#working-with-remotes)

## Git File Lifecycle Flowchart

1. **File Creation/Modification**

   - Edit or create a file in your working directory.

2. **Staging the File**

   - Command: `git add <filename>`
   - Stage your changes in preparation for a commit.

3. **Committing the File**

   - Command: `git commit -m "Commit message"`
   - Commit your staged changes to your local repository.

4. **Pushing to Remote Repository (Optional)**

   - Command: `git push`
   - Push your local commits to the remote repository.

5. **Pulling Updates from Remote (Optional)**

   - Command: `git pull`
   - Pull updates from the remote repository to your local repository.

6. **File Modification and Further Commits**
   - Repeat the process as needed for further changes.

## Setting Up and Cloning Repositories

### Command Line: `git init`

- **Description:** Initializes a new Git repository.
- **GUI Equivalent:** Typically, 'New Repository' or 'Initialize Repository' in the GUI menu.

### Command Line: `git clone [URL]`

- **Description:** Clones a repository from an existing URL.
- **GUI Equivalent:** 'Clone Repository' option where you paste the repository URL.

## Basic Local Changes

### Command Line: `git status`

- **Description:** Shows the status of changes as untracked, modified, or staged.
- **GUI Equivalent:** Automatically displayed in most GUIs, often with color-coded files.

### Command Line: `git add [file]`

- **Description:** Stages a file for the next commit.
- **GUI Equivalent:** 'Stage Changes' button or drag-and-drop files into the 'staged' area.

### Command Line: `git commit -m "[commit message]"`

- **Description:** Records staged snapshots with a descriptive message.
- **GUI Equivalent:** 'Commit' button with a field to enter the commit message.

## Branching and Merging

### Command Line: `git branch`

- **Description:** Lists all local branches.
- **GUI Equivalent:** Branch list, often in a dropdown or a separate pane.

### Command Line: `git branch [branch-name]`

- **Description:** Creates a new branch.
- **GUI Equivalent:** 'New Branch' or similar option.

### Command Line: `git checkout [branch-name]`

- **Description:** Switches to a specified branch.
- **GUI Equivalent:** Clicking or selecting the branch from the branch list.

### Command Line: `git merge [branch]`

- **Description:** Merges the specified branch into the current branch.
- **GUI Equivalent:** Often a 'Merge' button after selecting a branch from the branch list.

## Updating and Publishing

### Command Line: `git pull`

- **Description:** Fetches changes from the remote repository and merges them into the current branch.
- **GUI Equivalent:** 'Pull' button.

### Command Line: `git push`

- **Description:** Pushes all local branch commits to the remote repository.
- **GUI Equivalent:** 'Push' button.

## Inspection and Comparison

### Command Line: `git log`

- **Description:** Shows the commit logs.
- **GUI Equivalent:** A separate log/history view where you can see past commits.

### Command Line: `git diff`

- **Description:** Shows the file differences which are not yet staged.
- **GUI Equivalent:** Often a 'Diff' pane or window showing changes in a side-by-side view.

## Undoing Changes

### Command Line: `git reset [file]`

- **Description:** Unstages a file, but it preserves the file contents.
- **GUI Equivalent:** Option to unstage files usually available with a right-click or dedicated button.

### Command Line: `git checkout -- [file]`

- **Description:** Discards changes in the working directory.
- **GUI Equivalent:** Often a 'Discard Changes' option on right-clicking the file.

### Command Line: `git revert [commit]`

- **Description:** Creates a new commit that undoes all of the changes made in a specified commit.
- **GUI Equivalent:** Revert option in the commit history.

## Working with Remotes

### Command Line: `git remote -v`

- **Description:** Lists all the remotes.
- **GUI Equivalent:** Displayed in repository settings or a dedicated remotes section.

### Command Line: `git remote add [name] [url]`

- **Description:** Adds a new remote.
- **GUI Equivalent:** Option to add a remote in the repository settings.
