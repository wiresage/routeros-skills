# /tr069-client

> Source: https://manual.mikrotik.com/docs/cli-reference/tr069-client

Package: tr069-client; Type: Settings Directory

**Arguments**

- `enabled` (enum: yes | no): Enables or disables the CWMP protocol.
- `acs-url` (string): URL of the Auto Configuration Server (ACS). If the ACS is accessed using HTTPS, a Root CA must be imported in the client certificate store to verify the ACS server certificate.
- `username` (string): HTTP authentication username used by the CPE to authenticate with the ACS.
- `password` (string): HTTP authentication password used by the CPE to authenticate with the ACS.
- `periodic-inform-enabled` (bool): Enables or disables CPE periodic session initiation. The timer starts after every successful session. When a session is started by the periodic interval, the Inform RPC contains a "2 PERIODIC" event. Maps to `Device.ManagementServer.PeriodicInformEnable`.
- `periodic-inform-interval` (time): Timer interval of the periodic inform. Maps to `Device.ManagementServer.PeriodicInformInterval`.
- `connection-request-username` (string): Username used by the ACS to authenticate with the CPE for Connection Requests.
- `connection-request-password` (string): Password used by the ACS to authenticate with the CPE for Connection Requests.
- `connection-request-port` (num): Port on which the CPE listens for Connection Requests from the ACS.
- `provisioning-code` (string): Provisioning code for the device.
- `client-certificate` (enum: none): Certificate from the certificate store that can be used by the ACS for extra authentication.
- `check-certificate` (enum: yes | no): Whether to check the ACS server certificate.

**Read-only arguments**

- `status` (enum: disabled | initializing | error | waiting-url | running): Informative status of the CWMP client. Disabled means the protocol is disabled, waiting-url means the protocol is enabled but the ACS URL is not configured, and running means CWMP is configured correctly and will communicate with the ACS on events.
- `last-session-error` (string): User-friendly error description indicating why the previous session did not finish successfully.
- `retry-count` (num): Consecutive unsuccessful session count. If greater than 0, last-session-error should indicate the error. Resets to 0 on a successful session, disabled protocol, or reboot.

## Commands

### /tr069-client/reset-tr069-config

Package: tr069-client; Type: Command

Command completely resets and forgets the tr069-client configuration and state (without affecting other RouterOS configurations). Use this command when CWMP goes into an unresponsive or hung state and should be restored without reinstalling RouterOS.
