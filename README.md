# ansible-java

An Ansible role for installing Java 7 JDK.

## Role Variables

- `java_version` - Java JDK and JRE version
- `java_flavor` - Flavor of Java to install (default: `openjdk` but can also be
  `oracle`)
- `java_oracle_accept_license_agreement` - Flag to accept the Oracle license agreement (default: `False`)

## Example Playbook

See the [examples](./examples/) directory.
