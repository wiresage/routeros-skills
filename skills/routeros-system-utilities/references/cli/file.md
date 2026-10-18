# /file

> Source: https://manual.mikrotik.com/docs/cli-reference/file

Type: Directory

The `/file` menu lists user files on the router's storage and manages them: creating, editing, copying and deleting files and directories. For an uploaded RouterOS `.npk` file, the menu also shows package details, such as the architecture and build time. Files and directories shared through [File Share](https://manual.mikrotik.com/docs/network-management/cloud/file-share) (Back To Home) are marked with the shared flag and have a `url` property with the share link. See the [Files](../guides/system-information-and-utilities/files.md) guide.

**Flags**

- `S` (shared): The file or directory is shared through [File Share](https://manual.mikrotik.com/docs/network-management/cloud/file-share) (Back To Home).

**Arguments**

- `name` (file; mandatory): Name of the file or directory, including the path. A leading `/` is optional.
- `type` (enum: file | directory): Type of the entry. Default: file.
- `contents` (string): The actual content of the file. Limited to just under 60 KiB (61439 bytes): creating a file with longer contents fails, and files larger than that return nothing here. Use [`/file/read`](file.md) to read larger files.

**Read-only arguments**

- `size` (num): File size in bytes.
- `last-modified` (date): Time when the file was created or last modified.
- `package-name` (string): Name of the installable package. Applies only to RouterOS .npk files.
- `package-version` (string): Version of the installable package. Applies only to RouterOS .npk files.
- `package-build-time` (date): Time when the package was built. Applies only to RouterOS .npk files.
- `package-architecture` (string): Architecture that the package is built for. Applies only to RouterOS .npk files.
- `url` (string; syscap=cloud-vpn): URL for cloud VPN file sharing. Shown for files and directories shared through [File Share](https://manual.mikrotik.com/docs/network-management/cloud/file-share) (Back To Home).

## Commands

### /file/copy

Type: Command

Copies a file or directory. Directories are copied recursively, with all their contents. See the [Files](../guides/system-information-and-utilities/files.md#copy-a-file-or-directory) guide.

**Arguments**

- `name` (file): Destination name of the copy. Can include a path, to copy into a different directory.

### /file/head

Type: Command

Prints the first lines of a file's contents. With `as-value`, the lines are returned as an array of strings in `lines`. See the [Files](../guides/system-information-and-utilities/files.md#head-or-tail-a-file) guide.

**Arguments**

- `n` (num; unset): Number of lines to output from the beginning of the file. Range: 1..1000. Default: 10.
- `numbered` (switch): Show line numbers in front of each line.

**Read-only arguments**

- `lines` (object { line: string }): The output lines returned as an array of strings.

### /file/read

Type: Command

Reads a chunk of a file's contents and returns it as a string in `data`. Works with files of any size, unlike the `contents` property, which is limited to just under 60 KiB. See the [Files](../guides/system-information-and-utilities/files.md#read-file-contents) guide.

**Arguments**

- `file` (file): Name of the file to read.
- `chunk-size` (num): Chunk size to read from the file. Required. Range: 1..32768.
- `offset` (num): Offset where to start reading the file. A chunk that continues past the end of the file is shortened; an offset past the end fails.

**Read-only arguments**

- `data` (string): The read data returned as a string.

### /file/tail

Type: Command

Prints the last lines of a file's contents. With `as-value`, the lines are returned as an array of strings in `lines`. See the [Files](../guides/system-information-and-utilities/files.md#head-or-tail-a-file) guide.

**Arguments**

- `n` (num; unset): Number of lines to output from the end of the file. Range: 1..1000. Default: 10.
- `numbered` (switch): Show line numbers in front of each line.

**Read-only arguments**

- `lines` (object { line: string }): The output lines returned as an array of strings.
