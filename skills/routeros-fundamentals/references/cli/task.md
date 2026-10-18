# /task

> Source: https://manual.mikrotik.com/docs/cli-reference/task

Type: Directory

**Flags**

- `T`: terminated
- `C`: current
- `A`: autosave

**Read-only arguments**

- `term-pid` (num)
- `task-id` (num)
- `user` (string)
- `name` (string)
- `source` (string)
- `file-name` (string)
- `save-interval` (time)
- `append` (switch)

## Commands

### /task/add

Type: Command

**Arguments**

- `source` (string): command that should be executed in the background
- `switch-to` (switch): switch to background view immediately
- `append` (switch): append output to file
- `file-name` (file): default filename for output
- `save-interval` (time): autosave interval for when filename is set
- `max-lines` (num): maximum buffer lines
- `save-timestamp` (switch): add a timestamp to the saved file
- `no-header-paging` (switch): don't page header to output
- `max-size` (num): maximum save file size

### /task/next

Type: Command

### /task/terminate

Type: Command

**Arguments**

- `id` (num)
