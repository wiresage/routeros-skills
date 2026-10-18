# /interface/lte/esim

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/esim

Conditions: !smips; Type: Directory

**Flags**

- `A`: active

**Read-only arguments**

- `interface` (iface_enum)
- `nickname` (string)
- `name` (string)
- `spn` (string)
- `iccid` (string)

## Commands

### /interface/lte/esim/activate

Conditions: !smips; Type: Command

### /interface/lte/esim/deactivate

Conditions: !smips; Type: Command

### /interface/lte/esim/delete

Conditions: !smips; Type: Command

**Arguments**

- `force-delete` (bool): disables profile before deleting it, default: no

### /interface/lte/esim/esim-id

Conditions: !smips; Type: Command

**Arguments**

- `interface` (iface_enum)

**Read-only arguments**

- `eid` (string)

### /interface/lte/esim/provision

Conditions: !smips; Type: Command

**Arguments**

- `interface` (iface_enum)
- `activation-code` (string): Profile activation code. Example: LPA:1$server.example.io$ABCD10EFGHI5KL6M
- `activate` (bool): Activate newly created profile after it is provisioned (default: yes)
- `sm-dp-plus` (string): SM-DP+ server hostname. Example: sm-dp-plus=server.example.io
- `matching-id` (string): An activation code token. Example: matching-id=ABCD10EFGHI5KL6M
- `confirmation-code` (string): An optional code supplied by the operator
- `sm-dp-plus-oid` (string): An optional SM-DP+ supplied by the operator
- `force-confirmation` (bool): Will not ask for confirmation

**Read-only arguments**

- `iccid` (string)
- `spn` (string)
- `name` (string)
- `status` (string)

### /interface/lte/esim/refresh-profile-list

Conditions: !smips; Type: Command

**Arguments**

- `interface` (iface_enum)

### /interface/lte/esim/send-notifications

Conditions: !smips; Type: Command

**Arguments**

- `interface` (iface_enum)

### /interface/lte/esim/set-nickname

Conditions: !smips; Type: Command

**Arguments**

- `nickname` (string)
