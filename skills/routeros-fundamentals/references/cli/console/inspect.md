# /console/inspect

> Source: https://manual.mikrotik.com/docs/cli-reference/console/inspect

Type: Command

**Arguments**

- `request` (ubit (self, child, completion, highlight, syntax, error))
- `path` (multi { name: string })
- `input` (string)

**Read-only arguments**

- `type` (enum: self | child | completion | highlight | syntax | error)
- `name` (string)
- `node-type` (enum: path | dir | cmd | arg)
- `completion` (string)
- `style` (enum: none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7)
- `offset` (num)
- `preference` (num)
- `show` (bool)
- `highlight` (multi { style: enum (none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7) })
- `symbol` (string)
- `symbol-type` (enum: collection | explanation | definition)
- `nested` (num)
- `nonorm` (bool)
- `text` (string)
