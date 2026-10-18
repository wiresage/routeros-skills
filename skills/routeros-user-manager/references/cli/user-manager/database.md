# /user-manager/database

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/database

Package: userman-5; Type: Settings Directory

**Arguments**

- `db-path` (string)

**Read-only arguments**

- `found-legacy-db-path` (string)
- `db-size` (num)
- `free-disk-space` (num)

## Commands

### /user-manager/database/load

Package: userman-5; Type: Command

**Arguments**

- `name` (file)

### /user-manager/database/migrate-legacy-db

Package: userman-5; Type: Command

**Arguments**

- `database-path` (file)
- `overwrite` (bool)

### /user-manager/database/optimize-db

Package: userman-5; Type: Command

### /user-manager/database/save

Package: userman-5; Type: Command

**Arguments**

- `name` (file)
- `overwrite` (bool)
