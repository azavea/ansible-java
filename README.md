# ansible-java

An Ansible role for installing Java.

## Role Variables

- `java_version` - Java JDK and JRE version
- `java_major_version` - Major version of Java to install (default: `8`)
- `java_flavor` - Flavor of Java to install (default: `openjdk` but can also be `oracle`)
- `java_oracle_accept_license_agreement` - Flag to accept the Oracle license agreement (default: `False`)

## Testing

Tests are driven by [Molecule](http://molecule.readthedocs.io/). To run the test suite, install Molecule and run ` molecule test` from the folder containing `molecule.yml`. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) Python script in the [tests](./tests/) directory, or add a function to [test_java.py](./tests/test_java.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Usage

```
$ pip install -r requirements.txt
$ molecule test
```
