# /container

> Source: https://manual.mikrotik.com/docs/cli-reference/container

Package: container; Type: Directory

**Flags**

- `S`: stopped
- `N`: starting
- `R`: running
- `T`: stopping
- `E`: downloading/extracting
- `D`: deleting
- `F`: download/extract failed
- `C`: starting-with-healthcheck
- `H`: healthy
- `U`: unhealthy

**Arguments**

- `file` (file)
- `remote-image` (string)
- `ignore-remote-image-change` (bool)
- `check-certificate` (bool)
- `name` (string)
- `privileged` (bool)
- `interface` (multi { interface: iface_enum }; mandatory)
- `env` (object { key-and-value-element: super { ! , key-and-value: composite { key: string , value: string } } })
- `envlists` (multi { envlist: enum })
- `entrypoint` (multi { cmd: string })
- `cmd` (multi { cmd: string })
- `shell` (multi { cmd: string })
- `stop-signal` (enum: 1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)
- `stop-time` (time)
- `root-dir` (file)
- `layer-dir` (file)
- `mount` (object { src-dst-mode: composite { src: file , dst-mode: composite { dst: string , mode: enum (rw | ro | rw,noexec | ro,noexec) } } })
- `tmpfs` (object { dst-size-mode: composite { dst: string , size-mode: composite { size: num , mode: string } } })
- `mountlists` (multi { mountlist: enum })
- `shm-size` (num)
- `dns` (multi { dns-server-ip: address (flags=46) })
- `default-dns` (multi { dns-server-ip: address (flags=46) })
- `hostname` (string)
- `domain-name` (string)
- `workdir` (string)
- `logging` (bool)
- `start-on-boot` (bool)
- `stop-on-unhealthy` (bool)
- `restart-policy` (enum: no | on-failure | always)
- `restart-max-count` (num)
- `restart-interval` (time)
- `user` (string)
- `cpu-list` (multi { cpu: enum })
- `memory-high` (num)
- `memory-max` (num)
- `swap-max` (num)
- `devices` (object { dst-size-mode: composite { device: enum , container-dev-name: string } })
- `hosts` (object { host-entry: composite { host-name: string , host-addr: address (flags=46) } })
- `healthcheck-cmd` (multi { healthcheck-cmd: string })
- `healthcheck-interval` (time)
- `healthcheck-timeout` (time)
- `healthcheck-start-period` (time)
- `healthcheck-start-interval` (time)
- `healthcheck-retries` (num)
- `healthcheck-status` (string)

**Read-only arguments**

- `tag` (string)
- `os` (string)
- `arch` (string)
- `env-current` (object { key-and-value: composite { key: string , value: string } })
- `default-entrypoint` (string)
- `default-cmd` (string)
- `default-shell` (string)
- `default-stop-signal` (enum: 1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)
- `default-workdir` (string)
- `restart-count` (num)
- `default-user` (string)
- `memory-current` (num)
- `swap-current` (num)
- `cpu-usage` (num)
- `container-size` (num)
- `data-size` (num)
- `image-id` (string)
- `config-json` (string)
- `layers` (multi { layer: enum })
- `default-healthcheck-cmd` (multi { default-healthcheck-cmd: string })
- `default-healthcheck-interval` (time)
- `default-healthcheck-timeout` (time)
- `default-healthcheck-start-period` (time)
- `default-healthcheck-start-interval` (time)
- `default-healthcheck-retries` (num)

## Commands

### /container/kill

Package: container; Type: Command

**Arguments**

- `signal` (enum: 1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)

### /container/repull

Package: container; Type: Command

**Arguments**

- `file` (file)
- `remote-image` (string)

### /container/restart

Package: container; Type: Command

### /container/save

Package: container; Type: Command

**Arguments**

- `file` (file)
- `commit` (switch; unset)
- `name` (string; unset)

### /container/start

Package: container; Type: Command

### /container/stop

Package: container; Type: Command

### /container/update

Package: container; Type: Command
