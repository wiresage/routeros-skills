# /system/keymat-provider

> Source: https://manual.mikrotik.com/docs/cli-reference/system/keymat-provider

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string)
- `type` (enum: qkd | hkdf)
- `key-size` (num): in bits
- `qkd-address` (string): KME device address
- `qkd-kme-id` (string): should match the KME ID in the received TLS certificate
- `qkd-certificate` (enum: none): this also specifies your SAE ID
- `qkd-peer-sae-id` (string): peer (master or slave) SAE ID
- `qkd-cache-size` (num): number of unused keys to keep in cache
- `hkdf-secret` (string)
- `hkdf-hash` (enum: sha256 | sha512)

**Read-only arguments**

- `qkd-cache-state` (num): number of current unused keys in cache
- `qkd-total-keys-received` (num): total number of received keys

## Commands

### /system/keymat-provider/qkd-get-key

Type: Command

**Arguments**

- `additional-sae-ids` (multi { array-id, sae-id: string }): additional SAEs which will also get the generated key
- `number` (num): number of keys to generate

**Read-only arguments**

- `keys` (object { qkd-key: super { key-id: string , [key] : string } })

### /system/keymat-provider/qkd-get-key-with-ids

Type: Command

**Arguments**

- `key-ids` (multi { array-id, key-id: string })

**Read-only arguments**

- `keys` (object { qkd-key: super { key-id: string , [key] : string } })

### /system/keymat-provider/qkd-get-status

Type: Command

**Arguments**

- `sae-id` (string): if not specified, peer-sae-id will be used

**Read-only arguments**

- `source-kme-id` (string)
- `target-kme-id` (string)
- `master-sae-id` (string)
- `slave-sae-id` (string)
- `key-size` (num)
- `stored-key-count` (num)
- `max-key-count` (num)
- `max-key-per-request` (num)
- `max-key-size` (num)
- `min-key-size` (num)
- `max-sae-id-count` (num)
